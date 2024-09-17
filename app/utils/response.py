from flask import Response
import json

def gerar_response(status, nome_conteudo, conteudo, mensagem=False):
    body = {nome_conteudo: conteudo}
    if mensagem:
        body['mensagem'] = mensagem
    return Response(json.dumps(body), status=status, mimetype='application/json')
