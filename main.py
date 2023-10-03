from flask import Flask
from database import db
from flask_migrate import Migrate
from usuarios import bp_usuario

app = Flask(__name__)

conexao = "sqlite:///meubanco.sqlite"

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACKMODIFICATION'] = False
app.register_blueprint(bp_usuario, 
                       url_prefix='/usuarios')          

db.init_app(app)



migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)