from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
from autenticacao.autenticacao_dao import Usuario
from autenticacao.autenticacao_service import autenticar, salvar_usuario

autenticacao_bp = Blueprint("autenticacao", __name__, url_prefix="/auth")


class LoginForm(FlaskForm):
    login = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])


class RegistroForm(FlaskForm):
    login = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=8)])
    nome = StringField("Nome", validators=[DataRequired()])
    cpf = StringField("CPF", validators=[DataRequired(), Length(11)])
    

@autenticacao_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    registroForm = RegistroForm()
    if request.method == 'GET':
        return render_template("login.html", form=registroForm)
    
    if not registroForm.validate_on_submit():
        flash("Dados obrigatórios não preenchidos")
        return render_template("login.html")
    
    usuario = Usuario(
        registroForm.login.data,
        registroForm.senha.data,
        registroForm.nome.data,
        "Aluno",
    )
    try:
        salvar_usuario(usuario)
        flash("Usuário cadastrado com sucesso")
        return redirect(url_for("escolha"))
    except:
        flash("Nome de usuário já cadastrado")
        return render_template("login.html")
    

@autenticacao_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "GET":
        return render_template("index.html", form=form)

    if not form.validate_on_submit():
        flash("Login ou senha não informada!")
        return redirect(url_for("hello_world"))

    try:
        if autenticar(form.login.data, form.senha.data):
            session["usuario_logado"] = form.login.data
            return redirect(url_for("main"))
    except:
        flash("Usuário não cadastrado!")
        return redirect(url_for("hello_world"))

    flash("Login ou senha inválida!")
    return redirect(url_for("hello_world"))


@autenticacao_bp.route("/logout")
def logout():
    del session["usuario_logado"]
    return redirect(url_for("hello_world"))
