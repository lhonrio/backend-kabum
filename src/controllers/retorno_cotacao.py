from flask import Flask, request
from flask_restx import Api, Resource
from src.server.instance import server
from src.models.retorno_cotacao import requisicao, retorno
from src.models.metodos import *

app = server.app
api = server.api

@api.route('/cotacao')
class retorno_cotacao(Resource):
    @api.expect(requisicao, validate=True)
    @api.marshal_with(retorno)
    def post(self, ):
        #Coletando o Json da Entrada
            payload = api.payload

            #Etapa que faz a captura das dimensões
            altura = payload["dimensao"]["altura"]
            largura = payload["dimensao"]["largura"]
            peso = payload["peso"]
            
            #Etapa que realiza o cálculo das Modalidades
            expressa = entrega_ninja(altura, largura, peso)
            padrao = entrega_kabum(altura, largura, peso)

            #Etapa que realiza a validação dentro das Modalidades
            if expressa == None and padrao == None:
                return []

            elif expressa == None:
                return [padrao]

            elif padrao == None:
                return [expressa]

            else:
                return [expressa, padrao]
