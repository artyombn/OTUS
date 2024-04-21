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


