from flask import Flask, render_template, request, redirect, url_for, flash, session
import file
app=Flask(__name__)
app.config['SECRET_KEY'] = "Maqueicous"

@app.route('/')
def principal():
    return redirect(url_for("login"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('login', 'campo e-mail vazio')
        senha = request.form.get('senha', 'campo senha vazio')
        dados = file.load("arquivo.json")
        if dados.get(usuario) == senha:
            session['logado'] = usuario
            return f'você logou'
        
        flash('dados invalidos')
        return redirect('/')
    
    return render_template('login.html')
    

@app.route('/cadastro')
def cadastro():
    if session.get("logado",None):
        return redirect(url_for("cadastro"))
    return render_template("escolha.html")

@app.route('/esqueceu')
def esqueceu():
    return render_template("esqueceu.html")

@app.route('/esqueceu_senha', methods=['GET', 'POST'])
def esqueceu_senha():
    if request.method == 'POST':
        dados = file.load("arquivo.json")
        email = request.form.get('email', 'campo usuario vazio')
        if dados.get(email):
            senha_nova = request.form.get('nova_senha', 'campo senha vazio')
            conf_senha = request.form.get('conf_senha', 'campo confirmar senha vazio')
            if senha_nova == conf_senha:
                file.change_password("arquivo.json", email, senha_nova)
                return redirect('/login')
            else:
                flash('senha invalida')
                return redirect('/esqueceu')
        flash('email invalido')
        return redirect('/esqueceu')

@app.route("/cadastro_esta")
def cada_esta():
    if session.get("logado",None):
        return redirect(url_for("escolha"))
    return render_template("cadastro2.html")

@app.route("/cadastro_emp")
def cada_emp():
    if session.get("logado",None):
        return redirect(url_for("escolha"))
    return render_template("cadastro2.html")


if __name__=="__main__":
    app.run(debug=True)