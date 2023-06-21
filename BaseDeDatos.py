from Registro import Registro
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="password", database="proyectoFinal")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    if x == 'ispc':
        mycursor.execute('USE ispc')
    else:
        mycursor.execute("CREATE DATABASE mydatabase")

class BaseDeDatos:
    def __init__(self):
        self.__baseDeDatos__ = []

    def buscar_por_ley(self, ley):
        for registro in self.__baseDeDatos__:
            if (registro.nroNormativa == ley):
                return registro
        return False
    
    def agregar(self, registro):
        self.__baseDeDatos__.append(registro)

    def buscar_por_nroRegistro(self, nroRegistro):
        for registro in self.__baseDeDatos__:
            if (registro.nroRegistro == nroRegistro):
                return registro
        return False
    
    def buscar_por_palabra_clave(self, palabraClave):
        busqueda = []
        for registro in self.__baseDeDatos__:
            for keyword in registro.palabrasClaves:
                if palabraClave in keyword:
                    busqueda.append(registro)
        if busqueda:
            return busqueda
        else:
            return False

        
    def admin_agregar(self, registro, usuario):
        if (usuario["rol"] == "admin" and isinstance(registro, Registro)):
            self.__baseDeDatos__.append(registro)
            return True
        return False
    
    def admin_modificar(self, registro, usuario):
        if (usuario["rol"] == "admin" and isinstance(registro, Registro)):
            for item in self.__baseDeDatos__:
                if item.nroRegistro == registro.nroRegistro:
                    item.tipoNormativa = registro.tipoNormativa
                    item.nroNormativa = registro.nroNormativa
                    item.fecha = registro.fecha
                    item.descripcion = registro.descripcion
                    item.categoria = registro.categoria
                    item.jurisdiccion = registro.jurisdiccion
                    item.organoLegislativo = registro.organoLegislativo
                    item.palabrasClaves = registro.palabrasClaves
            return True
        return False

    def admin_borrar(self, registro, usuario):
        if usuario["rol"] == "admin" and isinstance(registro, Registro):
            for item in self.__baseDeDatos__:
                if item.nroRegistro == registro.nroRegistro:
                    self.__baseDeDatos__.remove(item)
                    return True
        return False