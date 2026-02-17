from flask import Blueprint, request, jsonify
import sqlite3

questions_bp = Blueprint("questions", __name__)

@questions_bp.route("/api/questions", methods=["GET"])
def get_questions():
    module = request.args.get("module")
    level = request.args.get("level")

    conn = sqlite3.connect("questions.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT id, question FROM questions WHERE module=? AND level=?",
        (module, level)
    )

    rows = cur.fetchall()
    conn.close()

    data = [
        {"id": row[0], "question": row[1]}
        for row in rows
    ]

    return jsonify(data)
