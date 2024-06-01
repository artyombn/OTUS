from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    session,
)

from werkzeug.exceptions import (
    NotFound,
    BadRequest,
)

from lessons.lesson_28.models.product import Product
from lessons.lesson_28.views.products.crud import products_storage as storage


products_app = Blueprint(
    "products_app",
    __name__,
    url_prefix="/products",
)


@products_app.get("/", endpoint="list")
def get_products():
    products = storage.get()
    return render_template(
        "products/list.html",
        products=products,
    )


@products_app.route("/add/", endpoint="add", methods=["GET", "POST"])
def add_product():
    if request.method == "GET":
        return render_template("products/add.html")

    product_name = request.form.get("product-name", "")
    product_name = product_name.strip()
    if not product_name:
        raise BadRequest("Product name is required")
    product: Product = storage.create(name=product_name)
    flash(f"{product_name}")
    session["last_product_name"] = product_name  # Save the product name in session
    url = url_for("products_app.details", product_id=product.id)
    return redirect(url)


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    product: Product = storage.get_or_404(
        product_id=product_id,
        description=f"Product with id #{product_id} is not found",
    )

    return render_template(
        "products/details.html",
        product=product,
    )


@products_app.route(
    "/<int:product_id>/confirm-delete/",
    endpoint="confirm_delete",
    methods=["GET", "POST"],
)
def confirm_delete_product(product_id: int):
    product: Product = storage.get_or_404(
        product_id=product_id,
    )
    if request.method == "GET":
        return render_template("products/confirm-delete.html", product=product)

    product_name = product.name
    storage.delete(product)
    flash(f"Product {product_name} deleted")
    return redirect(url_for("products_app.list"))
