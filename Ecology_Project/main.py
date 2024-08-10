#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

#Вторая страница
@app.route('/test')
def test():
    return render_template('test.html')

#Третья страница
@app.route('/test', methods=['POST'])
def process_form():
    button_enter = request.form.get('button_enter')
    choise = request.form['choise']
    if choise == '3':
        answer = 'Правильно!'
        return render_template('test.html', answer=answer, button_enter=button_enter)
    else:
        answer = 'Не правильно!!'
        return render_template('test.html', answer=answer, button_enter=button_enter)


app.run(debug=True)
