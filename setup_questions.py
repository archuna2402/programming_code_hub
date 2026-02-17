import sqlite3

conn = sqlite3.connect("questions.db")
cur = conn.cursor()

questions = [
    ("Python Basics", 1, "What is Python?", "programming language"),
    ("Python Basics", 1, "How do you print in Python?", "print"),
    ("Python Basics", 2, "What is a variable?", "stores data"),
    ("Python Basics", 2, "What data type is 10?", "int"),
    ("Python Basics", 3, "What is a list?", "collection"),
]

cur.executemany(
    "INSERT INTO questions (module, level, question, answer) VALUES (?, ?, ?, ?)",
    questions
)

conn.commit()
conn.close()

print("✅ Questions inserted successfully")
