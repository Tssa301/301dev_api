from flask import Flask, jsonify, request
import json

app = Flask(__name__)


desenvolvedores = [
    {'id': '0', 'nome': 'Tiago', 'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Silva', 'habilidades': ['Python', 'Django']}
]

#Por ID devolve, altera e deleta um desevolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desevolvedor de ID {} não existe'. format(id)
            response = {'status': 'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Admin da API'
            response = {'status': 'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})


#Lista todos os Devs e permiti a inserção de um novo Dev.
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__=='__main__':
    app.run(debug=True)
