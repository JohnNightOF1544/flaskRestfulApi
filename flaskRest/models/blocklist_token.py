from flaskRest.app import db, jwt
from datetime import datetime

class TokenBlockList(db.Model):
	__tablename__ = "tokenblocklist"

	id = db.Column(db.Integer, primary_key=True)
	jti = db.Column(db.String(36), nullable=False)
	created_at = db.Column(db.DateTime(timezone = False), default=datetime.now())


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
	jti = jwt_payload["jti"]
	token = db.session.query(TokenBlockList.id).filter_by(jti=jti).scalar()
	return token is not None


