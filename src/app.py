import os

from flask import Flask
from database import db
from routes import create_graphql_route, create_rest_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # path to our config module

    # Graphql routes at /graphql/.
    create_graphql_route(app)

    # Anything not caught by above rule will be handled by REST routes.
    create_rest_routes(app)

    db.init_app(app)

    with app.app_context():
        db.create_all(app=app)

    return app
