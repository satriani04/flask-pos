from flask import Flask
from pos.config import Config
from pos.models import db
from pos.views.products import bp

def create_app(config=Config):
	app = Flask(__name__)
	# load config
	app.config.from_object(config)

	# load sqlalchemy
	db.init_app(app)

	# register blueprint
	app.register_blueprint(bp)
	
	return app