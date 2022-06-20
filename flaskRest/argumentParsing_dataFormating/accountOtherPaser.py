from flask_restful import reqparse, fields

account_OtherParser = reqparse.RequestParser()
account_OtherParser.add_argument("name", type=str, help="Name of the user is required", required=True)
account_OtherParser.add_argument("age", type=int, help="Age of the user is required", required=True)
account_OtherParser.add_argument("course", type=str, help="Course of the user is required", required=True)


account_UPDATE_parser = reqparse.RequestParser()
account_UPDATE_parser.add_argument("name", type=str, help="Name of the user is required")
account_UPDATE_parser.add_argument("age", type=int, help="Age of the user is required")
account_UPDATE_parser.add_argument("course", type=str, help="Course of the user is required")
account_UPDATE_parser.add_argument("password", type=str, help="Course of the user is required")


account_OtherFields = {
    # 'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'course': fields.String
}