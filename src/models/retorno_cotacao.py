from flask_restx import fields

from src.server.instance import server

dimensao = server.api.model('Dimensao',{
    'altura': fields.Integer(description='Altura do Produto'),
    'largura': fields.Integer(description='Largura do Produto')
})

requisicao = server.api.model('Requisicao', {
    'dimensao': fields.Nested(dimensao),
    'peso' : fields.Integer(description='Peso do Produto')
})

retorno = server.api.model('Retorno', {
        'nome': fields.String(description='Nome do Método de Envio'),
        'valor_frete': fields.String(description='Preço do Frete'),
        'prazo_dias': fields.Integer(description='Prazo de Entrega')})  
        
   