from flask import Flask
from app.routes.index_routes import register_index_routes
from app.routes.review_routes import register_review_routes

def create_app():
    app = Flask(__name__)

    register_index_routes(app)
    register_review_routes(app)

    return app
