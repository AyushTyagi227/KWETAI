import psycopg2

conn = psycopg2.connect(
   database="mySQL", user='user1', password='kwit', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

sql = '''CREATE database kwitai''';

cursor.execute(sql)
print("Database created successfully........")

conn.close()