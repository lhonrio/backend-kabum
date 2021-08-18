from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
        version='1.0',
        title='Cotação de Frete KaBuM!',
        description='Desafio: Criação de API para cotação de Frete Kabum',
        doc='/docs')

    def run(self,):
        self.app.run(
            debug=True
        )

server = Server()