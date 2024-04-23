## SQLAlchemy связи между таблицами в БД

**_Пример связи posts.user_id с users.id_**
```postgresql
class Post(Base)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),  # путь до колонки в табличке users(User)
        unique=False,  # у одного юзера может быть много постов
        nullable=False,  # чтобы не было поста без user
    )
```

В другом модуле мы обязаны проинициализировать все модули с табличками перед использованием команды  
`Base.metadata.create_all(engine)`, то есть сначала инициализируем все модули, потом создаем

❗️ Делаем инициализацию в `__init__.py` , так как он инициализируется первее, чем модуль `models`  

**_Пример отношения между классами для связи таблиц (JOIN в SQL)_**
```postgresql
    # Код в классе Post, который будет связан с классом User таблицы users
    author = relationship(
        # to class name
        "User",
        # how to access to this model[s]: user.'posts'
        back_populates="posts",
        # author can be only one due to single 'user_id'
        uselist=False,  # 1 пост = 1 пользователь, каждый пост может быть создан только 1 пользователем
    )
```

**_Необходимо также сделать обратную связь в классе, с которым связываем_**
```postgresql
    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.'author'
        back_populates="author",
        # user can have any number of posts
        uselist=True,
    )
```
❗️ Этот код не вносит никаких изменений в таблице, поскольку этот код только для алхимии, не SQL

**_Для вывода связанных таблиц используем options(joinedload(Class.table))_**
```postgresql
def fetch_users_with_posts(
    session: Session,
) -> list[User]:
    stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    users = session.scalars(stmt)
    return users.unique().all()
```

**_В обратную сторону_**
```postgresql
def fetch_post_with_authors(
    session: Session,
) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.author)).order_by(Post.id)
    posts = session.scalars(stmt)
    return posts.all()
```

`options(joinedload(Post.author)`
Способ предварительной загрузки данных в SQLAlchemy из БД, чтобы избежать проблемы N+1 запросов, когда каждый объект связи загружается отдельным запросом.
Данный способ гарантирует, что все связанные сущности (в данном случае, посты пользователя) будут загружены в рамках одного запроса, 
что уменьшает количество запросов к базе данных и повышает производительность.

❗️ Для большей гибкости и работой с большими БД, лучше использовать
`selectinload()` вместо `joinedload()`


