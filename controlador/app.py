from flask import Flask,render_template, request
app = Flask(__name__, template_folder='../vista',static_folder='../static')

@app.route('/')
def inicio():
    return render_template('comunes/login.html')

@app.route('/Index')
def index():
    return render_template('comunes/index.html')

@app.route('/ciclos')
def ciclos():
    return render_template('ciclos/ciclosListado.html')

@app.route('/ciclosNuevo')
def ciclosNuevo():
    return render_template('ciclos/ciclosNuevo.html')

@app.route('/ciclosEditar')
def ciclosEditar():
    return render_template('ciclos/ciclosEditar.html')

@app.route('/ciclosEliminar')
def ciclosEliminar():
    return 'SE HA ELIMINADO EL CICLO'

@app.route('/recopilarDatosLogin',methods=['post'])
def recopilarDatosLogin():
    #nombreUsuario = request.form['nombreUsuario']
    #return 'Se verificara si existe el usuario '+nombreUsuario
    return render_template('comunes/index.html')

if __name__ == '__main__':
    app.run(debug=True)