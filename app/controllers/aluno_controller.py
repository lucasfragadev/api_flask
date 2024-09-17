from flask import Blueprint, request, jsonify
from app.services.aluno_service import get_all_alunos, get_aluno_by_id, create_aluno, update_aluno, delete_aluno
from app.utils.response import gerar_response

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = get_all_alunos()
    return gerar_response(200, 'alunos', [aluno.to_json() for aluno in alunos], 'ok')

@aluno_bp.route('/alunos<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = get_aluno_by_id(id)
    if aluno:
        return gerar_response(200, 'aluno', aluno.to_json(), 'ok')
    return gerar_response(404, 'aluno', {}, 'Aluno não encontrado')

@aluno_bp.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.get_json()
    aluno = create_aluno(data)
    return gerar_response(201, 'aluno', aluno.to_json(), 'Aluno criado com sucesso!')

@aluno_bp.route('/alunos<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = get_aluno_by_id(id)
    if aluno:
        data = request.get_json()
        aluno_atualizado = update_aluno(aluno, data)
        return gerar_response(200, 'aluno', aluno_atualizado.to_json(), 'Aluno atualizado com sucesso!')
    return gerar_response(404, 'aluno', {}, 'Aluno não encontrado')

@aluno_bp.route('/alunos<int:id>', methods=['DELETE'])
def excluir_aluno(id):
    aluno = get_aluno_by_id(id)
    if aluno:
        delete_aluno(aluno)
        return gerar_response(202, 'aluno', aluno.to_json(), 'Aluno excluído com sucesso!')
    return gerar_response(404, 'aluno', {}, 'Aluno não encontrado')
