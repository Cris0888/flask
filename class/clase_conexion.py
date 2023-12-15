import mysql.connector
conexion= mysql.connector.connect( 
host='localhost',
port='3306',
user= 'root',
passwd='',
database='productores' )
cursor=conexion.cursor()