from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    from . import converter
    app.register_blueprint(converter.bp)
    return app