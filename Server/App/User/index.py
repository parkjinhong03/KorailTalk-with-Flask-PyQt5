from flask_restful import Resource
# from App.User.Method.post import post


class HandleUser(Resource):
    def get(self):
        return 'RESTful API'

    def post(self):
        return 'POST'