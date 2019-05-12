from flask import Flask     # Import Flask

def create_app():

    app = Flask(__name__)       # Create a Flask "app" instance

    from app.code import bp as code_bp
    app.register_blueprint(code_bp)

    return app
