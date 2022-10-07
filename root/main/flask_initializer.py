from flask import Flask
from flask_cors import CORS
from root.rest.rest_controller import RestController


class FlaskInitializer:

    def __init__(self):
        self._app: Flask = Flask(__name__)
        self._app.config['CORS_HEADERS'] = 'Content-type'
        # don't store secret_key like this in production, this is for development purpose only
        self._app.config['SECRET_KEY'] = '/xa1/xb4/x02,Rg/x89L/x19/xaab/xf5'
        self.init_rest_controller()
        CORS(self._app)

    @property
    def app_instance(self):
        return self._app

    def init_rest_controller(self):
        RestController.initialization()
        RestController.register(self._app, route_base='/')
        pass
