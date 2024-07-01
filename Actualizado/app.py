from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contacto'

mysql = MySQL(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        sexo = request.form['sexo']
        correo = request.form['email'] 
        mensaje = request.form['mensaje']
        aceptar_terminos = request.form.get('aceptar_terminos')

        if not aceptar_terminos:
            return 'Debe aceptar los términos y condiciones', 400

        # Insertar datos en la base de datos
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''INSERT INTO contacts (nombre, apellido, sexo, correo, mensaje)
                          VALUES (%s, %s, %s, %s, %s)''',
                       (nombre, apellido, sexo, correo, mensaje))
        mysql.connection.commit()
        cursor.close()
        
        return jsonify({'status': 'success', 'message': 'Mensaje enviado correctamente'})
    
    except Exception as e:
        print(f"Error al insertar en la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al enviar el mensaje'})

if __name__ == '__main__':
    app.run(debug=True)
