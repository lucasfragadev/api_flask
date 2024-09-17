from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar blueprints
    from app.controllers.aluno_controller import aluno_bp
    from app.controllers.professor_controller import professor_bp
    app.register_blueprint(aluno_bp)
    app.register_blueprint(professor_bp)

    with app.app_context():
        db.create_all()

    return app

