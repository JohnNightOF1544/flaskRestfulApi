from flaskRest.app import app
from flask import Flask, request, make_response, url_for, render_template, jsonify
from flask_restful import Resource, abort, marshal_with
from flaskRest.models.account import Account, db
from flaskRest.argumentParsing_dataFormating.accountParser import account_fields, account_login, account_parser, login_fields
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import datetime
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt, 
    unset_jwt_cookies, set_access_cookies, JWTManager, jwt_required, set_refresh_cookies
)




class TodoList(Resource):
    @jwt_required(refresh=True)
    @marshal_with(account_fields)
    def get(self):
        if request.method == 'GET':
            all_account = Account.query.all()
            return all_account, 200


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

    def post(self):
        name = request.json.get("name", None)
        password = request.json.get("password", None)

        user_login = Account.query.filter_by(name=name).first()

        if not user_login:
            return {'message': 'Please input exact {} or {} correctly from name'.format('name', 'password')}

        check_pass = check_password_hash(user_login.password, password)

        if not check_pass:
            return {'message': 'Please input {} or {} correctly from password'.format('name', 'password')}

        access_token = create_access_token(identity=user_login, fresh = True)
        refresh_token = create_refresh_token(identity=user_login)
        
        resp = jsonify({'access_token': access_token, 'refresh_token': refresh_token})

        set_access_cookies(resp, access_token)
        set_refresh_cookies(resp, refresh_token)

        return resp











            