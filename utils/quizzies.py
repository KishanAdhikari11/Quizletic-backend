def generate_quiz(content):
    prompt = f"""
    Create 5 multiple-choice questions with 4 options and answers from:
    {content}

    Format:
    Q1. ...
    A. ...
    B. ...
    C. ...
    D. ...
    Answer: ...
    """
    return llm.complete(prompt).text
