from flask import Flask, jsonify                            # Import flask class and jsonify to send responses in JSON format
from marshmallow.exceptions import ValidationError          # Raises an error when validation fails on a field
from flask_sqlalchemy import  SQLAlchemy                    # This is the ORM
from flask_marshmallow import Marshmallow                   # Importing the Marshmallow class
from flask_bcrypt import Bcrypt                             # Hashing package
from flask_jwt_extended import JWTManager                   # Retrieves information form JWT
from flask_migrate import Migrate                           # Package to handle migrations

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    from dotenv import load_dotenv
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('default_settings.app_config')   # Loads the configuration for the app object from default_settings.py

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db) 

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    @app.errorhandler(ValidationError)
    def handle_bad_request(error):  
        return(jsonify(error.messages), 400)

    @app.errorhandler(500)
    def handle_500(error):
        app.logger.error(error)
        return ("Server error: AKA bad stuff", 500)

    return app