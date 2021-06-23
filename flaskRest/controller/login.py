from flaskRest.app import app
from flask import Flask, request, make_response, url_for, render_template
from flask_restful import Resource, abort, marshal_with
from flaskRest.models.account import Account, db
from flaskRest.argumentParsing_dataFormating.accountParser import account_fields, account_login, account_parser, login_fields
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime


class TodoList(Resource):
    @marshal_with(account_fields)
    def get(self):
        all_account = Account.query.all()
        return all_account, 200
        # return  make_response(render_template('login.html', all_account=all_account)) #can be used

    @marshal_with(account_fields)
    def post(self):
        args_parser = account_parser.parse_args(strict=True)

        hashed_password = generate_password_hash(
            args_parser['password'], 
            method='sha512'
        )

        add_account = Account(
            public_id=str(uuid.uuid4()), 
            name=args_parser['name'], 
            age=args_parser['age'], 
            course=args_parser['course'], 
            password=hashed_password
        )
        add_account.add_db_account()
        return add_account, 201

class AccountLogin(Resource):
    
    def get(self):
        """
        renders a simple HTML with email and password in a form.
        """
        return make_response(render_template('authlogin.html'))
    @marshal_with(login_fields)
    def post(self):

        args_login = account_login.parse_args(strict=True)

        add_user = Account.query.filter_by(name=args_login['name']).first()

        if not add_user:
            return make_response(
                'Please Input your username or password', 401,
                {'WWW.Authentication': 'Basic realm: "login required"'}
            )

        if check_password_hash(add_user.password, args_login['password']):

            token = jwt.encode({
                'public_id': add_user.public_id,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                },
                app.config['SECRET_KEY'])

            print({'token': token})
            # return {'token' : token.decode('UTF-8')}
            # return make_response({'token' : token})
            # return make_response({'result': 'success', 'token': token}, 200, {'authorization': token} )
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})











# class LoginAPI(Resource):
#     # added as /login

#     def get(self):
#         """
#         renders a simple HTML with email and password in a form.
#         """
#         headers = {'Content-Type': 'text/html'}
#         return make_response(render_template('login.html'), 200, headers)

#     def post(self):

#         email = request.form.get('email')
#         password = request.form.get('password')

#         # assuming the validation has passed.

#         payload = {
#             'user_id': query_user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
#         }

#         token = jwt\
#             .encode(payload, current_app.config['JWT_SECRET'], current_app.config['JWT_ALGORITHM'])\
#             .decode('utf-8')

#         # Is below the right way to set the token into header to be used in subsequent request?
#         # request.headers.authorization = token

#         # when {'authorization': token} below as a header, the header only shows up for /login not for any subsequent request.

#         return make_response({'result': 'success', 'token': token}, 200, {'authorization': token} )


# class ProtectedAPI(Resource):
#     @check_auth
#     def get(self):

#         return jsonify({'result': 'success', 'message': 'this is a protected view.'})


# decorator to check auth and give access to /protected
# def check_auth(f):

#     @wraps(f)
#     def authentication(*args, **kws):
#         # always get a None here.
#         jwt_token = request.headers.get('authorization', None)
#         payload = jwt.decode(jwt_token, 'secret_key', algorithms='HS512'])
#         # other validation below skipped.
#     return f(*args, **kws)
# return authentication