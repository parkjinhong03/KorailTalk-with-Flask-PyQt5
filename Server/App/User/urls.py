from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from App.User.View.post import signup, login
from App.User.View.put import put
from App.User.View.delete import delete


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

        except:
            return {"error": "You don't send [func] data(signup or login)", "code": 400}, 400

    @jwt_required
    def put(self):
        return put()

    @jwt_required
    def delete(self):
        return delete()