from flaskRest.app import db, jwt

class Account(db.Model):
	__tablename__ = "account"
	id = db.Column(db.Integer, primary_key = True)
	public_id = db.Column(db.String(50), unique = True)
	name = db.Column(db.String(50), nullable=False)
	age = db.Column(db.Integer, nullable=False)
	course = db.Column(db.String(100), nullable=False)
	password = db.Column(db.String(255), nullable=False)


	def __init__(self, public_id, name, age, course, password):
		self.public_id = public_id
		self.name = name
		self.age = age
		self.course = course
		self.password = password

	def add_db_account(self):
		db.session.add(self)
		db.session.commit()

	def update_db_account(self):
		db.session.commit()

	def delete_db_account(self):
		db.session.delete(self)
		db.session.commit()

@jwt.user_identity_loader
def user_identity_lookup(user_login):
    return user_login.public_id




