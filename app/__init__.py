from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# Initialisation de l'objet app
db = SQLAlchemy()


def create_app():
    # creation de l'objet app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Link app et db
    db.init_app(app)

    # Enregistrement des blueprint
    from .views import bp
    app.register_blueprint(bp)

    # creation des tables
    with app.app_context():
        db.create_all()

    return app
