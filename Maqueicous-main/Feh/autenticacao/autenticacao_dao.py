class Usuario:
    def __init__(self, login, senha, nome, papel):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.papel = papel


dados = []


def buscar_usuario_por_login(login):
    for dado in dados:
        if dado.login == login:
            return dado

    return None


def criar(usuario):
    dados.append(usuario)