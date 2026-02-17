from flask import Blueprint, request, jsonify
import sqlite3

test_bp = Blueprint("test_bp", __name__)

DB_NAME = "database.db"


def get_conn():
    return sqlite3.connect(DB_NAME)


# -----------------------------
# POST: Submit answers (Level Test)
# -----------------------------
@test_bp.route("/api/submit_answer", methods=["POST"])
def submit_answer():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"status": "error", "message": "JSON body missing"}), 400

    level = data.get("level")
    answers = data.get("answers", [])

    if level is None:
        return jsonify({"status": "error", "message": "level is required"}), 400

    if not isinstance(answers, list):
        return jsonify({"status": "error", "message": "answers must be a list"}), 400

    # ✅ SIMPLE scoring: count non-empty answers
    score = 0
    for item in answers:
        ans = ""
        if isinstance(item, dict):
            ans = str(item.get("answer", "")).strip()
        if ans:
            score += 1

    # ✅ next level rule
    # if score >= 7 -> go next level
    # else -> stay same level
    next_level = level + 1 if score >= 7 else level

    # ✅ Save result in DB
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO results (level, score) VALUES (?, ?)", (level, score))
    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "score": score,
        "next_level": next_level
    }), 200


# -----------------------------
# GET: View all results
# -----------------------------
@test_bp.route("/api/results", methods=["GET"])
def get_results():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT level, score FROM results")
    rows = cur.fetchall()

    conn.close()

    results = [{"level": r[0], "score": r[1]} for r in rows]

    return jsonify({
        "total_attempts": len(results),
        "results": results
    }), 200

