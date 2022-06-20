from flaskRest.app import app
from flask import Flask, request
from flaskRest.models.account import Account
from functools import wraps
import jwt

def token_required(func):
	@wraps(func)
	def wrapped(*args, **kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']
		# token = request.args.get('token')

		# token = request.headers.get('authorization', None)

		if not token:
			return {
				'message': 'a valid token is missing'
			}, 401
		try:
			payload = jwt.decode(token, app.config['SECRET_KEY'])
			current_user = Account.query.filter_by(public_id=payload['public_id']).first()
		except:
			return {'message': 'Token is invalid'}, 403
		return func(current_user, *args, **kwargs)
	return wrapped



# def token_required(func):

#     @wraps(func)
#     def authentication(*args, **kws):
#         # always get a None here.
#         jwt_token = request.headers.get('authorization', None)
#         payload = jwt.decode(jwt_token, 'secret_key', algorithms='HS512')
#         # other validation below skipped.
#     	return func(*args, **kws)
# 	return authentication