from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

#python
#>>> import secrets
#>>> secrets.token_hex()
app.secret_key = b'51f3b67ee0b8d9a37ca35fa5f2e204496512e4faac71570133c438c391b51e90'


# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#     # Обработка данных формы
#         flash('Форма успешно отправлена!', 'success')
#         return redirect(url_for('form'))
#     return render_template('form_flash.html')


@app.route('/form2', methods=['GET', 'POST']) # выдает разные типы сообщений в зависимости от успеха
def form2():
    if request.method == 'POST':
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form2'))
            # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
    return render_template('form_flash.html')


if __name__ == "__main__":
    app.run(debug=True)