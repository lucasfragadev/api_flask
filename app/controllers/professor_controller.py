from flask import Blueprint, request, jsonify
from app.services.professor_service import get_all_professores, get_professor_by_id, create_professor, update_professor, delete_professor
from app.utils.response import gerar_response

professor_bp = Blueprint('professor_bp', __name__)

@professor_bp.route('/professores', methods=['GET'])
def listar_professores():
    professores = get_all_professores()
    return gerar_response(200, 'professores', [professor.to_json() for professor in professores], 'ok')

@professor_bp.route('/professores<int:id>', methods=['GET'])
def obter_professor(id):
    professor = get_professor_by_id(id)
    if professor:
        return gerar_response(200, 'professor', professor.to_json(), 'ok')
    return gerar_response(404, 'professor', {}, 'professor não encontrado')

@professor_bp.route('/professores', methods=['POST'])
def adicionar_professor():
    data = request.get_json()
    professor = create_professor(data)
    return gerar_response(201, 'professor', professor.to_json(), 'professor criado com sucesso!')

@professor_bp.route('/professores<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = get_professor_by_id(id)
    if professor:
        data = request.get_json()
        professor_atualizado = update_professor(professor, data)
        return gerar_response(200, 'professor', professor_atualizado.to_json(), 'professor atualizado com sucesso!')
    return gerar_response(404, 'professor', {}, 'professor não encontrado')

@professor_bp.route('/professores<int:id>', methods=['DELETE'])
def excluir_professor(id):
    professor = get_professor_by_id(id)
    if professor:
        delete_professor(professor)
        return gerar_response(202, 'professor', professor.to_json(), 'professor excluído com sucesso!')
    return gerar_response(404, 'professor', {}, 'professor não encontrado')



