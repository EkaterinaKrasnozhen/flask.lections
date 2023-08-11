from app_01 import app
# этот файл ищет flask чтобы запустить без длиннлшл указания пути

if __name__ == "__main__":
    app.run(debug=True)
    
# flask run
# run --debug # режим отладки
