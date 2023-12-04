#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# No es necesario instalar, es parte del sistema standard de Python
import os
import time, datetime
#--------------------------------------------------------------------

app = Flask(__name__)

# Permitir acceso a la app desde cualquier origen externo con CORS

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
            # print(maxid[0])                # maxid[0] sería el primer valor de esa tupla (el unico que devuelve MAX(id))
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
    

mensaje = Mensaje("localhost", "root", "", "clientes")  # Objeto de clase Mensaje creado

# A continuación están los métodos que serán utilizados por el front-end al acceder a las distintas rutas de la @app con los methods GET, POST, PUT y DELETE, para así poder leer, agregar, modificar o eliminar mensajes en la BD de clientes (desde el formulario usado por los clientes o desde la pagina de admin).

# Para probar los metodos de las rutas de la @app con POSTMAN, elegir el BROWSER Agent de la web de POSTMAN, no usar ni el cloud, ni el desktop. Con POSTMAN se pueden simular acciones sin necesidad de tener el front end armado.

# Con los metodos POST y GET debo retornar un JSON y un codigo para saber si se ejecutó satisfactoriamente lo que intenté.

#--------------------------------------------------------------------
@app.route("/mensajes", methods=["GET"])
def listar_mensajes():                      # este es la definicion de un metodo de @app.route, se puede llamar igual
    respuesta = mensaje.listar_mensajes()   # esta es la invocacion al metodo de la clase Mensajes, aunque se llame igual
    return jsonify(respuesta)               # jsonify transforma a un objeto de python en un objeto JSON


#--------------------------------------------------------------------
@app.route("/mensajes", methods=["POST"])   # Mientras que "methods" sea distinto, la ruta puede ser exactamente igual
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
        return jsonify({"mensaje": "Mensaje agregado"}), 201        # Devulevo 2 datos: un JSON y un codigo 201
    else:
        return jsonify({"mensaje": "No fue posible registrar el mensaje"}), 400
  

#--------------------------------------------------------------------
@app.route("/mensajes/<int:id>", methods=["PUT"])   # <int:id> tomara un valor entero en la ruta y eso será "id"
def responder_mensaje(id):
    #Desde la página admin, ingreso la gestión
    gestion = request.form.get("gestion")   # se usa .form.get(), en vez de .form[]: "use it if the key might not exist"
    
    if mensaje.responder_mensaje(id, gestion):
        return jsonify({"mensaje": "Mensaje modificado"}), 200
    else:
        return jsonify({"mensaje": "Mensaje no encontrado"}), 403





mensaje.listar_mensajes_prolijo()

# mensaje.enviar_mensaje("Matias", "Seminara", "123456789", "matiasseminara@gmail.com", "Esta consulta es para ver la conexion a la base de datos")
# respuesta = mensaje.listar_mensajes()
# print(mensaje.responder_mensaje(1, "Ya le contesté"))
# print(mensaje.eliminar_mensaje(1))
# print(mensaje.mostrar_mensaje(2))


#--------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
