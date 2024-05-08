from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def hello_world():
    return "<h1>Hello World</h1>"


# # Вытаскиваем параметры через request.args (аргументы-параметры query string - параметры URL запроса)
# @app.route("/hello/")
# def hello_from_qs():
#     print("args", request.args)
#     name = request.args.get("name", "")
#     # foo = request.args.getlist("foo")
#     foo = request.args.get("foo", "")
#     # request.headers
#     return {"message": f"Hello {name}!", "foo": foo}
#
#
# # Вытаскиваем параметры через строчку
# @app.get("/hello/<name>/")
# def hello_name(name):
#     return {"message": f"Hello {name}!"}
# Если мы хотим сделать обе вышеупомянутые ф-ции в одной
@app.get("/hello/")
@app.get("/hello/<name>/")
def hello_name(name=None):
    if name is None:
        name = request.args.get("name", "")

    name = name.strip() or "World"
    # strip() удаляет лишние пробелы (ил др. символы) с начала и конца строки
    return {"message": f"Hello {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
