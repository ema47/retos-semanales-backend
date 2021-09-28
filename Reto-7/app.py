from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tienda.db'
db = SQLAlchemy(app)

@app.route('/ping')
def ping():
    return 'pong'

class Usuario (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    is_active = db.Column(db.Boolean)

@app.route('/crear_usuario' , methods=['POST'])
def crear_usuario():
    user = Usuario( username = request.form['username'] , is_active = True )
    db.session.add(user)
    db.session.commit()
    return 'OK' , 201

@app.route('/listar_usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        print(usuario)
    return 'OK'
    
if __name__ == '__main__':
    app.run()