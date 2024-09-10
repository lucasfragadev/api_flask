from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD=os.getenv('DB_SGBD'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        server=os.getenv('DB_SERVER'),
        database=os.getenv('DB_NAME')
    )

db = SQLAlchemy(app)

# CRUD // create, read, update e delete // 

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
    
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))

with app.app_context():
    db.create_all()


@app.route('/alunos', methods=['GET'])
def selecionar_aluno(): 
    alunos = Aluno.query.all() 
    alunos_json = [aluno.to_json() for aluno in alunos]
    
    return gerar_response (
        status=200, 
        nome_conteudo='Alunos', 
        conteudo=alunos_json,
        mensagem='ok'
    )

@app.route('/alunos/<id>', methods=['GET'])
def selecionar_alunos(id):
    aluno = Aluno.query.filter_by(id=id).first()
    aluno_json = aluno.to_json()

    return Response(json.dumps(aluno_json))

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    body = request.get_json()

    try:
        aluno = Aluno(nome=body['nome'], email=body['email'])
        db.session.add(aluno)
        db.session.commit()
        return gerar_response (
            201,
            'Aluno',
            aluno.to_json(),
            'Aluno criado com sucesso!'
        )
    except Exception:
        return gerar_response (
            400,
            'Aluno',
            {},
            'Erro ao cadastrar aluno.'
        )
    
@app.route('/alunos/<id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = Aluno.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if 'nome' in body:
            aluno.nome = body['nome']
        if 'email' in body:
            aluno.email = body['email']
        
        db.session.add(aluno)
        db.session.commit()
        return gerar_response (
            200,
            'Aluno',
            aluno.to_json(),
            'Aluno atualizado com sucesso!'
        )
    except Exception:
        gerar_response (
            400,
            'aluno',
            {},
            'Erro ao atualizar o aluno.'
        )

@app.route('/alunos/<id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = Aluno.query.filter_by(id=id).first()

    try:
        db.session.delete(aluno)
        db.session.commit()
        return gerar_response (
            202,
            'aluno',
            aluno.to_json(),
            'Aluno deletado.'
        )

    except Exception as e:
        print(e)
        gerar_response(
            400,
            'Aluno',
            {},
            'Erro ao deletar usuário.'
        )


def gerar_response(status, nome_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_conteudo] = conteudo

    if mensagem:
        body["mensagem"] = mensagem

    return Response(
        json.dumps(body),
        status=status,
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(debug=True)