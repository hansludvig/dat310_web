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

class Checkout:
    """Class representing a shopping cart."""

    def __init__(self, contents=dict()):
        """Initializes a shopping cart with content (if provided)."""
        self.__cart = contents

    def set(self, order_nr, pdata):  # pdata -> personel data
        """Sets a product quantity."""
        self.__cart[order_nr] = pdata

    def remove(self, order_nr):
        """Removes a product from the shopping cart."""
        self.__cart.pop(order_nr)

    def contains(self, order_nr):
        """Checks if the cart contains a given product."""
        return order_nr in self.__cart

    def contents(self):
        """Returns the contents of the cart as a dict."""
        return self.__cart

class OrderNr:

    def __init__(self):
        self.__order_nr = self.order_nr_init()

    def get_db(self):
        if not hasattr(g, "_database"):
            g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                                  password=app.config["DATABASE_PASSWORD"],
                                                  database=app.config["DATABASE_DB"])
        return g._database

    def order_nr_init(self):

        db = get_db()
        db.ping(True)
        cur = db.cursor(buffered=True)

        try:
            sql = "SELECT order_id FROM order_head ORDER BY order_id DESC LIMIT 1"
            cur.execute(sql)
            for e in cur:
                order_id = e[0] + 1

            return order_id
        except mysql.connector.Error as err:
            return 101 #no entries
        finally:
            cur.close()
            db.close()

    def get(self):
        return self.__order_nr

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database

@app.route("/")
def index():
    """Index page that shows a list of products"""

    db = get_db()
    db.ping(True)
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
        db.close()

def get_product(product_id):
    """Loads a product from the database."""
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        product_data = {}
        sql = "SELECT * FROM product_info WHERE id={};".format(product_id)
        cur.execute(sql)
        for i in cur:
            id, name, desc, normal_prcie, bonus_price, photo = i
            product_data = {
                "product_id": id,
                "name": name,
                "description": desc,
                "normal_price": normal_prcie,
                "bonus_price": bonus_price,
                "img": photo
            }
        return product_data
    except mysql.connector.Error as err:
        print(err)
        return render_template("layout.html", err=err)
    finally:
        cur.close()
        db.close()


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
        #print(type(product_id))
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
        flash("Quantity modified", "set")
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
            flash("Product removed from cart", "remove")
        else:  # trying to remove a product which is not in the cart
            print(400)
    else:
        print(400)
    return redirect(url_for("cart"))


@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    """Checkout process"""
    order_nr = OrderNr().get()
    action = request.form.get("action")

    if action == "do_1":
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        s_address = request.form.get("saddress")
        postcode = request.form.get("postcode")
        city = request.form.get("city")

        pdata = {
            "fname": fname,
            "lname": lname,
            "email": email,
            "phone": phone,
            "s_address": s_address,
            "postcode": postcode,
            "city": city
        }
        #print(pdata)

        out = Checkout()
        out.set(str(order_nr), pdata)
        session["checkout"] = out.contents()
        ch_session = session.get("checkout")

        #print(out.contents())

        if fname and lname and email and phone and s_address and postcode and city:
            if len(str(phone)) == 8:
                #print(len(phone))
                if len(str(postcode)) == 4:
                    #print(len(postcode))
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
                    return render_template("checkout_1.html", cart=cartItems, total=total)
                else:
                    msg = "Wrong postcode format"
                    pdata["postcode"] = ""

                    return render_template("checkout_0.html", pdata=ch_session[str(order_nr)], war=msg)
            else:
                msg = "Wrong phone format"
                pdata["phone"] = ""

                return render_template("checkout_0.html", pdata=ch_session[str(order_nr)], war=msg)
        else:
            msg = "Fill out the missing field(s)"
            print(msg)
            return render_template("checkout_0.html", pdata=ch_session[str(order_nr)], war=msg)
        # TODO: check order details, if all correct show confirmation form,
        # otherwise show order form again (with filled-in values remembered)
    elif action == "do_2":
        if request.form.get("confirm") == "1":  # check if order is confirmed
            # TODO: save order in database and return order number
            ch = Checkout(session.get("checkout", dict()))
            pr = ShoppingCart(session.get("cart", dict()))
            # print(pr.contents())
            if ch.contains(str(order_nr)):

                tmp = []
                for nr, data in ch.contents().items():
                    tmp.append(nr)
                    for d, v in data.items():
                        tmp.append(v)
                # print(tmp)
                sql = "INSERT INTO order_head (order_id, fname, lname, email, phone, " \
                      "street, postcode, city, order_date) VALUES (" + tmp[0] + ", '" + tmp[3] + "', '" + tmp[4] + "', '" + \
                      tmp[2] + "', " + tmp[5] + ", '" + tmp[7] + "', " + tmp[6] + ", '" + tmp[1] + "', current_timestamp());"
                query1 = insert_query(sql)
                if query1 is True:
                    for k, v in pr.contents().items():
                        sql = "INSERT INTO order_items (order_id, product_id, qt) VALUES ({}, {}, {});".format(order_nr, k, v)
                        query_product = insert_query(sql)
                        if query_product is True:
                            continue
                        else:
                            flash("Unable to save your order. This order wil now be deleted. Please try again", "remove")
                            delete_order(order_nr)
                            return redirect(url_for("index"))
                    session.pop("cart", None)
                    session.pop("checkout", None)
                    return render_template("checkout_2.html", order_number=order_nr)
                else:
                    return render_template("layout.html", err=query1)
            else:
                session.pop("cart", None)
                session.pop("checkout", None)
                flash("Something went wrong! Please try again.", "remove")
                return redirect(url_for("index"))
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
            return render_template("checkout_1.html", cart=cartItems, total=total, err="You need to confirm the order.")
    else:
        tmp = session.get("checkout", dict())
        if order_nr in tmp:
            return render_template("checkout_0.html", pdata=tmp[str(order_nr)])
        else:
            return render_template("checkout_0.html")

def insert_query(sql):
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        cur.execute(sql)
        db.commit()
        return True
    except mysql.connector.Error as err:
        return err
    finally:
        cur.close()
        db.close()

def delete_order(order_id):
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        sql = "SET SQL_SAFE_UPDATES = 0; delete head, items from order_head head join order_items items on " \
              "head.order_id = items.order_id where head.order_id = {};SET SQL_SAFE_UPDATES = 1;".format(order_id)
        cur.execute(sql, multi=True)
        db.commit()
        flash("Order id: " + str(order_id) + " deleted from database")
    except mysql.connector.Error as err:
        flash(err)
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    app.run()
