import sqlite3

conn = sqlite3.connect("questions.db")
cur = conn.cursor()

cur.execute("SELECT id, module, level, question FROM questions")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
