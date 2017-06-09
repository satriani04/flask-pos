from flask import Blueprint, render_template, request, redirect
from pos.models.transactions import Transactions
from pos.models.transactions_products import TransactionProducts
from pos.models import db

bp = Blueprint("transactions",__name__)

@bp.route("/transactions")
def transactions_list():
	transactions = Transactions.query.all()
	return render_template("transactions/list.html",transactions=transactions)

@bp.route("/transactions/add", methods=["GET","POST"])
def transactions_add():
	if request.method == "POST":
		# ambil data dari form html
		products = request.form.getlist("products")
		products_qty = request.form.getlist("products_qty")

		# buat transacsi utamanya
		transactions = Transactions()
		db.session.add(transactions)
		# flush terlebih dahulu untuk mencegah transaksi apabila gagal
		db.session.flush()

		# loop product
		for i, product in enumerate(products):
			transactions_products = TransactionProducts()
			transactions_products.transaction_id = transactions.id
			transactions_products.product_id = int(product)
			transactions_products.product_qty = int(products_qty[i])
			db.session.add(transactions_products)
			db.session.flush()

		# commit semua transaksi
		db.session.commit()
		return redirect("/transactions")
	return render_template("transactions/form_add.html")