import asyncio

from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy import func
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.orm import Session, joinedload, selectinload

from models.user import User
from models.base import Base
from models.post import Post
from models.tag import Tag
from models.db import async_session


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
    refresh_after_commit: bool = False,
) -> User:
    user = User(username=username, email=email)
    session.add(user)
    await session.commit()
    if refresh_after_commit:
        await session.refresh(user)
    print("created_user:", user)
    return user


async def create_post(
    session: AsyncSession,
    title: str,
    user_id: int,
) -> Post:
    post = Post(title="", user_id=user_id)
    session.add(post)
    await session.commit()
    print("created_post:", post)
    return post


async def create_several_users(
    session: AsyncSession,
    *usernames: str,
) -> list[User]:
    users = [User(username=username) for username in usernames]
    session.add_all(users)
    print()
    print("prepared users:", users)
    print()
    await session.commit()
    print()
    print("created users:", users)
    return users


async def create_several_posts(
    session: AsyncSession,
    *titles: str,
    user_id: int,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in titles]
    session.add_all(posts)
    await session.commit()
    return posts


async def fetch_all_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    res = await session.scalars(stmt)
    users = res.all()
    users_list = list(users)
    for user in users_list:
        print(user)
    return users_list


def fetch_user_by_id(session: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user


def fetch_user_by_username(session: Session, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)
    print()
    print("User:", user)
    print()
    return user


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


def fetch_all_posts(session: Session) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    posts = session.scalars(stmt)
    return posts.all()


def fetch_user_for_domain(session: Session, domain: str) -> list[User]:
    stmt = select(User).where(User.email.ilike(f"%{domain.lower()}"))
    users = session.scalars(stmt).all()
    print(f"Users for domain {domain}:", users)
    return users


def fetch_post_for_user_id(session: Session, user_id: int) -> list[Post]:
    stmt = select(Post).where(Post.user_id == user_id).order_by(Post.id)
    posts = session.scalars(stmt).all()
    return posts


def fetch_users_with_posts(
    session: Session,
) -> list[User]:
    stmt = select(User).options(joinedload(User.posts)).order_by(User.id)
    users = session.scalars(stmt)
    return users.unique().all()


def fetch_post_with_authors(
    session: Session,
) -> list[Post]:
    stmt = select(Post).options(joinedload(Post.author)).order_by(Post.id)
    posts = session.scalars(stmt)
    return posts.all()


def create_tags(
    session=Session,
    *tags_names: str,
) -> list[Tag]:
    tags = [Tag(name=tag_name) for tag_name in tags_names]
    session.add_all(tags)
    session.commit()
    print(tags)
    return tags


def create_tags_for_posts_names(
    session: Session,
) -> list[Tag]:
    posts = fetch_all_posts(session)
    tags_name = []
    for post in posts:
        parts = post.title.lower().split()
        tags_name.extend(parts)

    tags = [Tag(name=name) for name in set(tags_name)]
    session.add_all(tags)
    session.commit()
    print(tags)
    return tags


def fetch_all_tags_with_posts(session: Session) -> list[Tag]:
    stmt = select(Tag).options(selectinload(Tag.posts)).order_by(Tag.id)
    tags = session.scalars(stmt)
    return tags.all()


def fetch_all_posts_with_tags(session: Session) -> list[Tag]:
    stmt = select(Post).options(selectinload(Post.tags)).order_by(Post.id)
    posts = session.scalars(stmt)
    return posts.all()


def auto_associate_tags_with_posts(session: Session):
    tags = fetch_all_tags_with_posts(session)
    posts = fetch_all_posts_with_tags(session)
    for post in posts:
        for tag in tags:
            if tag in post.tags:
                continue
            if tag.name.lower() in post.title.lower():
                post.tags.append(tag)

    session.commit()


# получить пользователей с постами по тегам
def get_users_with_posts_with_tags(
    session: Session,
    tag_name: str,
) -> list[User]:
    stmt = (
        select(User)
        .join(User.posts)
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
        .order_by(User.id)
    )
    result = session.scalars(stmt)
    users = result.unique().all()
    print("users who used tag:", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


# subquery() создает подзапрос для получения user_id, которые публиковали посты с определенным тегом
# затем эти идентификаторы используются в основном запросе для извлечения соответствующих пользователей
def get_users_with_posts_with_tag_using_subquery(
    session: Session,
    tag_name: str,
) -> list[User]:

    stmt_user_id_from_posts_with_tag = (
        select(Post.user_id)
        .join(Post.tags)
        .where(
            func.lower(Tag.name) == tag_name.lower(),
        )
    )

    stmt = (
        select(User)
        .where(
            User.id.in_(
                stmt_user_id_from_posts_with_tag.subquery(),
            ),
        )
        .order_by(User.id)
    )

    result = session.scalars(stmt)
    users = result.unique().all()
    print("users who used tag:", repr(tag_name), "in posts:")
    for user in users:
        print(user)

    return users


async def demo(session: AsyncSession):
    user_john: User = await create_user(
        session, username="John", refresh_after_commit=True
    )
    user_sam: User = await create_user(session, username="Sam")
    user_nick: User = await create_user(session, username="Nick")

    # await fetch_all_users(session)
    #
    await create_post(session, title="Intro Lesson", user_id=user_john.id)
    await create_several_posts(
        session,
        "SQL Introduction",
        "SQL Transactions",
        user_id=user_john.id,
    )
    #
    # user_bob = create_user(session, username="bob")
    # user_alice = create_user(session, username="alice")
    # create_several_posts(
    #     session,
    #     "Transactions in MySQL",
    #     "MySQL Lesson",
    #     "Postgresql Lesson",
    #     user_id=user_bob.id,
    # )
    # ---------------------------------------------
    # for user_id in (0, 1, 2, 3):
    #     posts = fetch_post_for_user_id(session, user_id)
    #     if not posts:
    #         print("-- no posts for user:", user_id)
    #         continue
    #     print(f"++ user id = {user_id}, posts {len(posts)}:")
    #     for post in posts:
    #         print("-", post)
    # ---------------------------------------------
    # users_with_posts = fetch_users_with_posts(session)
    # for user in users_with_posts:
    #     print("++ posts for user", user)
    #     for post in user.posts:
    #         print("-", post)
    # ---------------------------------------------
    # post_with_authors = fetch_post_with_authors(session)
    # for post in post_with_authors:
    #     print("post", (post.id, post.title), "author", post.author)
    #
    # create_tags(
    #     session,
    #     "news",
    #     "python",
    # )
    #
    # create_tags_for_posts_names(session)
    # auto_associate_tags_with_posts(session)
    # posts_with_tags = fetch_all_posts_with_tags(session)
    # for post in posts_with_tags:
    #     print("Post:", post)
    #     for tag in post.tags:
    #         print("-t", tag)
    #
    # tags_with_posts = fetch_all_tags_with_posts(session)
    # for tag in tags_with_posts:
    #     print("Tags", tag)
    #     for post in tag.posts:
    #         print("-", post.id, post.title)
    #
    # get_users_with_posts_with_tags(session, "sql")
    # get_users_with_posts_with_tags(session, "news")
    # get_users_with_posts_with_tags(session, "mysql")
    #
    # get_users_with_posts_with_tag_using_subquery(session, "sql")
    # get_users_with_posts_with_tag_using_subquery(session, "news")
    # get_users_with_posts_with_tag_using_subquery(session, "mysql")


async def async_main():
    async with async_session() as session:
        await demo(session)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
