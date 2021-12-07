import json
from flask import request, render_template, make_response
from flask_restful import Resource
from API import IFAPI
from Config.addones import headers
from http import HTTPStatus


class getAllIfs(Resource):
    def get(self):
            allIfs = IFAPI.getAllIfs()
            return make_response(render_template('home.html', data=allIfs),  HTTPStatus.OK, headers)


class getIf(Resource):
    def get(self, id):
            newIf = IFAPI.getIf(id)
            return make_response(render_template('if.html', data=newIf),  HTTPStatus.OK, headers)


class If(Resource):
    def post(self):
            form = request.form.to_dict()
            transaction = IFAPI.createIf(form)
            return make_response(render_template('status.html', data=json.loads(json.dumps(transaction))),
                                        HTTPStatus.OK, headers)


class Execute(Resource):
    def post(self, name):
            param = request.get_json()
            result = IFAPI.executeIf(name, param)
            return json.loads(json.dumps(result))