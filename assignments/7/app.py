"""
Assignment 7: Webshop
"""

from flask import Flask, request, render_template, g, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "admin"
app.config["DATABASE_DB"] = "test_storage"
app.config["DATABASE_HOST"] = "localhost"

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
        return g._database

@app.route("/")
def index():
    """Index page that shows a list of products"""

    db = get_db()
    cur = db.cursor()

    try:
        product_list = []
        sql = "SELECT id, name, description, base_price, bonus_price, photo FROM product_info ORDER BY id;"
        cur.execute(sql)
        for i in cur:
            print(i)
        return render_template("index.html")
    except mysql.connector.Error as err:
        print(err)
        return render_template("layout.html", msg="erreor")
    finally:
        cur.close()

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