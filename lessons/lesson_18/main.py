from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func
from sqlalchemy import text

from sqlalchemy.orm import Session

from lessons.lesson_18.models.user import User
from lessons.lesson_18.models.base import Base
from lessons.lesson_18.models.post import Post


from lessons.lesson_18.models.db import engine


# def main():
#     print(
#         Base.metadata.tables
#     )  # если не проинициализировали в __init__, то Metadata будет пустая
#     Base.metadata.create_all(
#         bind=engine
#     )  # к этому моменту должны быть проинициализированы все классы


# СКОПИРОВАНО ИЗ LESSON 17
def create_tables():
    Base.metadata.create_all(engine)


# Добавление пользователей в таблицу:
def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    print("created_user:", user)
    return user


def create_post(
    session: Session,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title="", user_id=user_id)
    session.add(post)
    session.commit()
    print("created_post:", post)
    return post


def create_several_users(
    session: Session,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    print()
    print("prepared users:", users)
    print()
    session.commit()
    print()
    print("created users:", users)
    return users


def create_several_posts(
    session: Session,
    *titles: str,
    user_id: int,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in titles]
    session.add_all(posts)
    session.commit()
    return posts


# Запрос вывода всех полей таблицы Users
def fetch_all_users(session: Session) -> list[User]:
    stmt = select(User).order_by(User.id)
    users = session.scalars(stmt).all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


# Запрос вывода пользователя по id
def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user


# Запрос вывода пользователя по username
def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user


# Обновление email пользователей
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


def fetch_user_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(User.email.ilike(f"%{domain.lower()}"))
    users = session.scalars(stmt).all()
    print(f"Users for domain {domain}:", users)
    return users


def fetch_post_for_user_id(session: Session, user_id: int) -> list[Post]:
    stmt = select(Post).where(Post.user_id == user_id).order_by(Post.id)
    posts = session.scalars(stmt).all()
    return posts


def demo(session: Session):
    # user_john = create_user(session, username="John")
    # user_sam = create_user(session, username="Sam")
    #
    # create_post(session, title="Intro Lesson", user_id=user_john.id)
    # create_several_posts(
    #     session,
    #     "SQL Introduction",
    #     "MySQL Lesson",
    #     "Postgres Lesson",
    #     user_id=user_sam.id,
    # )
    for user_id in (0, 1, 2, 3):
        posts = fetch_post_for_user_id(session, user_id)
        if not posts:
            print("-- no posts for user:", user_id)
            continue
        print(f"++ user id = {user_id}, posts {len(posts)}:")
        for post in posts:
            print("-", post)


def main():
    create_tables()

    with Session(engine) as session:
        demo(session)


if __name__ == "__main__":
    main()
