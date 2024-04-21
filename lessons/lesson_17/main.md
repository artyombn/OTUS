# SQLAlchemy ORM
https://www.sqlalchemy.org

`pip install sqlalchemy`

## Psycopg3
Библиотека для работы с БД PostgreSQL  
`pip install "psycopg[binary,pool]"`  

## Postgres
**_Use Postgres docker compose_**  
_https://hub.docker.com/_/postgres_  
**_docker-compose.yml_**

### Подключение
_https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql_  
_Config:_  
`DB_URL = (f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")`  

### Для ORM
`from sqlalchemy.orm import DeclarativeBase`  

**_Используем декларативный стиль SQL для создания таблиц  
Наследуемся от Декларативного Базового класса_**

```postgresql
class Base(DeclarativeBase):
    pass
```

`Base.metadata.drop_all(engine)` - дропнуть табличку  
`Base.metadata.create_all(engine)` - создать табличку  

### Session

`from sqlalchemy.orm import Session`  
_Session в SQLAlchemy - это класс, предоставляющий средства для управления сеансами (сессиями) взаимодействия с базой данных. 
Эта сессия будет использоваться для выполнения запросов к базе данных, добавления, изменения и удаления объектов._  

```postgresql
    with Session(engine) as session:
        result = session.execute(select(1))
        print(result)
```

**_Пример создания значений в таблице Users:_**
```postgresql
def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    return user
```
_Для отслеживания изменений значения. Изменения автоматически попадут в БД_  
`    session.add(user)`  
_Для добавления изменений в таблицу_  
`    session.commit()`  

**_Пример запроса всех полей таблицы:_**
```postgresql
def fetch_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list  
```
**_Пример запроса одного пользователя по user_id:_**
```postgresql
def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    user = session.scalar(stmt)
    print("User:", user)
    return user
```

**_Обновление данных таблицы (на примере email)_**
```postgresql
def update_users_emails(
    session: Session,
    username_len: int,
    email_domain: str,
):
    stmt = (
        update(User)
        .where(
            User.email.is_(None),
            func.length(User.username) > username_len,
        )
        .values(
            {
                User.email: func.concat(
                    func.lower(User.username), email_domain.lower()
                ),
                # User.username: 'Qwery',
            }
        )
    )

    result = session.execute(stmt)
    session.commit()
```
