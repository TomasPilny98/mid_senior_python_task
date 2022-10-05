from flask import Flask
from flask_cors import CORS
from root._rest.rest_controller import RestController


class FlaskInitializer:

    def __init__(self):
        self._app: Flask = Flask(__name__)
        self._app.config['CORS_HEADERS'] = 'Content-type'
        self.init_rest_controller()
        CORS(self._app)

    @property
    def app_instance(self):
        return self._app

    def init_rest_controller(self):
        RestController.initialization()
        RestController.register(self._app, route_base='/')
        pass
