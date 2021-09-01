from flaskRest.app import app, jwt
from flask import Flask, request, redirect, jsonify
from flask_restful import Resource, abort, marshal_with
# from flaskRest.authorization.auth import token_required
from flaskRest.models.account import Account, db
from flaskRest.argumentParsing_dataFormating.accountOtherPaser import account_OtherParser, account_UPDATE_parser, account_OtherFields
from flaskRest.argumentParsing_dataFormating.accountParser import account_login, account_fields
from flask_jwt_extended import ( 
    get_jwt_identity, get_jwt, jwt_required, unset_jwt_cookies
)
# from flask_httpauth import HTTPBasicAuth

# @auth.verify_password
# def verify_password(usename, password):
#     pass_hash = Account.query.filter_by(name=name).first()
#     if pass_hash and check_password_hash(pass_hash.password, password):
#         return pass_hash

class Todo(Resource):
	# @auth.login_required
	@jwt_required(refresh=True)
	# @token_required
	@marshal_with(account_fields)
	def get(self, account_id: int):

		identity = get_jwt_identity()

		account_query = Account.query.filter_by(public_id=identity).first()

		print(account_query.public_id)

		if not account_query:
			resp = jsonify({"code": "Check for error code", "msg": "Have a exact credentials"})
			unset_jwt_cookies(resp)
			return resp

		if account_query:
			accout_first = Account.query.filter_by(id=account_id).first()
			return account_query, 200

		# args_parser = account_login.parse_args()
		# account_query = Account.query.filter_by(id=account_id).first()
		# return account_query, 200

	@jwt_required(refresh=True)
	@marshal_with(account_OtherFields)
	def put(self, account_id: int):

		identity = get_jwt_identity()
		print(identity)

		args_parser = account_UPDATE_parser.parse_args(strict=True)
		
		result = Account.query.filter_by(public_id=identity).first()
		print(result)

		if not result:
			abort(404, message="Account doesn't exist")
		# result.admin = True
		if result:
			update_account = Account.query.filter_by(id=account_id).first()
			if "name" in args_parser:
				update_account.name = args_parser['name']
			if "age" in args_parser:
				update_account.age = args_parser['age']
			if "course" in args_parser:
				update_account.course = args_parser['course']

			result.update_db_account()
		
			return result, 201
	
	@jwt_required(refresh=True)
	@marshal_with(account_fields)
	def delete(self, account_id: int):
		identity = get_jwt_identity()

		del_result = Account.query.filter_by(public_id=identity).first()

		if not del_result:
			abort(404, message="Account doesn't exist")
			return redirect('/logout')

		if del_result:
			update_account = Account.query.filter_by(id=account_id).first()
			update_account.delete_db_account()
			return update_account, 201
	