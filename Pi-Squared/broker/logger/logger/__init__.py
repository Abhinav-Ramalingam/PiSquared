import os
import sys
from flask import Flask
from flask import request, Response
from . import db
from . import logger
from . import logging_client
import json


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='devdev',
        DATABASE=os.path.join(app.instance_path, 'logger.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/log', methods=['POST'])
    def log():
        msg = None
        try:
            print("log log log", file=sys.stderr)
            print(request.data, file=sys.stderr)
            msg = logger.logMessage(request.data)

        except Exception as e:
            print(e)
            return Response("invalid request", status=400, mimetype='text/plain')

        return Response("hi", status=200, mimetype='application/json')

    @app.route('/getChat', methods=['POST'])
    def getChat():
        msg = None
        try:
            msg = logger.getMessages(request.data)
        except Exception as e:
            print(e)
            return Response("invalid request", status=400, mimetype='text/plain')

        return Response(json.dumps(msg), status=200, mimetype='application/json')

    with app.app_context():
        db.init_app(app)

    return app
