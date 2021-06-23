from flask import Flask, request
from flask_restful import Resource, abort, marshal_with
from flaskRest.authorization.auth import token_required
from flaskRest.models.account import Account, db
from flaskRest.argumentParsing_dataFormating.accountOtherPaser import account_OtherParser, account_UPDATE_parser, account_OtherFields
from flaskRest.argumentParsing_dataFormating.accountParser import account_login, account_fields


class Todo(Resource):
	@token_required
	@marshal_with(account_fields)
	def get(self, account_id):
		args_parser = account_login.parse_args()
		account_query = Account.query.filter_by(id=account_id).first()
		return account_query, 200

	@token_required
	@marshal_with(account_OtherParser)
	def put(self, account_id):
		args_parser = account_UPDATE_parser.parse_args() 
		result = Account.query.filter_by(id=account_id).first()
		if not result:
			abort(404, message="Account doesn't exist")
		# result.admin = True
		if "name" in args_parser:
			result.name = args_parser['name']
		if "age" in args_parser:
			result.age = args_parser['age']
		if "course" in args_parser:
			result.course = args_parser['course']

		result.update_db_account()
		
		return result, 201

	@token_required
	def delete(self, account_id):
		del_result = Account.query.filter_by(id=account_id).first()
		if not del_result:
			abort(404, message="Account doesn't exist")

		del_result.delete_db_account()
	

		















# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

# class Todo(Resource):
#     def get(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]


#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201