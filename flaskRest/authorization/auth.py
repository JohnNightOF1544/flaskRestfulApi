from flask import Flask, request, jsonify
from flaskRest.models.account import Account
from functools import wraps
import jwt

def token_required(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		token = None

		if 'x-access-tokens' in request.headers:
			token = request.headers['x-access-tokens']
		if not token:
			return jsonify({'message': 'a valid token is missing'})
		try:
			result = jwt.decode(token, app.config[SECRET_KEY])
			current_user = Account.query.filter_by(public_id=data['public_id']).first()
		except:
			return jsonify({'message': 'Token is invalid'})

		return f(current_user, *args, **kwargs)
	return decorator
		