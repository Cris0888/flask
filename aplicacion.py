from flask import Flask,render_template,request,session
import mysql.connector


aplicacion=Flask(__name__)

conexion= mysql.connector.connect( 
host='localhost',
port='3306',
user= 'root',
password='',
database='productores')


cursor=conexion.cursor()


aplicacion.secret_key = '000013'


@aplicacion.route('/')
def index():
    return render_template('/login.html')


@aplicacion.route('/registro')
def registro():
    return render_template('/registro.html')


@aplicacion.route('/irabuscar')
def irabuscar():
    return render_template('/mostrar.html')


@aplicacion.route("/iragregar")
def iragregar():
    return render_template('/agregar.html')


@aplicacion.route('/create',methods=['POST'])
def create():
    nombre=request.form['nombre']
    contraseña=request.form['password']
    sql=f"INSERT INTO usuarios (id,nombre,contrasena) VALUES ('?','{nombre}','{contraseña}')"
    cursor.execute(sql)
    conexion.commit()
    return render_template("/login.html")


@aplicacion.route("/validacion", methods=['POST', 'GET'])
def validacion():
    if request.method == 'POST' and 'nombre' in request.form and 'password' in request.form:
        nombre=request.form['nombre']
        contrasena = request.form['password']
        sql=(f"SELECT * FROM usuarios WHERE nombre = '{nombre}'  AND contrasena = '{contrasena}'")
        cursor.execute(sql)
        resultado=cursor.fetchone()
        conexion.commit()
        

        if resultado:
            session['logueado']= True
            session["id"] = resultado[0]
            return render_template("/principal.html")
        else:
            return render_template("/login.html", denegado=" su acceso fue Denegado")
        
        
@aplicacion.route("/agregar" ,methods=['POST'])
def agregar():
        propietario=request.form['propietario']
        tipo=request.form['tipo']
        marca=request.form['marca']
        modelo=request.form['modelo']
        nacionalidad=request.form['nacionalidad']
        sql=f"INSERT INTO agregar (propietario,tipo,marca,modelo,nacionalidad) VALUES('{propietario}','{tipo}','{marca}','{modelo}','{nacionalidad}')"
        cursor.execute(sql)
        conexion.commit()
        return render_template("/agregar.html", aprobacion="Guardados Con Exito") 


@aplicacion.route("/buscar" ,methods=['POST'])
def buscar():
    busqueda=request.form["busqueda"]
    sql=f"SELECT propietario,tipo,marca,modelo,nacionalidad FROM agregar WHERE  propietario LIKE '%{busqueda}%'"
    cursor.execute(sql)
    resultado=cursor.fetchone()
    conexion.commit()
    return render_template ("/mostrar.html",resultado=resultado)


if __name__=='__main__':
    aplicacion.run(debug=True ,host="0.0.0.0", port=8081 )
