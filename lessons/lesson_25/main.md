# Знакомство с веб разработкой на Flask

_https://flask.palletsprojects.com/en/3.0.x/_

Многие вещи Flask делает через Werkzeug
_https://werkzeug.palletsprojects.com/en/3.0.x/_

Werkzeug - обертка для WSGI для приема и отправки web-запросов (Python интерфейс для веб-приложений)

В продакшине приложения запускать через Gunicorn или uWSGI! 

Контекстные переменные в Python позволяют по контексту получит значения
Во Flask каждый запрос это контекст

HTML "наследование данных"
`{% extends 'base.html'%}`  
В файл с данной командой вставляется весь код из файла base.html

_Для отрисовывания шаблона (рендеринг index.html)_
```python
from flask import render_template

@app.get("/")
def hello_world():
    return render_template("index.html")
```

В Jinja используются блоки для организации шаблонов и наследования макетов.  
Блоки это секция, которая будет заменена на то, что мы укажем в блоке
Синтаксис:
```python
{% block block_name %}
    Содержимое блока
{% endblock %}
```

**_Blueprint_** - чертеж приложений для организации множества маршрутов (routers) и представлений (views)  
_(почти как роутеры в FastApi)_

```python
from flask import Blueprint

items_app = Blueprint(
    "items_app",
    __name__,
    url_prefix="/items",
)
```
*Импортируем items_app в основной модуль приложения, а затем:
```python
app.register_blueprint(items_app)
```