from flask import Flask, render_template, request, redirect, url_for, flash, session
from autenticacao.routes import autenticacao_bp
from alunos.routes import alunos_bp
app=Flask(__name__)
app.config['SECRET_KEY'] = "Maqueicous"

@app.route('/')
def principal():
    return redirect(url_for("login"))


if __name__=="__main__":
    app.run(debug=True)
