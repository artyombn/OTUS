from flask import (
    Flask,
    request,
    render_template,
)
from flask_migrate import Migrate

from lessons.lesson_28.models.database import db
from lessons.lesson_28.views.items import items_app
from lessons.lesson_28.views.products.views import products_app

print("Создание приложения Flask")
app = Flask(__name__)
app.config.update(
    SECRET_KEY="616b2180ee260174500b1042c64",  # для Flask message flesh
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg://user:example@localhost:5432/blog",
    SQLALCHEMY_ECHO=True,
)

print("Регистрация блюпринтов")
app.register_blueprint(items_app)
app.register_blueprint(products_app)

print("Инициализация базы данных")
db.init_app(app)

print("Настройка миграций")
migrate = Migrate(app, db)

# with app.app_context():
#     # db.create_all()
#     migrate.init_app(app, db)


@app.get("/", endpoint="index")
def hello_world():
    return render_template("index.html")


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
