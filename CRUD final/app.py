from flask import Flask, request, redirect, url_for, send_from_directory, render_template, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__, static_folder='.', template_folder='.')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'contacto'  

mysql = MySQL(app)

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crud')
def crud():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM contacts')
        contactos = cursor.fetchall()
        cursor.close()
        return render_template('admin.html', contactos=contactos)
    except Exception as e:
        print(f"Error al obtener los contactos de la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al obtener los contactos de la base de datos'})

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

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO contacts (nombre, apellido, sexo, correo, mensaje)
                          VALUES (%s, %s, %s, %s, %s)''',
                       (nombre, apellido, sexo, correo, mensaje))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('crud'))

    except MySQLdb.Error as e:
        print(f"Error MySQL al insertar en la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al enviar el mensaje (MySQL)'})

    except Exception as e:
        print(f"Error general al insertar en la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al enviar el mensaje'})

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE FROM contacts WHERE id = %s', [id])
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('crud'))

    except Exception as e:
        print(f"Error al eliminar el contacto: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al eliminar el contacto'})

@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    try:
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        sexo = request.form['sexo']
        correo = request.form['email']
        mensaje = request.form['mensaje']
        aceptar_terminos = request.form.get('aceptar_terminos')

        if not aceptar_terminos:
            return 'Debe aceptar los términos y condiciones', 400

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE contacts
                          SET nombre = %s, apellido = %s, sexo = %s, correo = %s, mensaje = %s
                          WHERE id = %s''',
                       (nombre, apellido, sexo, correo, mensaje, id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('crud'))

    except MySQLdb.Error as e:
        print(f"Error MySQL al actualizar en la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al actualizar el contacto (MySQL)'})

    except Exception as e:
        print(f"Error general al actualizar en la base de datos: {e}")
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al actualizar el contacto'})

if __name__ == '__main__':
    app.run(debug=True)
