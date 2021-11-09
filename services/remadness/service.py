from flask import (
    Blueprint
)

from flask_restful import (
    Api, Resource, reqparse
)

bp = Blueprint('remadness_api', __name__, url_prefix='/remadness')
api = Api(bp)


class SystemStateRepository1(Resource):
    def get(self):
        return {'y': 'hello'}


api.add_resource(SystemStateRepository1, '/fd')
