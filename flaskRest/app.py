import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
# from flask_httpauth import HTTPBasicAuth


app = Flask('flaskRest', instance_relative_config = True, static_folder='static', template_folder='templates')
# app = Flask(__name__, instance_relative_config = True) #will work also
app.config.from_object('config')
app.config.from_pyfile('config.py')

jwt = JWTManager(app)
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

# auth = HTTPBasicAuth()

from flaskRest.controller.login import TodoList, AccountLogin
from flaskRest.controller.register import Todo
from flaskRest.controller.logout import Logout 

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<account_id>') #can input another argument
api.add_resource(AccountLogin, '/account_login')
api.add_resource(Logout, '/logout')
# api.add_resource(LoginAPI, '/login')


