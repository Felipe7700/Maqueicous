from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length
from autenticacao.autenticacao_service import autenticar, salvar_usuario


app=Flask(__name__)#criação da aplicação flask
app.config['SECRET_KEY'] = "Maqueicous" #A 'SECRET_KEY' é usada para proteger os dados da sessão e outras coisas sensíveis
"""app.register_blueprint(autenticacao_bp)
app.register_blueprint(alunos_bp)
"""
class Cliente: 
    def __init__(self, email_acad, senha_esta, cep_alu, cpf_alu, tel_alu, cre_alu, curriculo):
        self.email_acad = email_acad
        self.senha_esta = senha_esta
        self.cep_alu = cep_alu
        self.cpf_alu = cpf_alu
        self.tel_alu = tel_alu
        self.cre_alu = cre_alu
        self.curriculo = curriculo

class Empresa:
    def __init__(self, cnpj, razao_social, email_empr, senha_empr, cep_empr, tel_empr, certificados_empr):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.email_empr = email_empr
        self.senha_empr = senha_empr
        self.cep_empr = cep_empr
        self.tel_empr = tel_empr
        self.certificados_empr = certificados_empr

        
        
empresas = [
    Empresa('15245632521456', 'Mercadinho Renan', 'email_empr', 'senha_empr', 'cep_empr', 'tel_empr', 'certificados_empr')
]

estagiarios = [
    Cliente('ribeiro.renan@academico.ifpb.edu.br', '1234', '58300000', '08731693440', '83981819023', '90.3', 'awdoak')
]


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    senha = PasswordField ("senha", validators=[DataRequired(), Length(min=3)])

class RegistroForm(FlaskForm):
    cnpj = StringField("cnpj", validators=[DataRequired()])
    razao_social = StringField("razao_social", validators=[DataRequired()])
    email_empr = StringField("email_empr", validators=[DataRequired()])
    senha_empr = PasswordField ("senha_empr", validators=[DataRequired()])
    cep_empr = StringField("cep_empr", validators=[DataRequired()])
    tel_empr = StringField('tel_empr', validators=[DataRequired()])
    certificados_empr = StringField('certificados_empr', validators=[DataRequired()])


@app.route("/cadastro_empr", methods = ['GET', 'POST'])
def cadastro():
    registroform = RegistroForm()
    
    if request.method == 'GET':
        return render_template('cadastro_empr.html', form=registroform)
    
    if not registroform.validate_on_submit():
        flash("Dados obrigatorios não preenchidos")
        return render_template("cadastro_empr.hmtl")
    

    try:
        salvar_usuario(usuario)
        flash("Usuário cadastrado com sucesso")
        return redirect(url_for("main"))
    except:
        flash("Usuário já cadastrado")
        return render_template("cadastro_empr.html")

    

def buscar_usuario(email): #função para verificar se o usuario já está cadastrado
    for estagiario in estagiarios: #buscar usuario para saber se ele já ta cadastrado
    
        if estagiario.email_acad == email:#se o email queeu forneci no login é igual a um deles que está na lista
            return estagiario #vai retornar os dados do estagiário no código
    
    return None #se colocar o return none dentro na identação vários emails irão dar errado ao acontecer o login, por isso que tem q ser fora

def validar_login (email, senha): 

    usuario_encontrado = buscar_usuario(email)#


    if usuario_encontrad__init__o == None:
        raise Exception ("Usario não encontrado")
    
    if not usuario_encontrado.senha == senha:#se a senha que o cara preencheu no login não for encontrada, sobe a mensagem de erro
        raise Exception ("Senha Incorreta")
    
    return usuario_encontrado.email_acad


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


@app.route("/catalogo")
def catalogo():
    if session.get("Usuario",None):
        return render_template("catalogo_empr.html")
    flash("Faça o login!")
    return redirect(url_for("login"))

@app.route("/escolha")
def escolha():from flask import Flask, render_template, request, redirect, url_for, flash, session
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


@app.route("/catalogo")
def catalogo():
    if session.get("Usuario",None):
        return render_template("catalogo_empr.html")
    flash("Faça o login!")
    return redirect(url_for("login"))

@app.route("/escolha")
def escolha():
    return render_template("escolha.html")


if __name__=='__main__':
    app.run(debug=False)

    return render_template("escolha.html")

@app.route("/cadastro_empr")
def cadastro_empr():
    return render_template("cadastro_empr.html")

@app.route("/cadastro_esta")
def cadastro_esta():
    return render_template("cadastro_esta.html")



if __name__=='__main__':
    app.run(debug=False)

