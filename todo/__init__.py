"""
use __init.py__ to make Python treat 
directories containing the file as packages
"""
from flask import Flask

# the method of creation of application


def create_app():
    app = Flask(__name__)

    from .views.routes import api  # "." means routing method
    app.register_blueprint(api)
    """
    Register a blueprint multiple times on an 
    application with different URL rules.
    """

    return app
