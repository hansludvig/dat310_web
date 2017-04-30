"""
    Assignment 9
    @author: Hans Ludvig Kleivdal
"""
import os
from flask import Flask, request, render_template, g, flash, redirect, url_for, session, send_from_directory
import mysql.connector
#from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import json

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = ["txt", "pdf", "png", "jpg", "jpeg", "gif"]

app = Flask(__name__)
app.debug = True

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "admin"
app.config["DATABASE_DB"] = "test_storage"
app.config["DATABASE_HOST"] = "localhost"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "any random string"


class Database:

    def __init__(self, db):
        self.products = []
        self._load_products(db)

    def _load_products(self, db):

        db.ping(True)
        cur = db.cursor()

        try:
            sql = "select * from product_info;"
            cur.execute(sql)
            for i in cur:
                id, name, description, normal_price, bonus_price, photo = i
                self.products.append({
                    "id": id,
                    "name": name,
                    "description": description,
                    "normal_price": float(normal_price) if float(normal_price).is_integer() else None,
                    "bonus_price": float(bonus_price) if bonus_price else None,
                    "photo": photo
                })
            print(self.products)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cur.close()
            db.close()

    def get_products(self):
        return self.products

    def get_product(self, id):
        for i in self.products:
            if int(id) == i['id']:
                return i
        return None
"""
    def get_db(self):
        if not hasattr(g, "_database"):
            g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"],
                                                  user=app.config["DATABASE_USER"],
                                                  password=app.config["DATABASE_PASSWORD"],
                                                  database=app.config["DATABASE_DB"])
        return g._database"""


def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

with app.app_context():
    app.config["PRODUCTS"] = Database(get_db())


@app.route("/products")
def products():

    db = app.config["PRODUCTS"]
    print(db.get_products())

    return render_template("products.html", products=db.get_products())


@app.route("/edit/<id>")
def edit(id):
    products = app.config["PRODUCTS"]
    if id:
        return render_template("edit.html", product=products.get_product(id))
    else:
        flash("Product to not exist")


@app.route("/submit", methods=['POST'])
def submit():
    db = app.config["PRODUCTS"]
    id = request.form.get("id")
    name = request.form.get("name")
    desc = request.form.get("description")
    price = request.form.get("normal_price")
    bonus_price = request.form.get("bonus_price")
    curent_product = db.get_product(id)
    file = request.files["file"]
    new_photo = False

    if file.filename == "":
        file = curent_product["photo"]
        new_photo = False
    else:
        new_photo = True

    print(new_photo)
    print(file)
    if bonus_price == "":
        bonus_price = None
    else:
        bonus_price = float(bonus_price)

    product = db.get_product(id)

    if int(id) == product['id'] and name == product['name'] and desc == product['description'] and float(price) == product['normal_price'] and bonus_price == product['bonus_price'] and file == product["photo"]: # feil HERRRR!!!!!!!!
        flash("Noting to update!", "remove")
        print("NO UPDATE")

        return redirect(url_for('products'))
    else:
        if bonus_price == None:
            bonus_price = "NULL"
        if new_photo:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                photo = "../"+path
                sub = db_update_product(id, name, desc, price, bonus_price, photo)
                if sub is True:
                    file.save(path)
                    flash("Product #" + id + " updated!", "set")
                    return redirect(url_for('products'))
                else:
                    return redirect(url_for('products'))
        else:
            sub = db_update_product(id, name, desc, price, bonus_price, file)
            if sub is True:
                flash("Product #" + id + " updated!", "set")
                return redirect(url_for('products'))
            else:
                return redirect(url_for('products'))


@app.route("/add")
def add():
    return render_template("add.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/add_product", methods=['POST'])
def add_product():
    name = request.form.get("name")
    desc = request.form.get("description")
    price = request.form.get("normal_price")
    bonus_price = request.form.get("bonus_price")
    file = request.files["file"]
    print(file)
    print(file.filename)

    db = app.config["PRODUCTS"]

    if file and allowed_file(file.filename):
        # "secure" the filename (form input may be forged and filenames can be dangerous)
        filename = secure_filename(file.filename)
        # save the file to the upload folder
        path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        print(path)
        if bonus_price == "":
            bonus_price = "NULL"
        print("bonus: " + bonus_price)
        db_add = db_add_product(name, desc, price, bonus_price, path)
        if db_add:
            file.save(path)
            flash("File uploaded", "set")
            return redirect(url_for("products"))
        else:
            return redirect(url_for("products"))
    else:
        flash("Not allowed file type", "set")
        return redirect(url_for("products"))


@app.route("/delete/<id>")
def delete(id):
    db_del = db_delete_product(id)
    if db_del:
        flash("Product #" + id + " has been removed", "remove")
        return redirect(url_for('products'))
    else:
        return redirect(url_for('products'))

def db_delete_product(id):
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        sql = "DELETE FROM product_info WHERE id={};".format(id)
        cur.execute(sql)
        db.commit()
        return True
    except mysql.connector.Error as err:
        flash(err, "remove")
        print(err)
        return False
    finally:
        cur.close()
        db.close()
        app.config["PRODUCTS"] = Database(get_db())


def db_update_product(id, name, desc, price, bonus_price, photo):
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        sql = "UPDATE product_info SET name='{}', description='{}', normal_price='{}', bonus_price={}, photo='{}' WHERE id={};".format(name, desc, price, bonus_price, photo, id)
        print(sql)
        cur.execute(sql)
        db.commit()
        print("TRY")
        return True
    except mysql.connector.Error as err:
        flash(err, "remove")
        print(err)
        print("FAIL")
        return False
    finally:
        cur.close()
        db.close()
        app.config["PRODUCTS"] = Database(get_db())

def db_add_product(name, desc, price, bonus_price, img):
    db = get_db()
    db.ping(True)
    cur = db.cursor()

    try:
        sql = "INSERT INTO product_info (name, description, normal_price, bonus_price, photo) VALUE ('{}', '{}', {}, {}, '../{}');".format(name, desc, price, bonus_price, img)
        print(sql)
        cur.execute(sql)
        db.commit()
        print("TRY")
        return True
    except mysql.connector.Error as err:
        flash(err, "remove")
        print(err)
        print("FAIL")
        return False
    finally:
        cur.close()
        db.close()
        app.config["PRODUCTS"] = Database(get_db())

if __name__ == '__main__':
    app.run()