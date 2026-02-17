from database import get_connection, init_db

init_db()

conn = get_connection()
cursor = conn.cursor()

# Demo user
cursor.execute(
    "INSERT OR IGNORE INTO users (regno, password) VALUES (?, ?)",
    ("715023243016", "admin123")
)

conn.commit()
conn.close()

print("✅ Demo user ready")
print("Reg No: 715023243016")
print("Password: admin123")
