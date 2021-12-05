from flask import Flask
from flask_restful import Api
import clientRequests

app = Flask(__name__)

api = Api(app)

api.add_resource(clientRequests.getAllIfs, '/')
api.add_resource(clientRequests.getIf, '/if/<string:id>')
api.add_resource(clientRequests.If, '/if')
api.add_resource(clientRequests.Execute, '/if/<name>/execute')

if __name__ == '__main__':
    app.run()