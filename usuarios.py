from flask import Blueprint
from flask import render_template, request
from models import Usuario


bp_usuario = Blueprint("usuarios",__name__, template_folder="templates")

@bp_usuario.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('usuarios_create.html')
    
    
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        csenha = request.form.get('csenha')
        return 'datos recebidos'


    u = Usuario(nome, email, senha, csenha)
    db.session.add(u)
    db.usuario.session.commit()
    return 'datos cadastrado'