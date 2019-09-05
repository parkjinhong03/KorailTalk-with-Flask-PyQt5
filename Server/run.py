from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

from App.User.urls import HandleUser
from App.Train.urls import Train


api.add_resource(HandleUser, '/user')
api.add_resource(Train, '/train')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)