import clientRequests
from flask_restful import Api

def enableRoutes(api:Api):
    api.add_resource(clientRequests.getAllIfs, '/')
    api.add_resource(clientRequests.getIf, '/if/<string:id>')
    api.add_resource(clientRequests.If, '/if')
    api.add_resource(clientRequests.Execute, '/if/<name>/execute')