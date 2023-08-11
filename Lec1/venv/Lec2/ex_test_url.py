from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=42) = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=42, data="new_data", pi=3.14515) = }<br>'
    return text


@app.route('/about/')
def about():
    context = {
    'title': 'Обо мне',
    'name': 'Ярослав',
    }
    return render_template('about.html', **context)


@app.route('/get/')
def get():
    if level := request.args.get('level'):
        text = f'Похоже ты опытный игрок, раз имеешь уровень {level}<br>'
    else:
        text = 'Привет, новичок.<br>'
    return text + f'{request.args}'
# get/?name=alex&age=13&level=80 
# ответ ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level', '80')])


if __name__ == "__main__":
    app.run(debug=True)