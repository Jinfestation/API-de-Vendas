import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


#  página inicial
@app.route('/')
def homepage():
    return 'Hello world '

#  página de request


@app.route('/req')
def request():
    tabela = pd.read_csv('apiv.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


app.run(host='0.0.0.0')
