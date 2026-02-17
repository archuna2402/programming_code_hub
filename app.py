from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        regno = request.form.get("regno")
        password = request.form.get("password")

        # Temporary login check
        if regno == "123" and password == "admin":
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

# Dashboard page
@app.route("/dashboard")
def dashboard():
    return "<h2 style='font-family:Arial'>✅ Dashboard Working</h2>"

if __name__ == "__main__":
    app.run(debug=True)
