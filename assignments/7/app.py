"""
Assignment 7: Webshop
"""

from flask import Flask, request, render_template, g, flash, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "admin"
app.config["DATABASE_DB"] = "test_storage"
app.config["DATABASE_HOST"] = "localhost"
app.secret_key = "any random string"

class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self, contents=dict()):
        """Initializes a shopping cart with content (if provided)."""
        self.__cart = contents

    def add(self, product_id, qt):
        """Adds a product to the shopping cart or increases its quantity if it's already there."""
        self.__cart[product_id] = self.__cart.get(product_id, 0) + qt

    def set(self, product_id, qt):
        """Sets a product quantity."""
        self.__cart[product_id] = qt

    def remove(self, product_id):
        """Removes a product from the shopping cart."""
        self.__cart.pop(product_id)

    def contains(self, product_id):
        """Checks if the cart contains a given product."""
        return product_id in self.__cart

    def contents(self):
        """Returns the contents of the cart as a dict."""
        return self.__cart


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
        sql = "SELECT id, name, description, normal_price, bonus_price, photo FROM product_info ORDER BY id;"
        cur.execute(sql)
        for i in cur:
            product_list.append({"id": i[0],
                                 "name": i[1],
                                 "description": i[2],
                                 "normal_price": i[3],
                                 "bonus_price": i[4],
                                 "img": i[5]})
        return render_template("index.html", product_list=product_list)
    except mysql.connector.Error as err:
        print(err)
        return render_template("layout.html", msg="erreor")
    finally:
        cur.close()

def get_product(product_id):
    """Loads a product from the database."""
    db = get_db()
    cur = db.cursor()

    try:
        product_data = {}
        sql = "SELECT id, name, description, normal_price, bonus_price, photo FROM product_info WHERE id={};".format(product_id)
        cur.execute(sql)
        for i in cur:
            product_data = {
                "product_id": product_id,
                "name": i[1],
                "description": i[2],
                "normal_price": i[3],
                "bonus_price": i[4],
                "img": i[5]
            }
        return product_data
    except mysql.connector.Error as err:
        print(err)
        return render_template("layout.html", msg="erreor")
    finally:
        cur.close()


@app.route("/product/<int:product_id>")
def product(product_id):
    """Product page"""
    return render_template("product.html", product=get_product(product_id))


@app.route("/cart")
def cart():
    """Shopping cart."""

    total = 0

    cart = ShoppingCart(session.get("cart", dict()))
    cartItems = []
    for product_id, qt in cart.contents().items():
        prod = get_product(product_id)
        prod["count"] = qt
        cartItems.append(prod)
        if prod["bonus_price"] == None:
            total += prod["normal_price"] * qt
        else:
            total += prod["bonus_price"] * qt
    return render_template("cart.html", cart=cartItems, total=total)


@app.route("/addtocart", methods=["POST"])
def add_to_cart():
    """Add a given product to cart."""
    product_id = request.form["product_id"]
    qt = int(request.form["qt"])

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.add(product_id, qt)
        session["cart"] = cart.contents()
        msg = "{} piece(s) of product #{} have been added to the cart".format(request.form["qt"], product_id)
    else:
        msg = "error"

    return render_template("product.html", product=get_product(product_id), msg=msg)


@app.route("/set", methods=["POST"])
def set():
    product_id = request.form["product_id"]
    qt = int(request.form["qt"])

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.set(product_id, qt)
        session["cart"] = cart.contents()
        flash("Quantity modified")
    else:
        print(400)

    return redirect(url_for("cart"))


@app.route("/remove", methods=["GET"])
def remove():
    product_id = request.args.get("product_id")

    if product_id:
        cart = ShoppingCart(session.get("cart", dict()))
        if cart.contains(product_id):
            cart.remove(product_id)
            session["cart"] = cart.contents()
            flash("Product removed cart")
        else:  # trying to remove a product which is not in the cart
            print(400)
    else:
        print(400)
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["POST", "GET"])
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
        total = 0

        cart = ShoppingCart(session.get("cart", dict()))
        cartItems = []
        for product_id, qt in cart.contents().items():
            prod = get_product(product_id)
            prod["count"] = qt
            cartItems.append(prod)
            if prod["bonus_price"] == None:
                total += prod["normal_price"] * qt
            else:
                total += prod["bonus_price"] * qt

        return render_template("checkout_0.html", cart=cartItems, total=total)


if __name__ == "__main__":
    app.run()
