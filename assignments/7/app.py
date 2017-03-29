"""
Assignment 7: Webshop
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Index page that shows a list of products"""
    # TODO: fetch all products from database
    return render_template("index.html")


def get_product(product_id):
    """Loads a product from the database."""
    # TODO: look up product from database
    product_data = {
        "product_id": product_id
    }
    return product_data


@app.route("/product/<int:product_id>")
def product(product_id):
    """Product page"""
    return render_template("product.html", product=get_product(product_id))


@app.route("/cart")
def cart():
    """Shopping cart."""
    # TODO: fetch the contents of the cart from session
    return render_template("cart.html")


@app.route("/addtocart", methods=["POST"])
def add_to_cart():
    """Add a given product to cart."""
    product_id = request.form["product_id"]
    # TODO: add product to cart
    msg = "{} piece(s) of product #{} have been added to the cart".format(request.form["qt"], product_id)
    return render_template("product.html", product=get_product(product_id), msg=msg)


@app.route("/checkout", methods=["POST"])
def checkout():
    """Checkout process"""
    action = request.form.get("action")
    if action == "do_1":
        # TODO: check order details, if all correct show confirmation form,
        # otherwise show order form again (with filled-in values remembered)
        return render_template("checkout_1.html")
    elif action == "do_2":
        if request.form.get("confirm") == "1":  # check if order is confirmed
            # TODO: save order in database and return order number
            return render_template("checkout_2.html", order_number="XXX")
        else:
            return render_template("checkout_1.html", err="You need to confirm the order.")
    else:
        # TODO: display form for order details
        return render_template("checkout_0.html")


if __name__ == "__main__":
    app.run()