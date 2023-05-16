import os
from flask import Flask, request,send_file
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
#app = Flask(__name__)
#api = Api(app)

class ObjectStorage(Resource):

    def put(self, object_name):
        # upload file
        try:
            file = request.files['file']
            file.save(object_name)
            return {'status': 'success'}
        except Exception as e:
            return {'status': 'fail'}

    def get(self, object_name):
        # download file
        try:
            file = open(object_name, 'rb')
            return send_file(file, mimetype='application/octet-stream')
        except Exception as e:
            return {'status': 'fail'}

    def delete(self, object_name):
        try:
            os.remove(object_name)
            return {'status': 'success'}
        except Exception as e:
            return {'status': 'fail'}

api.add_resource(ObjectStorage, '/objects/<string:object_name>')
if __name__ == '__main__':
    app.run()