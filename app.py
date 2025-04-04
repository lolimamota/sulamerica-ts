from flask import Flask;

import requests;

import os;

from flask_cors import CORS;

from dotenv import load_dotenv;

# -------------------- LOGIN --------------------

urlLogin = "https://saude.sulamericaseguros.com.br/prestador/login/?accessError=2"


load_dotenv()

credenciais = {
    'codRef': os.getenv("COD_REF"),
    'user': os.getenv("USER"),
    'passwrd': os.getenv("PASSWORD")
}

requisicao = requests.Session()

response = requisicao.post(urlLogin, data=credenciais)

if response.status_code == 200 and "sucesso" in response.text.lower():
    print("Login realizado com sucesso!")
else:
    print("Não foi possível realizar o login.")



# ------------------- SEARCH --------------------

urlSearch = "https://saude.sulamericaseguros.com.br/prestador/servicos-medicos/contas-medicas/faturamento-tiss-3/faturamento/guia-de-consulta/"

response = requisicao.get(urlSearch)

if response.status_code == 200:
    print("Esta é a página pra buscar informações!")
else:
    print("Não foi possível chegar a página e busca. Status:", response.status_code)


# -------------------- SEARCH CLIENT ID ------------------------


urlPaciente = "https://saude.sulamericaseguros.com.br/lumis/portal/controller/html/PortalRequestParametersControllerHtml.jsp"

carteira = {
    'codPaciente': "55788888485177660015"
}

response = requisicao.post(urlPaciente, json=carteira)

if response.status_code == 200:
    print("Paciente localizado na base de dados! Dados:")
    print(response.json())
else:
    print("Paciente não encontrado! Status:", response.status_code)


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '<h1>API de automação de login</h1><hr>'

if __name__ == '__main__':
    app.run()