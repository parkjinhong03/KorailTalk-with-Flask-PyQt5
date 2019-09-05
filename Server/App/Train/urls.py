from flask_jwt_extended import jwt_required
from flask_restful import Resource
from App.Train.View import get


class Train(Resource):
    def get(self):
        return get.get()