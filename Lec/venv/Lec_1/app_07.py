from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/')# шаблон
def index():
    context = {
            'title': 'Личный блог',
            'name': 'Харитон',
            }
    return render_template('index.html', **context) # ** распаковывает словарь на ключ и значение


if __name__ == "__main__":
    app.run(debug=True)