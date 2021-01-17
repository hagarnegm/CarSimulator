from data_simulator import data, images
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class OBDData(Resource):
    def get(self):
        return data

    def post(self):
        return data


class CarImages(Resource):
    def get(self):
        return images

    def post(self):
        return images


api.add_resource(OBDData, '/obd')
api.add_resource(CarImages, '/images')

if __name__ == 'main':
    app.run(debug=True)

