from flask import Flask
from pos.config import Config
from pos.models import db
from pos.views import products, transactions

def create_app(config=Config):
	app = Flask(__name__)
	# load config
	app.config.from_object(config)

	# load sqlalchemy
	db.init_app(app)

	# register blueprint
	app.register_blueprint(products.bp)
	app.register_blueprint(transactions.bp)
	
	return app