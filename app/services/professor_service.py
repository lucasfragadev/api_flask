from app.models.professor_model import Professor
from app import db

def get_all_professores():
    return Professor.query.all()

def get_professor_by_id(id):
    return Professor.query.filter_by(id=id).first()

def create_professor(data):
    professor = Professor(nome=data['nome'], email=data['email'])
    db.session.add(professor)
    db.session.commit()
    return professor

def update_professor(professor, data):
    if 'nome' in data:
        professor.nome = data['nome']
    if 'email' in data:
        professor.email = data['email']
    db.session.commit()
    return professor

def delete_professor(professor):
    db.session.delete(professor)
    db.session.commit()