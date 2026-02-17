import sqlite3

conn = sqlite3.connect("database.db")  # use SAME db file your project uses
cur = conn.cursor()

# create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    regno TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# insert demo user (change later)
cur.execute("INSERT OR IGNORE INTO users (regno, password) VALUES (?, ?)",
            ("715023243016", "admin123"))

conn.commit()
conn.close()

print("✅ users table ready + demo user added")
print("Login details -> regno: 715023243016  password: admin123")
