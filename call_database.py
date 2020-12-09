import psycopg2
import os

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(alpaca_name, training, duration, date)'
    postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s,%s,%s,%s)"""

    cursor.executemany(postgres_insert_query, record_list)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 alpaca_training 表單！"
    print(message)

    cursor.close()
    conn.close()
    
    return message


def line_insert_record2(record_list2):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(rent_type, price)'
    postgres_insert_query = f"""INSERT INTO rent_info {table_columns} VALUES (%s,%d)"""

    cursor.executemany(postgres_insert_query, record_list2)
    conn.commit()

    message2 = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 rent_info 表單！"
    print(message2)

    cursor.close()
    conn.close()
    
    return message2