import os
from flask import Flask
from database import db
from schema import schema
from flask_graphql import GraphQLView
from routes import create_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # path to our config module

    # graphql routes
    app.add_url_rule('/graphql/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    # rest routes
    create_routes(app)

    db.init_app(app)

    with app.app_context():
        db.create_all(app=app)

    return app
