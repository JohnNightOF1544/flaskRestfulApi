from flask_restful import reqparse, fields

account_parser = reqparse.RequestParser()
account_parser.add_argument("name", type=str, help="Name of the user is required", required=True)
account_parser.add_argument("age", type=int, help="Age of the user is required", required=True)
account_parser.add_argument("course", type=str, help="Course of the user is required", required=True)
account_parser.add_argument("password", type=str, help="Password of the user is required", required=True)


account_login = reqparse.RequestParser()
account_login.add_argument("name", type=str, help="Please input your name")
account_login.add_argument("password", type=str, help="Please input your password")

account_fields = {
    # 'id': fields.Integer,
    # 'public_id': fields.String,
    'name': fields.String,
    'age': fields.Integer,
    'course': fields.String,
    # 'password': fields.String
}

# ang dahilan nah hindi gumana ang aking token sah curl
# >>>
login_fields = {
    'name': fields.String,
    'password': fields.String
}