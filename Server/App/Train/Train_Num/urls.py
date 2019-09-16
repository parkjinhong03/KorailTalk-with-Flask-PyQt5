from flask_restful import Resource
from App.Train.Train_Num.View import get, post, delete
from flask_jwt_extended import jwt_required


class Train_Num(Resource):
    def get(self, date):
        return get.get(date)

    @jwt_required
    def post(self, date):
        return post.post(date)

    @jwt_required
    def delete(self, date):
        return delete.delete(date)