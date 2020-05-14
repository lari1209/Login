from flask import render_template, request, session, flash, redirect, url_for
from dao import UsuarioDao
from login import db, app

usuario_dao = UsuarioDao(db)

# Tela inicial
@app.route('/')
def index():
    return render_template('home.html')

# Página após logar
@app.route('/homepage')
def homepage():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('homepage')))
    return render_template('homepage.html')

# Página de login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

# Autenticação de credenciais
@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.busca_por_id(request.form['id'], request.form['senha'])
    if usuario:
        # se senha do usuario e id estiverem corretos
        if usuario.senha == request.form['senha'] and request.form['id'] == usuario.id:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Login ou senha incorreto, tente novamente!')
        return redirect(url_for('login'))

# Logout da conta
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário está logado!')
    return redirect(url_for('index'))
