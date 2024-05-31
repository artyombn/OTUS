"""
CRUD functions for products

Create
Read
Update
Delete
"""

from random import randint

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

from app.models import (
    Product,
    db as main_sqla_db,
)


class ProductsStorage:
    def __init__(self, db: SQLAlchemy) -> None:
        self.db = db

    def create(self, name: str, price: int | None = None) -> Product:
        product = Product(
            name=name,
            price=price or randint(10, 1000),
        )
        self.db.session.add(product)
        self.db.session.commit()
        return product

    def get(self) -> list[Product]:
        return Product.query.order_by(Product.id).all()

    def get_by_id(self, product_id: int) -> Product | None:
        # return self.db.session.get(Product, product_id)
        return Product.query.get(product_id)

    def get_or_404(self, product_id: int, description: str | None = None) -> Product:
        if description is None:
            description = f"Product with id #{product_id} not found!"

        return Product.query.get_or_404(
            ident=product_id,
            description=description,
        )

    def delete(self, product: Product) -> None:
        self.db.session.delete(product)
        self.db.session.commit()
        return "Product deleted"


products_storage = ProductsStorage(db=main_sqla_db)
