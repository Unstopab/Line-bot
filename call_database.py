  
import psycopg2
import os

def line_insert_record(record_list):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()

    table_columns = '(message)'
    postgres_insert_query = f"""INSERT INTO alpaca_training {table_columns} VALUES (%s)"""

    cursor.executemany(postgres_insert_query)
    conn.commit()

    message = f"恭喜您！ {cursor.rowcount} 筆資料成功匯入 message 表單！"
    print(message)

    cursor.close()
    conn.close()
    
    return message