import mysql.connector

user="root"
password=""
host="localhost"
port=3306
database="proyectofinal"



conexion= mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    port=port,
    database=database)
