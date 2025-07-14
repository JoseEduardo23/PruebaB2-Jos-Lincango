from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': os.getenv("MYSQL_HOST", "maestro1"),
    'user': os.getenv("MYSQL_USER", "root"),
    'password': os.getenv("MYSQL_PASSWORD", "root"),
    'database': os.getenv("MYSQL_DB", "db_informacion"),
    'port': int(os.getenv("MYSQL_PORT", 3306))
}

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        experiencia = request.form.get('experiencia')
        formacion = request.form.get('formacion')

        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO datos (nombre, correo, experiencia, formacion) VALUES (%s, %s, %s, %s)",
            (nombre, correo, experiencia, formacion)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('formulario'))

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')