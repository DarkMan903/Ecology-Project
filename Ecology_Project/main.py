#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

score = 0

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

#Вторая страница
@app.route('/question1')
def test():
    return render_template('question1.html')

#Третья страница
@app.route('/question1', methods=['POST'])
def question1():
    button_enter = request.form.get('button_enter')
    choise = request.form['choise']
    if choise == '3':
        answer = 'Правильно!'
        return render_template('question1.html', answer=answer, button_enter=button_enter)
    else:
        answer = 'Не правильно!!'
        return render_template('question1.html', answer=answer, button_enter=button_enter)

@app.route('/question2')
def q1():
    return render_template('question2.html')

@app.route('/question2', methods=['POST'])
def question2():
    button__enter = request.form.get('button__enter')
    choise1 = request.form['choise1']
    if choise1 == '4':
        answer = 'Правильно!'
        return render_template('question2.html', answer=answer, button__enter=button__enter)
    else:
        answer = 'Не правильно!!'
        return render_template('question2.html', answer=answer, button__enter=button__enter)

@app.route('/question3')
def q2():
    return render_template('question3.html')

@app.route('/question3', methods=['POST'])
def question3():
    button___enter = request.form.get('button___enter')
    choise2 = request.form['choise2']
    if choise2 == '8':
        answer = 'Правильно!'
        return render_template('question3.html', answer=answer, button___enter=button___enter)
    else:
        answer = 'Не правильно!!'
        return render_template('question3.html', answer=answer, button___enter=button___enter)

@app.route('/result')
def res():
    return render_template('result.html')

@app.route('/result', methods=['POST'])
def result():
    results = request.form['results']
    return render_template('result.html', results=results)

app.run(debug=True)
