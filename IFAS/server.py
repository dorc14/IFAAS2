from flask import Flask
from flask_restful import Api
from routes import enableRoutes

app = Flask(__name__)

api = Api(app)

enableRoutes(api)

if __name__ == '__main__':
    app.run()