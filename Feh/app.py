from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')
def principal():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['login']
    senha = request.form['senha']
    if usuario=='aluno' and senha=='1234':
        return f'você logou {usuario} e {senha}'
    return 'e-mail ou senha invalidos'


@app.route('/esqueceu_email')
def esqueceu():
    return 'você entrou na tela de esqueceu senha'

@app.route("/cadastro_esta")
def cada_esta():
    return render_template("cadastro1.html")

@app.route("/cadastro_emp")
def cada_emp():
    return render_template("cadastro2.html")
if __name__=="__main__":
    app.run(debug=True)
