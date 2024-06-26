DB_ENGINE = "asyncpg"
DB_USER = "user"
DB_PASSWORD = "example"
DB_NAME = "blog"
DB_HOST = "localhost"
DB_PORT = 5432

# DB_URL = f"postgresql+psycopg://user:example@localhost:5432/blog"
DB_URL = (
    f"postgresql+{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# DB_ECHO = False
DB_ECHO = True  # для отладки (чтобы показать сам SQL запрос, который генерируется)
