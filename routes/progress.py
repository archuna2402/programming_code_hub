from flask import Blueprint, request, jsonify
import sqlite3

progress_bp = Blueprint("progress", __name__)

@progress_bp.route("/api/save_progress", methods=["POST"])
def save_progress():
    data = request.json

    regno = data.get("regno")
    module = data.get("module")
    level = data.get("level")
    score = data.get("score")

    completed = 1 if score >= 50 else 0

    conn = sqlite3.connect("questions.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO progress (regno, module, level, score, completed)
        VALUES (?, ?, ?, ?, ?)
    """, (regno, module, level, score, completed))

    conn.commit()
    conn.close()

    return jsonify({"message": "Progress saved"})
