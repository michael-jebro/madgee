import dbman as db

from flask import (
    g, abort
)

from model.cloudapp_master import (
    CloudAppMaster, AppNotFound
)

from flask_restful import (
    Api, Resource, reqparse
)

def register_endpoints(api):
    api.add_resource(CloudAppRepository, '/cloudapps/<token>/<target>/')
    api.add_resource(LoginEndpoint, '/mglogin/<token>/')


class CloudAppRepository(Resource):
    def get(self, token, target):
        #Validate token somehow. maybe using native flask signing mechanism or jwt
        cloudapp_master = CloudAppMaster(1)
        if target == 'all':
            return cloudapp_master.get_all_apps(), 200

        elif target == 'user_all':
            print(cloudapp_master.get_user_apps())
            return cloudapp_master.get_user_apps(), 200

        else:
            try:
                return cloudapp_master.get_app(target)

            except AppNotFound:
                abort(404)



class LoginEndpoint(Resource):
    pass

