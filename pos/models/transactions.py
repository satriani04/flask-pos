from pos.models import db
from datetime import datetime

class Transactions(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	create_on = db.Column(db.DateTime, nullable=False)
	def __init__(self):
		self.create_on = datetime.now()