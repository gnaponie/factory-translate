import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import api 


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(api.api, url_prefix='/api/v1')

@app.route('/')
def main():
    return 'Factory Translate'

if __name__ == '__main__':
    app.run()
