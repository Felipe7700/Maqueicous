import json
dados = {
    "Renan": "1234", 
    "Emilly": "1357",
    "Eduarda": "2468",
    "Felipe": "3425"
     
     }

arquivo = open("arquivo.json", "w")
arquivo.write(json.dumps(dados))


arquivo = open("arquivo.json", "r")
envio = arquivo.read()
print(envio)
print(type (envio))
arquivo.close()

def load(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    return json.loads(arquivo.read())

def save(nome_arquivo, novo_dado):
    arquivo = open(nome_arquivo, "w")
    arquivo.write(json.dumps(novo_dado))


def change_password(nome_arquivo, login, senha):
    arquivo = open(nome_arquivo, "r")
    dados = json.loads(arquivo.read())
    arquivo.close()
    arquivo = open(nome_arquivo, "w")
    dados[login] = senha
    arquivo.write(json.dumps(dados))
