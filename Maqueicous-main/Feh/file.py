import json
dados={}

def load(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    return json.loads(arquivo.read())

def save(nome_arquivo, novo_dado):
    arquivo = open(nome_arquivo, "w")
    arquivo.write(json.dumps(novo_dado))
    arquivo.close()

def cadastro_empr(nome_arquivo, email, nome, cnpj, senha, endereco, telefone, desc, prem):
    arquivo = open(nome_arquivo, "r")
    dados = json.loads(arquivo.read())
    arquivo.close()
    dados["dados_empr"][email]:{
        email:{
            nome:"maria",
            cnpj:"12312312312312",
            senha:"1234",
            endereco:["estado", "cidade", "bairro", "cep"],
            telefone:["83988759854"],
            desc:"melhor empresa",
            prem:"123243534645654.pdf"
        }
    }
    arquivo = open(nome_arquivo, "w")
    arquivo.write(json.dumps(dados))
    arquivo.close()

def cadastro_esta(nome_arquivo, email, nome, data_nasc, cpf, senha, endereco, telefone, campus, cre, area, curriculo):
    arquivo = open(nome_arquivo, "r")
    dados = json.loads(arquivo.read())
    arquivo.close()
    dados["dados_esta"][email]={
            "nome":nome,
            "data_nasc":data_nasc,
            "cpf":cpf,
            "senha":senha,
            "endereco":endereco,
            "telefone":telefone,
            "campus":campus,
            "cre":cre,
            "area":area,
            "curriculo":curriculo
        }
    print (dados)
    arquivo = open(nome_arquivo, "w")
    arquivo.write(json.dumps(dados))
    arquivo.close()

def change_password(nome_arquivo, email, senha):
    arquivo = open(nome_arquivo, "r")
    dados = json.loads(arquivo.read())
    arquivo.close()
    arquivo = open(nome_arquivo, "w")
    dados[email]["senha"] = senha
    arquivo.write(json.dumps(dados))