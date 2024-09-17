from app.models.aluno_model import Aluno
from app import db

def get_all_alunos():
    return Aluno.query.all()

def get_aluno_by_id(id):
    return Aluno.query.filter_by(id=id).first()

def create_aluno(data):
    aluno = Aluno(nome=data['nome'], email=data['email'])
    db.session.add(aluno)
    db.session.commit()
    return aluno

def update_aluno(aluno, data):
    if 'nome' in data:
        aluno.nome = data['nome']
    if 'email' in data:
        aluno.email = data['email']
    db.session.commit()
    return aluno

def delete_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()
