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
            senha_nova = request.form.get('nova_senha', False)
            conf_senha = request.form.get('conf_senha', False)
            if senha_nova == conf_senha and senha_nova:
                file.change_password("arquivo.json", email, senha_nova)
                return redirect('/login')
            else:
                flash('senha invalida')
                return redirect('/esqueceu')
        flash('email invalido')
        return redirect('/esqueceu')

@app.route("/cadastro_esta", methods = ['POST', 'GET'])
def cadastro_esta():
    if request.method == 'POST':
        nome_esta = request.form.get('nome_esta', False)
        data_nasc_esta = request.form.get('data_nasc_esta', False)
        email_esta = request.form.get('email_esta', False)
        senha_esta = request.form.get('senha_esta', False)
        cpf_esta = request.form.get('cpf_esta', False)
        bairro_esta = request.form.get('bairro_esta', False)
        cidade_esta = request.form.get('cidade_esta', False)
        estado_esta = request.form.get('estado_esta', False)
        telefone_esta = request.form.get('telefone_esta', False)
        cep_esta = request.form.get('cep_esta', False)
        campus_esta = request.form.get('campus_esta', False)
        cre_esta = request.form.get('cre_esta', False)
        area_esta = request.form.get('area_esta', False)
        curriculo_esta = request.form.get('curriculo_esta', False)
        file.cadastro_esta("arquivo.json", email_esta, nome_esta, data_nasc_esta, cpf_esta, senha_esta, [estado_esta, cidade_esta, bairro_esta, cep_esta], [telefone_esta], campus_esta, cre_esta, area_esta, curriculo_esta)
    if session.get("logado",None):
        return redirect(url_for("escolha"))
    return render_template("cadastro_esta.html")

@app.route("/cadastro_emp", methods = ['GET', 'POST'])
def cadastro_emp():
    if request.method == 'POST':
        print (request.form)
        nome_empr = request.form.get('nome_empr', False)
        cnpj_empr = request.form.get('cnpj_empr', False)
        email_empr = request.form.get('email_empr', False)
        senha_empr = request.form.get('senha_empr', False)
        cidade_empr = request.form.get('cidade_empr', False)
        estado_empr = request.form.get('estado_empr', False)
        bairro_empr = request.form.get('bairro_empr', False)
        telefone_empr = request.form.get('telefone_empr', False)
        cep_empr = request.form.get('cep_empr', False)
        desc_empr = request.form.get('desc_empr', False)
        prem_empr = request.form.get('prem_empr', False)
        file.cadastro_empr("arquivo.json", email_empr, nome_empr, cnpj_empr, senha_empr, [estado_empr, cidade_empr, bairro_empr, cep_empr], telefone_empr, desc_empr, prem_empr)
    if session.get("logado",None):
        return redirect(url_for("escolha"))
    return render_template("cadastro_empr.html")

@app.route('/debug')
def debug():
    return file.dados

if __name__=="__main__":
    app.run(debug=True)