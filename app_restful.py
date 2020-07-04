from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id': '0', 'nome': 'Tiago', 'habilidades': ['Python', 'Flask']},
    {'id': '1', 'nome': 'Silva', 'habilidades': ['Python', 'Django']}
]

#Por ID devolve, altera e deleta um desevolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desevolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o Admin da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return(response)

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

#Lista todos os Devs e permiti a inserção de um novo Dev.
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

#Rotas URL:
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__=='__main__':
    app.run(debug=True)