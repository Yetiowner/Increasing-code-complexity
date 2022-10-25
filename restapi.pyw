from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import string

app = Flask(__name__)
api = Api(app)

ALPHABETDICT = {}
for i in string.printable:
  ALPHABETDICT[str(bin(ord(i)))[2:]] = i


class Characters(Resource):
    def get(self, bin_code):
        return ALPHABETDICT[bin_code]
        

api.add_resource(Characters, '/characters/<bin_code>')


if __name__ == '__main__':
    app.run(port="5002")