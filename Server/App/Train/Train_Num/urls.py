from flask_restful import Resource
from App.Train.Train_Num.View import get, post


class Train_Num(Resource):
    def get(self, date):
        return get.get(date)

    def post(self, date):
        return post.post(date)