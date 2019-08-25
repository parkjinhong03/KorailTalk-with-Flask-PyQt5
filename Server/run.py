from flask import Flask
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

from App.User.index import HandleUser

api.add_resource(HandleUser, '/user')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)