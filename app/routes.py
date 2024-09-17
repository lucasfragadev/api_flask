from app.controllers.aluno_controller import aluno_bp
from app.controllers.professor_controller import professor_bp

def register_routes(app):
    app.register_blueprint(aluno_bp, url_prefix='/alunos')
    app.register_blueprint(professor_bp, url_prefix='/professores')
