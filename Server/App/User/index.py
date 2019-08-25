from flask_restful import Resource
from App.User.Method.post import post


class HandleUser(Resource):
    def post(self):
        return post()