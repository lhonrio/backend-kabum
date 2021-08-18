from src.controllers.retorno_cotacao import *

#Função com o método de Entrega Ninja - Expressa
def entrega_ninja(altura,largura,peso):
        condicoes = 10 <= altura <= 200 and 6 <= largura <= 140 and peso > 0
        if condicoes:
            constante_ninja = 0.3
            cotacao_frete = (peso*constante_ninja)/10
            prazo = 6
            metodo = {'nome': 'Entrega Ninja', 'valor_frete': f'{cotacao_frete:.2f}', 'prazo_dias': prazo}
            return metodo
        else:
            None

#Função com o método de Entrega KaBuM - Padrão
def entrega_kabum(altura,largura,peso):
        condicoes = 5 <= altura <= 140 and 13 <= largura <= 125 and peso > 0
        if condicoes:
            constante_ninja = 0.2
            cotacao_frete = (peso*constante_ninja)/10
            prazo = 4
            metodo = {'nome': 'Entrega KaBuM', 'valor_frete': f'{cotacao_frete:.2f}', 'prazo_dias': prazo}
            return metodo
        else:
            None
