from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contactos = [
    {"id": 1, "nombre": "Asd", "sexo": "masculino", "email": "juan@example.com"},
    {"id": 2, "nombre": "María", "sexo": "femenino", "email": "maria@example.com"}
]


@app.route('/')
def formulario():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', contactos=contactos)

@app.route('/submit', methods=['POST'])
def submit_form():
    nombre = request.form['nombre']
    sexo = request.form['sexo']
    email = request.form['email']

    nuevo_contacto = {"id": len(contactos) + 1, "nombre": nombre, "sexo": sexo, "email": email}
    contactos.append(nuevo_contacto)

    return redirect(url_for('admin'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    global contactos
    contactos = [contacto for contacto in contactos if contacto['id'] != id]
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
