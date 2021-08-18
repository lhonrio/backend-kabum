<h1 align='center'>
    Atividade Back-End Kabum
</h1>

<h2>Objetivo do Projeto:</h2>
Desenvolver uma <b>API Rest</b> que será utilizada pelo site para a consulta de opções de transportes dos produtos, onde cada transportadora terá seus requisitos e retornos de acordo com as <b>dimensões</b> e <b>peso</b>.
<br>
<br>
<h2>Tecnologias Utilizadas:</h2>

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- Bibliotecas: Requeriments.txt

<h2>Exemplo:</h2>

- Input: Altura e Largura em Centímetros e Peso em Gramas <b>(Itens Obrigatórios)</b>

```json
{
    "dimensao": {
                    "altura":102,
                    "largura":40
                },
    "peso":400
}
````

- Output: De acordo com as dimensões do produto será apresentada a(s) transportadoras disponíveis para entrega.
</br>

```json
[
	{
        "nome":"Entrega Ninja",
    	  "valor_frete": 12.00,
    	  "prazo_dias": 6
	},
	{
    	  "nome":"Entrega KaBuM",
    	  "valor_frete": 8.00,
    	  "prazo_dias": 4
	}
]
````
<h2>Clone o Repositório:</h2>

````bash
$ git clone https://github.com/lhonrio/DesafioKabum.git
````
<h3><b>OBS:</h3></b> Após rodar a aplicação a mesma será iniciada na porta 5000. </br>
</br>Para conferir o funcionamento da API utilize o Postman ou um aplicativo de sua preferencia com a seguinte URL: https://127.0.0.1:5000/ 
</br>
</br>Para consultar a documentação da API consulte: https://127.0.0.1:5000/docs 
</br>
</br><h3><b>Desenvolvido por:</h3></b>

- [Lucas Honório Lima](https://www.linkedin.com/in/lhonrio/)