import psycopg2

try:
    pg_conn = psycopg2.connect(
        dbname='nexpressdatawarehouse',  # Tên cơ sở dữ liệu
        user='postgres',                  # Tên người dùng
        password='12345678',             # Mật khẩu
        host='localhost',                 # Hoặc 'my_postgres' nếu trong container khác
        port='5432'
    )

    cursor = pg_conn.cursor()
    cursor.execute("SELECT version();")  # Kiểm tra phiên bản PostgreSQL
    version = cursor.fetchone()
    print("Đã kết nối đến PostgreSQL. Phiên bản:", version)

except Exception as e:
    print("Lỗi kết nối PostgreSQL:", e)

finally:
    if cursor:
        cursor.close()
    if pg_conn:
        pg_conn.close()
try:
    pg_conn = psycopg2.connect(
        dbname='nexpressdatawarehouse',
        user='postgres',
        password='12345678',
        host='localhost',
        port='5432'
    )

    cursor = pg_conn.cursor()
    cursor.execute("INSERT INTO your_table (column1, column2) VALUES ('value1', 'value2');")
    pg_conn.commit()
    print("Dữ liệu đã được lưu trữ thành công!")

except Exception as e:
    print("Lỗi kết nối PostgreSQL:", e)

finally:
    if cursor:
        cursor.close()
    if pg_conn:
        pg_conn.close()

