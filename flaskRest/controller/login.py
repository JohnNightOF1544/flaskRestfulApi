from flaskRest.app import app
from flask import Flask, request, jsonify, make_response
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
        return  all_account

    @marshal_with(account_fields)
    def post(self):
        args_parser = account_parser.parse_args(strict=True)

        hashed_password = generate_password_hash(args_parser['password'], method='sha256')

        add_account = Account(public_id=str(uuid.uuid4()), name=args_parser['name'], age=args_parser['age'], course=args_parser['course'], password=hashed_password)
        add_account.add_db_account()
        return add_account, 201

class AccountLogin(Resource): 
    @marshal_with(login_fields)
    def post(self):

        args_login = account_login.parse_args(strict=True)

        # password = args_login['password']
        # auth = request.authorization

        # if not auth or not auth.name or not auth.password:  
        #     return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        add_user = Account.query.filter_by(name=args_login['name']).first()
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')

        if not add_user:
            return make_response('Please Input your username or password', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')

        if check_password_hash(add_user.password, args_login['password']):
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            token = jwt.encode({'public_id': add_user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            print('jovence')
            # return jsonify({'token' : token.decode('UTF-8')})
            return token, 201
            print('hehehe')
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'}) 

