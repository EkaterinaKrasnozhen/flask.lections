from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request
from form_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Добро пожаловать на главную страницу!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
    # Обработка данных из формы
        pass
    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
        ...
    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)