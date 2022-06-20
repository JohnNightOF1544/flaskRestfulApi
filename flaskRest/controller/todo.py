from flaskRest.app import app, db
from flask import Flask, request, redirect, jsonify, url_for
from flask_restful import Resource, abort, marshal_with
# from flaskRest.authorization.auth import token_required
from flaskRest.models.account import Account
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

		if not account_query:
			return abort(404, message="Account id not exist")

		if request.method == 'GET':

			account_first = Account.query.filter_by(id=account_id).first()

			if not account_first:
				return abort(404, message="Account id not exist")

			if account_first:
				return account_first, 200

		# args_parser = account_login.parse_args()
		# account_query = Account.query.filter_by(id=account_id).first()
		# return account_query, 200

	@jwt_required(refresh=True)
	@marshal_with(account_OtherFields)
	def put(self, account_id: int):

		identity = get_jwt_identity()

		args_parser = account_UPDATE_parser.parse_args(strict=True)
		
		update_result = Account.query.filter_by(public_id=identity).first()

		if not update_result:
			return abort(404, message="Account doesn't exist")
		# update_result.admin = True

		if request.method == 'PUT':

			if update_result:
				update_account = Account.query.filter_by(id=account_id).first()
				if not update_account:
					return abort(404, message="Account id not exist")
				if "name" in args_parser:
					update_account.name = args_parser['name']
				if "age" in args_parser:
					update_account.age = args_parser['age']
				if "course" in args_parser:
					update_account.course = args_parser['course']

				update_account.update_db_account()
			
				return update_result, 202
	
	@jwt_required(refresh=True)
	@marshal_with(account_fields)
	def delete(self, account_id: int):
		identity = get_jwt_identity()

		del_result = Account.query.filter_by(public_id=identity).first()

		if not del_result:
			
			return abort(404, message="Account doesn't exist")

		if request.method == 'DELETE':

			if del_result:
				account_result = Account.query.filter_by(id=account_id).first()
				if not account_result:
					return abort(404, message="Account is not exist")
				account_result.delete_db_account()
				return del_result, 202
