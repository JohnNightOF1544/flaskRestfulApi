from flaskRest.app import app
from flask import Flask, jsonify
from flask_restful import Resource 
from flaskRest.models.blocklist_token import TokenBlockList, db
from datetime import datetime

from flask_jwt_extended import ( 
    get_jwt, unset_jwt_cookies, jwt_required
)

class Logout(Resource):
	@jwt_required(refresh=True)
	def delete(self):
		jti = get_jwt()["jti"]
		print(jti)
		now = datetime.now()
		db.session.add(TokenBlockList(jti=jti, created_at=now))
		db.session.commit()

		resp = jsonify({"code": 200, "msg": "Logout Successful", "jti": "jwt revoked"})
		unset_jwt_cookies(resp)
		return resp








