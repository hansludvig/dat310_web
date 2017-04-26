"""
    Assignment 9
    @author: Hans Ludvig Kleivdal
"""

from flask import Flask, request, render_template, g, flash, redirect, url_for, session
import mysql.connector
#from werkzeug.security import generate_password_hash, check_password_hash
import json

app = Flask(__name__)
app.debug = True

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "admin"
app.config["DATABASE_DB"] = "test_storage"
app.config["DATABASE_HOST"] = "localhost"
app.secret_key = "any random string"


class Database1:

    def __init__(self):
        self.products = []
        self._load_products()

    def _load_products(self):

        db = self.get_db()
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
                    #"description": description,
                    "normal_price": float(normal_price) if float(normal_price).is_integer() else None,
                    "bonus_price": float(bonus_price) if bonus_price else None
                })
            print(self.products)
        except mysql.connector.Error as err:
            print(err)
        finally:
            cur.close()
            db.close()

    def get_db(self):
        if not hasattr(g, "_database"):
            g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"],
                                                  user=app.config["DATABASE_USER"],
                                                  password=app.config["DATABASE_PASSWORD"],
                                                  database=app.config["DATABASE_DB"])
        return g._database

def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                              password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database
def test():
    return Database1()

@app.route("/products")
def products():

    db = test()

    return render_template("products.html")

if __name__ == '__main__':
    app.run()