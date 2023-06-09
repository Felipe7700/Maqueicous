from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['login']
    senha = request.form['senha']
    if usuario=='aluno' and senha=='1234':
        return f'você logou {usuario} e {senha}'
    return 'e-mail ou senha invalidos'


@app.route('/escolha')
def escolha():
    return render_template("escolha.html")

@app.route('/esqueceu_email')
def esqueceu():
    return 'você entrou na tela de esqueceu senha'

if __name__=="__main__":
    app.run(debug=True)