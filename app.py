from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
from routes.test import test_bp
from database import get_connection, init_db   # ✅ DB helpers

app = Flask(__name__)
CORS(app)

app.secret_key = "pyzone_secret_key"  # ✅ required for session

app.register_blueprint(test_bp)

# ✅ Make sure DB + tables exist
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        regno = request.form.get("regno")
        password = request.form.get("password")

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE regno = ? AND password = ?",
            (regno, password)
        )
        user = cur.fetchone()
        conn.close()

        if user:
            session["regno"] = regno
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="❌ Invalid reg no or password")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "regno" not in session:
        return redirect(url_for("login"))

    # ✅ show dashboard page
    return render_template("dashboard.html", regno=session["regno"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
