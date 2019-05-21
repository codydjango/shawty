import os
from flask import Flask
from routes import create_routes
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    create_routes(app)

    db.init_app(app)

    with app.app_context():
        db.create_all(app=app)

    return app
