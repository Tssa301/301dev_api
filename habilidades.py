from flask_restful import Resource


lista_habilidades = ['python', 'Java', 'Flask', 'PHP']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades
