import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from api import translate_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(translate_api, url_prefix='/api/v1')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
