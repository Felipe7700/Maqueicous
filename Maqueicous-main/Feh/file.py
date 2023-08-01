import json

def load(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        return json.load(arquivo)

def save(nome_arquivo, novo_dado):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(novo_dado, arquivo)

def cadastro_empr(nome_arquivo, email, nome, cnpj, senha, endereco, telefone, desc, prem):
    dados = load(nome_arquivo)
    dados["dados_empr"][email] = {
        "nome": nome,
        "cnpj": cnpj,
        "senha": senha,
        "endereco": endereco,
        "telefone": telefone,
        "desc": desc,
        "prem": prem
    }
    save(nome_arquivo, dados)

def cadastro_esta(nome_arquivo, email, nome, data_nasc, cpf, senha, endereco, telefone, campus, cre, area, curriculo):
    dados = load(nome_arquivo)
    dados["dados_esta"][email] = {
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "senha": senha,
        "endereco": endereco,
        "telefone": telefone,
        "campus": campus,
        "cre": cre,
        "area": area,
        "curriculo": curriculo
    }
    save(nome_arquivo, dados)

def change_password(nome_arquivo, email, senha):
    dados = load(nome_arquivo)
    dados[email]["senha"] = senha
    save(nome_arquivo, dados)