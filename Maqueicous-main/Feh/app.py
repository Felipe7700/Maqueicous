from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length


app=Flask(__name__)
app.config['SECRET_KEY'] = "Maqueicous"
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

def buscar_usuario(email):
    for estagiario in estagiarios:

        if estagiario.email_acad == email:
            return estagiario
    
    return None

def validar_login (email, senha):

    usuario_encontrado = buscar_usuario(email)


    if usuario_encontrado == None:
        raise Exception ("Usario não encontrado")
    
    if not usuario_encontrado.senha == senha:
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



    if request.method == "POST":
        
        if not form.validate_on_submit():
            flash ("Email ou Senha Incorreta")
            return render_template ("teste.html", form = form)
        
        
        try:
            validacao = validar_login(form.email.data, form.senha.data)
            session["Usuario"] = validacao
            return redirect ("/catalogo")
        
        except:
            flash ("Email ou Senha Incorreta")
        
    
    return render_template ("teste.html", form = form)

if __name__=='__main__':
    app.run(debug=False)
