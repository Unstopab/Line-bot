import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a line-bot-rent').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

delete_table_query = '''DROP TABLE IF EXISTS rent_info'''
cursor.execute(delete_table_query)
conn.commit()