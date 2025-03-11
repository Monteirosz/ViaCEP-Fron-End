from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_cep', methods=['POST'])
def buscar_cep_front():
    cep = request.form.get('cep')
    response = requests.get(f'http://127.0.0.1:7777/buscar_cep/{cep}')
    dados = response.json()
    return render_template('resultado.html', dados=dados)

@app.route('/historico', methods=['GET'])
def todos_cep():
    requisicao = requests.get('http://127.0.0.1:7777/ver_tabela')
    dados = requisicao.json()
    return render_template('historico.html', dados=dados)
if __name__ == '__main__':
    app.run(debug=True, port=8888)