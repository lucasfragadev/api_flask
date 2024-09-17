from app import db

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email
        }
