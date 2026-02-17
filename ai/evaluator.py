def evaluate_answer(question, user_answer):
    """
    Simple AI logic (for now)
    Later we can replace with real AI (GPT, embeddings, etc.)
    """

    # basic keyword-based check
    keywords = question.lower().split()

    score = 0
    for word in keywords:
        if word in user_answer.lower():
            score += 1

    if score >= 2:
        return {
            "result": "correct",
            "score": 10
        }
    else:
        return {
            "result": "wrong",
            "score": 0
        }
