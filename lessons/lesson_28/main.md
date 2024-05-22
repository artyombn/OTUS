# Flask-SQLAlchemy, Flask-Migrate

_https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/_

database.py (Initialize the Extension)
```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
```

Configure: 
```python
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg://user:example@localhost:5432/blog"
)

db.init_app(app)
```

Create tables:
```python
with app.app_context():
    db.create_all()
```

Исползовать alembic с алхимией
_https://flask-migrate.readthedocs.io/en/latest/_

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

`flask db init`   
`flask db migrate -m "create products table"` - сделать миграцию  
`flask db upgrade` - применить миграцию  
