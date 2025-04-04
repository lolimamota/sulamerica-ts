from flask import Flask, requests;


urlLogin = "https://saude.sulamericaseguros.com.br/prestador/login/?accessError=2"

credenciais = {
    'codRef': "100000009361",
    'user': "master",
    'passwrd': "837543"
}

session = requests.Session()

response = session.post(login_url, dados=credenciais)

if response.status_code == 200:
    print("Login realizado com sucesso!")
else:
    print("Não foi possível realizar o login. Status:", response.status_code)





app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)