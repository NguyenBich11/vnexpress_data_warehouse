# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import json
import csv
import os
import pandas as pd
import numpy as np
import random
import psycopg2
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from pymongo import MongoClient
from collections import Counter
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from scrapy.exceptions import DropItem

class MongoDBVnexpressDataWarehousePipeline:
    def __init__(self):
        # Connection String
        econnect = str(os.environ['Mongo_HOST'])
        # self.client = pymongo.MongoClient('mongodb://mymongodb:27017')
        self.client = pymongo.MongoClient('mongodb://'+econnect+':27017')
        self.db = self.client['vnexpressdatawarehouse'] #Create Database      
    
    def process_item(self, item, spider):
        
        collection =self.db['tblVnexpress'] #Create Collection or Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       

class JsonDBVnexpressDataWarehousePipeline:
    def process_item(self, item, spider):
        with open('jsondatavnexpress.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item

class CSVDBVnexpressDataWarehousePipeline:
    def __init__(self):
        # Mở file một lần và giữ mở cho toàn bộ quá trình
        self.file = open('csvdatavnexpress.csv', 'a', encoding='utf-8', newline='')
        self.fieldnames = ['title', 'author', 'date', 'location', 'disease_name', 'count_comments', 'total_like', 'content']
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        # Ghi tiêu đề vào file nếu file trống
        if os.stat('csvdatavnexpress.csv').st_size == 0:
            self.writer.writeheader()

    def process_item(self, item, spider):
        # In ra item để kiểm tra
        print(f'Writing item to CSV: {item}')  # Kiểm tra item
        self.writer.writerow({
            'title': item['title'],
            'author': item['author'],
            'date': item['date'],
            'location': item['location'],
            'disease_name': item['disease_name'],
            'count_comments': item['count_comments'],
            'total_like': item['total_like'],
            'content': item['content']
        })
        return item

    def close_spider(self, spider):
        self.file.close()  # Đảm bảo file được đóng khi spider kết thúc

    
class ProcessDataToPostgreSQLPipeline:
    def __init__(self):
        # Kết nối tới MongoDB
        econnect = str(os.environ['Mongo_HOST'])
        self.client = MongoClient("mongodb://" + econnect + ":27017")
        self.db = self.client["vnexpressdatawarehouse"]
        self.collection = self.db["tblVnexpress"]

        # Kết nối tới PostgreSQL
        self.conn = psycopg2.connect(
            dbname='vnexpress',
            user='postgres',
            password='postgres',
            host='mypostgres',  # Đảm bảo sử dụng tên container
            port='5432'
        )
        self.cursor = self.conn.cursor()

        # Tạo bảng nếu chưa tồn tại
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Author (
            author_id SERIAL PRIMARY KEY,
            author_name TEXT UNIQUE NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Post (
            post_id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INT REFERENCES Author(author_id),
            disease_name TEXT,
            location TEXT NOT NULL,
            date DATE NOT NULL
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS PostDetail (
            post_id INT PRIMARY KEY REFERENCES Post(post_id),
            count_comments INT NOT NULL,
            total_like INT NOT NULL,
            day_in_week TEXT NOT NULL,
            time TIMESTAMP NOT NULL,
            season TEXT NOT NULL,
            content_count INT NOT NULL,
            content TEXT
        )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        # Đọc dữ liệu từ MongoDB thành DataFrame của pandas
        data = list(self.collection.find())
        df = pd.DataFrame(data)

        # Xử lý dữ liệu NaN
        df = df.dropna(subset=['title', 'date'])
        df['disease_name'] = df['disease_name'].replace(np.nan, 'unknown')
        df = self.random_name_author(df)
        df = self.random_name_location(df)

        # Xử lý cột date
        pattern = r'^(Thứ \w+|Chủ nhật), \d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2} \(GMT\+7\)$'
        df['date'] = df['date'].astype(str)
        invalid_rows = df[~df['date'].str.match(pattern)]
        if not invalid_rows.empty:
            print("Invalid date rows:")
            print(invalid_rows['date'])

        # Hàm để trích xuất thông tin ngày
        def extract_date_info(row):
            split_data = row.split(', ')
            if len(split_data) < 3:
                return pd.Series([None, None, None])
            try:
                date = datetime.strptime(split_data[1], '%d/%m/%Y')
                date_in_week = split_data[0]
                time = split_data[2].split(' ')[0]
                return pd.Series([date, date_in_week, time])
            except ValueError:
                return pd.Series([None, None, None])

        # Áp dụng hàm để tạo các cột mới
        df[['date', 'day_in_week', 'time']] = df['date'].apply(extract_date_info)
        df['content_count'] = df['content'].apply(lambda x: len(x.split()))

        # Thêm cột season
        df['season'] = df['date'].apply(lambda x: self.get_season(x))

        # Di chuyển cột content vào cuối DataFrame
        column_name = 'content'
        df = df[[col for col in df.columns if col != column_name] + [column_name]]

        # Chèn dữ liệu đã xử lý vào PostgreSQL
        for _, row in df.iterrows():
            author_id = self.insert_author(row['author'])
            
             # Thêm bài viết vào bảng Post
            insert_query = """
            INSERT INTO Post (title, author_id, disease_name, location, date)
            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (title, date) DO NOTHING RETURNING post_id;
            """
            
            try:
                self.cursor.execute(insert_query, (
                    row['title'],
                    author_id,
                    row['disease_name'],
                    row['location'],
                    row['date'],
                ))
                post_id = self.cursor.fetchone()[0]  # Lấy post_id vừa chèn
                self.conn.commit()

                # Thêm dữ liệu vào bảng PostDetail
                insert_detail_query = """
                INSERT INTO PostDetail (post_id, count_comments, total_like, day_in_week, time, season, content_count, content)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (post_id) DO NOTHING;
                """
                self.cursor.execute(insert_detail_query, (
                    post_id,
                    row['count_comments'],  # Giả sử bạn có cột này trong DataFrame
                    row['total_like'],     # Giả sử bạn có cột này trong DataFrame
                    row['day_in_week'],    # Giả sử bạn có cột này trong DataFrame
                    row['time'],           # Giả sử bạn có cột này trong DataFrame
                    row['season'],           # Giả sử bạn có cột này trong DataFrame
                    row['content_count'],   # Giả sử bạn có cột này trong DataFrame
                    row['content'],        # Giả sử bạn có cột này trong DataFrame
                ))
                self.conn.commit()  # Cam kết thay đổi cho PostDetail

            except Exception as e:
                print(f"Error inserting item into PostgreSQL: {e}")
                self.conn.rollback()  # Hoàn tác nếu có lỗi

        return item

    def insert_author(self, author_name):
        self.cursor.execute("""
        INSERT INTO Author (author_name) VALUES (%s) ON CONFLICT (author_name) DO NOTHING RETURNING author_id;
        """, (author_name,))
        author_id = self.cursor.fetchone()
        if author_id is None:
            self.cursor.execute("SELECT author_id FROM Author WHERE author_name = %s;", (author_name,))
            author_id = self.cursor.fetchone()
        return author_id[0]
    
    def get_season(self, date):
        month = date.month
        if month in [1, 2, 3]:
            return 'Xuân'
        elif month in [4, 5, 6]:
            return 'Hạ'
        elif month in [7, 8, 9]:
            return 'Thu'
        else:
            return 'Đông'

    def random_name_author(self, df):
        unique_names = df['author'].dropna().unique().tolist()
        def get_random_name():
            return random.choice(unique_names)
        df['author'] = df['author'].fillna(df['author'].apply(lambda x: get_random_name() if pd.isna(x) else x))
        return df

    def random_name_location(self, df):
        unique_names = df['location'].dropna().unique().tolist()
        def get_random_name():
            return random.choice(unique_names)
        df['location'] = df['location'].fillna(df['location'].apply(lambda x: get_random_name() if pd.isna(x) else x))
        return df

    def close_spider(self, spider):
        self.client.close()
        self.cursor.close()
        self.conn.close()
