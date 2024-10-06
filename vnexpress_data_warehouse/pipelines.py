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
    def process_item(self, item, spider):
        with open('csvdatavnexpress.csv', 'a', encoding='utf-8', newline='') as file:
            fieldnames = ['title', 'author', 'date', 'location','disease_name', 'count_comments', 'total_like', 'content']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if isinstance(item, dict):
                writer.writerow([
                    item['title'],
                    item['author'],
                    item['date'],
                    item['location'],
                    item['disease_name'],
                    item['count_comments'],
                    item['total_like'],
                    item['content']
                ])
        return item
    
class ProcessDataToPostgreSQLPipeline:
    def __init__(self):
        # Kết nối tới MongoDB
        econnect = str(os.environ['Mongo_HOST'])
        self.client = MongoClient("mongodb://"+econnect+":27017")
        self.db = self.client["vnexpressdatawarehouse"]
        self.collection = self.db["tblVnexpress"]

        # Kết nối tới PostgreSQL
        self.conn = psycopg2.connect(
            dbname='vnexpress',
            user='postgres',
            password='postgres',
            host='172.18.0.3',
            port='5432'
        )
        self.cursor = self.conn.cursor()

        # Tạo bảng nếu chưa tồn tại
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vnexpress (
            id serial primary key,
            title text,
            author text,
            date timestamp,
            location text,
            disease_name text,
            count_comments int,
            total_like int,
            content text,
            date_in_week text,
            time text,
            content_count int
        )
        """)
        self.conn.commit()

    def process_item(self, item, spider):
        # Đọc dữ liệu từ MongoDB thành DataFrame của pandas
        data = list(self.collection.find())
        df = pd.DataFrame(data)

        # Xử lý dữ liệu NaN
        df = df.dropna(subset=['title', 'date'])

        # Thay thế giá trị NaN trong cột disease_name
        df['disease_name'] = df['disease_name'].replace(np.nan, 'unknown')

        # Gọi hàm random_name cho cột author và location
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
                return pd.Series([None, None, None])  # Trả về None nếu không đủ phần tử
            try:
                date = datetime.strptime(split_data[1], '%d/%m/%Y')
                date_in_week = split_data[0]
                time = split_data[2].split(' ')[0]
                return pd.Series([date, date_in_week, time])
            except ValueError:
                return pd.Series([None, None, None])  # Trả về None nếu không thể phân tích

        # Áp dụng hàm để tạo các cột mới
        df[['date', 'date_in_week', 'time']] = df['date'].apply(extract_date_info)
        # Tính số từ trong cột content
        df['content_count'] = df['content'].apply(lambda x: len(x.split()))

        # Di chuyển cột content vào cuối DataFrame
        column_name = 'content'
        df = df[[col for col in df.columns if col != column_name] + [column_name]]

        # Chèn dữ liệu đã xử lý vào PostgreSQL
        insert_query = """
        INSERT INTO vnexpress (title, author, date, location, disease_name, count_comments, total_like, content, date_in_week, time, content_count)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for _, row in df.iterrows():
            try:
                self.cursor.execute(insert_query, (
                    row['title'],
                    row['author'],
                    row['date'],
                    row['location'],
                    row['disease_name'],
                    row['count_comments'],
                    row['total_like'],
                    row['content'],
                    row['date_in_week'],
                    row['time'],
                    row['content_count']
                ))
                self.conn.commit()
            except Exception as e:
                print(f"Error inserting item into PostgreSQL: {e}")

        return item

    def random_name_author(self, df):
        # Tạo danh sách các tên duy nhất cho author
        unique_names = df['author'].dropna().unique().tolist()

        # Hàm để chọn một tên ngẫu nhiên
        def get_random_name():
            return random.choice(unique_names)

        # Áp dụng hàm lên các giá trị NaN
        df['author'] = df['author'].fillna(df['author'].apply(lambda x: get_random_name() if pd.isna(x) else x))

        return df

    def random_name_location(self, df):
        # Tạo danh sách các tên duy nhất cho location
        unique_names = df['location'].dropna().unique().tolist()

        # Hàm để chọn một tên ngẫu nhiên
        def get_random_name():
            return random.choice(unique_names)

        # Áp dụng hàm lên các giá trị NaN
        df['location'] = df['location'].fillna(df['location'].apply(lambda x: get_random_name() if pd.isna(x) else x))

        return df

    def close_spider(self, spider):
        # Đóng kết nối khi spider kết thúc
        self.client.close()
        self.cursor.close()
        self.conn.close()
