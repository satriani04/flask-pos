from flask import Blueprint, render_template, request, redirect
from pos.models.products import Products
from pos.models import db

bp = Blueprint("products",__name__)

@bp.route("/")
def index():
	return redirect("/products")

@bp.route("/products")
def product_list():
	product = Products.query.all()
	return render_template("products/list.html", products=product)

@bp.route("/products/add", methods=["GET","POST"])
def products_add():
	if request.method == "GET":
		return render_template("products/form_add.html")

	product = Products()

	product.name = request.form['name']
	product.price = request.form['price']
	product.stock = request.form['stock']

	db.session.add(product)
	db.session.commit()

	return redirect("/products")


@bp.route("/products/update", methods=["GET","POST"])
def products_edit():
	if request.method == "GET":
		prod_id = request.args["id"]
		product = Products.query.filter_by(id=prod_id).first()
		return render_template("products/form_edit.html", product=product)

	prod_id = request.args["id"]
	product = Products.query.filter_by(id=prod_id).first()
	product.name = request.form['name']
	product.price = request.form['price']
	product.stock = request.form['stock']

	db.session.add(product)
	db.session.commit()
	return redirect("/products")

@bp.route("/products/delete", methods=["GET"])
def product_delete():
	prod_id = request.args["id"]
	product = Products.query.filter_by(id=prod_id).first()
	if product:
		db.session.delete(product)
		db.session.commit()
		return redirect("/products")