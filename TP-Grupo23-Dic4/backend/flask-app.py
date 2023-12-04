#--------------------------------------------------------------------
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time, datetime
#--------------------------------------------------------------------

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}) 

class Mensaje:
    def __init__(self, host_, user_, password_, database_):
        self.conn = mysql.connector.connect(
            host = host_,
            user = user_,
            password = password_
        )

        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"USE {database_}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database_}")
                self.conn.database = database_
            else:
                raise err

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS mensajes (
            id int(11) NOT NULL AUTO_INCREMENT,
            nombre varchar(30) NOT NULL,
            email varchar(60) NOT NULL,
            telefono varchar(10) NOT NULL,
            excursion tinyint(5) NOT NULL,
            fecha_viaje date NOT NULL,
            cant_personas tinyint(20) NOT NULL,
            comentario_cliente varchar(500) NOT NULL,
            fecha_envio datetime NOT NULL,
            leido tinyint(1) NOT NULL,
            gestion varchar(500) DEFAULT NULL,
            fecha_gestion datetime DEFAULT NULL,
            PRIMARY KEY(`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
            ''')            
        self.conn.commit()
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    #----------------------------------------------------------------
    def enviar_mensaje(self, nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario):
        sql = "INSERT INTO mensajes(nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario_cliente, fecha_envio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        fecha_envio = datetime.datetime.now()
        valores = (nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario, fecha_envio)
        self.cursor.execute(sql, valores)        
        self.conn.commit()
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        return True

    #----------------------------------------------------------------
    def listar_mensajes(self):
        self.cursor.execute("SELECT * FROM mensajes")
        mensajes = self.cursor.fetchall()
        return mensajes
    
    #----------------------------------------------------------------
    def listar_mensajes_prolijo(self):
            self.cursor.close()
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT MAX(id) AS max_id FROM mensajes")
            maxid = self.cursor.fetchone()
            self.cursor.close()
            self.cursor = self.conn.cursor(dictionary=True)
            print("-"*20)
            for id in range(1, maxid[0]+1,1):
                sql = f"SELECT id, nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario_cliente, fecha_envio, leido, gestion, fecha_gestion FROM mensajes WHERE id = {id}"  
                self.cursor.execute(sql)
                print(self.cursor.fetchone())
                print("-"*20)

    #----------------------------------------------------------------
    def responder_mensaje(self, id, gestion):
        fecha_gestion = datetime.datetime.now()
        sql = "UPDATE mensajes SET leido = 1, gestion = %s, fecha_gestion = %s WHERE id = %s"
        valores = (gestion, fecha_gestion, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def eliminar_mensaje(self, id):
        self.cursor.execute(f"DELETE FROM mensajes WHERE id = {id}")
        self.conn.commit()
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor.rowcount > 0

    #----------------------------------------------------------------
    def mostrar_mensaje(self, id):
         sql = f"SELECT id, nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario_cliente, fecha_envio, leido, gestion, fecha_gestion FROM mensajes WHERE id = {id}"
         self.cursor.execute(sql)
         return self.cursor.fetchone()
    

# Objeto de clase Mensaje creado
mensaje = Mensaje("subtrooper14.mysql.pythonanywhere-services.com", "subtrooper14", "Comision23501", "subtrooper14$clientes")


#--------------------------------------------------------------------
@app.route("/mensajes", methods=["GET"])
def listar_mensajes():                      
    respuesta = mensaje.listar_mensajes()   
    return jsonify(respuesta)               


#--------------------------------------------------------------------
@app.route("/mensajes", methods=["POST"])
def agregar_producto():
    #Recojo los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    excursion = request.form['excursion']
    fecha_viaje = request.form['fecha']
    cant_personas = request.form['personas']
    comentario_cliente = request.form['comentarios']

    if mensaje.enviar_mensaje(nombre, email, telefono, excursion, fecha_viaje, cant_personas, comentario_cliente):
        return jsonify({"mensaje": "Mensaje agregado"}), 201
    else:
        return jsonify({"mensaje": "No fue posible registrar el mensaje"}), 400
  

#--------------------------------------------------------------------
@app.route("/mensajes/<int:id>", methods=["PUT"])
def responder_mensaje(id):
    #Desde la página admin, ingreso la gestión
    gestion = request.form.get("gestion")
    
    if mensaje.responder_mensaje(id, gestion):
        return jsonify({"mensaje": "Mensaje modificado"}), 200
    else:
        return jsonify({"mensaje": "Mensaje no encontrado"}), 403


#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
