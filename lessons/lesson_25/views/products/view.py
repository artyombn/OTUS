from flask import Blueprint
from flask import render_template

from crud import products_storage as storage

products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.route("/")
def get_products():
    products = storage.get()
    return render_template(products)
