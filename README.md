
# Sistema CRUD de Alunos e Professores

Este projeto é uma API RESTful simples construída com Flask, que utiliza um banco de dados MySQL para gerenciar um sistema CRUD (Create, Read, Update, Delete) para Alunos e Professores. Ele inclui funcionalidades para criar, ler, atualizar e deletar registros de alunos e professores, usando Flask e SQLAlchemy como ORM.

## Requisitos

Certifique-se de que os seguintes softwares estão instalados em seu ambiente de desenvolvimento:

- Python 3.7+
- MySQL Server
- Flask
- Flask-SQLAlchemy
- mysql-connector-python

### Instalação de Dependências

Você pode instalar as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

(O arquivo `requirements.txt` deve incluir os seguintes pacotes: `Flask`, `Flask-SQLAlchemy`, `mysql-connector-python`.)

## Configuração do Banco de Dados

1. Crie um banco de dados MySQL chamado `turma` (ou outro nome de sua escolha).
2. Configure suas credenciais de banco de dados no código dentro da variável `SQLALCHEMY_DATABASE_URI` no arquivo principal (`app.py`):

```python
app.config['SQLALCHEMY_DATABASE_URI'] =     '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        password='SUA_SENHA',
        server='localhost',
        database='turma'
    )
```

Substitua os valores `user`, `password`, `server` e `database` de acordo com suas configurações locais.

## Estrutura do Projeto

- `app.py`: Arquivo principal contendo a API e as rotas.
- Modelos de banco de dados: 
  - `Aluno`: Representa os alunos com campos `id`, `nome`, e `email`.
  - `Professor`: Representa os professores com campos `id`, `nome`, e `email`.
- Rotas implementadas:
  - `GET /alunos`: Retorna todos os alunos cadastrados.
  - `GET /alunos/<id>`: Retorna os detalhes de um aluno específico.
  - `POST /alunos`: Cria um novo aluno.
  - `PUT /alunos/<id>`: Atualiza os dados de um aluno específico.
  - `DELETE /alunos/<id>`: Deleta um aluno específico.

## Como Executar

1. Inicialize o banco de dados com as tabelas necessárias rodando o comando:

```bash
python app.py
```

O Flask irá automaticamente criar as tabelas para os modelos `Aluno` e `Professor` no banco de dados especificado.

2. A API estará disponível localmente em: `http://127.0.0.1:5000/`

## Exemplos de Uso

### Criar um Aluno (POST /alunos)

```json
{
  "nome": "João da Silva",
  "email": "joao.silva@email.com"
}
```

### Listar Alunos (GET /alunos)

Resposta:

```json
{
  "Alunos": [
    {
      "id": 1,
      "nome": "João da Silva",
      "email": "joao.silva@email.com"
    }
  ],
  "mensagem": "ok"
}
```

### Atualizar um Aluno (PUT /alunos/<id>)

```json
{
  "nome": "João Silva Atualizado",
  "email": "joao.silva@atualizado.com"
}
```

### Deletar um Aluno (DELETE /alunos/<id>)

Nenhum corpo é necessário para essa requisição. O aluno será removido.

## Contribuições

Sinta-se à vontade para contribuir com o projeto abrindo issues e enviando pull requests.

## Licença

Este projeto está sob a licença MIT.
