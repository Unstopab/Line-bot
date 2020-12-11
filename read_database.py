import os
import psycopg2

DATABASE_URL = os.popen('heroku config:get DATABASE_URL -a line-bot-rent').read()[:-1]

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'rent_info'")
cursor.execute("SELECT * FROM rent_info") #找出所有

data = []
while True:
    temp = cursor.fetchone()
    if temp:
        data.append(temp)
    else:
        break
print(data)