import random
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is the largest planet in our Solar System?", "options": ["Mars", "Earth", "Jupiter", "Venus"], "answer": "Jupiter"},
    {"question": "What is 5 + 7?", "options": ["10", "12", "14", "15"], "answer": "12"}
]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form
        score = sum(1 for i, q in enumerate(questions) if user_answers.get(str(i)) == q['answer'])
        return render_template('result.html', score=score, total=len(questions))

    random.shuffle(questions)
    return render_template('quiz.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
