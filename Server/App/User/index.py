from flask_restful import Resource, reqparse
from App.User.Method.post import signup, login
from App.User.Method.put import put
from flask import request


class HandleUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('func', type=str)
            args = parser.parse_args()

            if args['func'] == 'signup':
                return signup()
            elif args['func'] == 'login':
                return login()

        except SyntaxError:
            return {"error": "You don't send [func] data(signup or login)", "code": 400}, 400

    def put(self):
        return put()