from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length


app=Flask(__name__)
app.config['SECRET_KEY'] = "Maqueicous" #A 'SECRET_KEY' é usada para proteger os dados da sessão e outras coisas sensíveis
"""app.register_blueprint(autenticacao_bp)
app.register_blueprint(alunos_bp)
"""
class Cliente: 
    def __init__(self, email_acad, senha, cep_alu, cpf_alu, tel_alu, cre_alu ):
        self.email_acad = email_acad
        self.senha = senha
        self.cep_alu = cep_alu
        self.cpf_alu = cpf_alu
        self.tel_alu = tel_alu
        self.cre_alu = cre_alu

estagiarios = [
    Cliente('ribeiro.renan@academico.ifpb.edu.br', '1234', '58300000', '08731693440', '83981819023', '90.3')
]

def buscar_usuario(email): #função para verificar se o usuario já está cadastrado
    for estagiario in estagiarios: #buscar usuario para saber se ele já ta cadastrado
    
        if estagiario.email_acad == email:#se o email queeu forneci no login é igual a um deles que está na lista
            return estagiario #vai retornar os dados do estagiário no código
    
    return None #se colocar o return none dentro na identação vários emails irão dar errado ao acontecer o login, por isso que tem q ser fora

def validar_login (email, senha): 

    usuario_encontrado = buscar_usuario(email)#


    if usuario_encontrado == None:
        raise Exception ("Usario não encontrado")
    
    if not usuario_encontrado.senha == senha:#se a senha que o cara preencheu no login não for encontrada, sobe a mensagem de erro
        raise Exception ("Senha Incorreta")
    
    return usuario_encontrado.email_acad

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    senha = PasswordField ("senha", validators=[DataRequired(), Length(min=3)])

@app.route('/')
def main():
    return redirect(url_for('login'))



@app.route("/login",  methods=['POST', 'GET'])
def login():
    form=LoginForm() #CRIAR INSTANCIA NA PÁGINA LOGIN



    if request.method == "POST": #pra ficar visivel o que está sendo enviado
        
        if not form.validate_on_submit(): #se o que está no formulario não tiver correto, essa mensagem sobe na tela
            flash ("Email ou Senha Incorreta") #se email ou senha estiverem errados entrarão nesse if
            return render_template ("teste.html", form = form)
        
        
        try:#Se a validação for bem-sucedida, o email do usuário é armazenado na sessão.
            validacao = validar_login(form.email.data, form.senha.data) #para buscar o email e senha que foi enviado no formulario
            session["Usuario"] = validacao #se usuario conseguiu validar o login dele, então esse cara existe e pode mudar de rota.
            return redirect ("/catalogo") #
            #o session: Se as credenciais estiverem corretas, o email do usuário é armazenado na sessão e o usuário é redirecionado para a rota /catalogo
        
        except:
            flash ("Email ou Senha Incorreta")
        
    
    return render_template ("teste.html", form = form) #form=form está passando a instância do formulário para a página HTML para que ela possa exibir o formulário e interagir com os dados enviados pelo usuário.

if __name__=='__main__':
    app.run(debug=False)
