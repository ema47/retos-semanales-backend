from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

departamentos = {
    'dep01': {
        'nombre': 'Lima',
        'capital': 'Lima',
        'poblacion': 10628470
    },
    'dep02': {
        'nombre': 'Amazonas',
        'capital': 'Chachapoyas',
        'poblacion': 426806
    },
    'dep03': {
        'nombre': 'Ica',
        'capital': 'Ica',
        'poblacion': 975182
    },
    'dep04': {
        'nombre': 'Pasco',
        'capital': 'Cerro de Pasco',
        'poblacion': 271904
    },
    'dep05': {
        'nombre': 'Tumbes',
        'capital': 'Tumbes',
        'poblacion': 251521
    }
}

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/departamentos')
def obtener_departamentos():
    return {
        'ok': True,
        'content' : departamentos,
        'message' : 'se devuelven todos los departamentos'
    }