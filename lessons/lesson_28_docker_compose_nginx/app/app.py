import os
from flask import (
    Flask,
    request,
    render_template,
)
from flask_migrate import Migrate

from models.database import db
from views.items import items_app
from views.products.views import products_app

print("Создание приложения Flask")
app = Flask(__name__)

app.config.update(
    SECRET_KEY="616b2180ee260174500b1042c64",  # для Flask message flash
    SQLALCHEMY_DATABASE_URI=os.getenv(
        "SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://user:example@pg:5432/blog"
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
)

print("Инициализация базы данных")
db.init_app(app)

print("Настройка миграций")
migrate = Migrate(app, db)

print("Регистрация блюпринтов")
app.register_blueprint(items_app)
app.register_blueprint(products_app)

with app.app_context():
    # db.create_all()
    migrate.init_app(app, db)


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
    app.run(host="0.0.0.0", port=5000)
