import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# app = Flask('flaskRest', instance_relative_config = True, static_folder='static', template_folder='templates')
app = Flask(__name__, instance_relative_config = True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
api = Api(app)
CORS(app)


from flaskRest.controller.login import TodoList, AccountLogin
from flaskRest.controller.register import Todo

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<account_id>')
api.add_resource(AccountLogin, '/account_login')



