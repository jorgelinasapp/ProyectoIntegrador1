from Registro import Registro
import mysql.connector


class BaseDeDatos:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="proyectoFinal"
        )
        self.mycursor = self.mydb.cursor()

    def buscar_por_ley(self, ley):
        query = "SELECT n.NroNormativa, n.Fecha, n.Descripcion, c.TipoCategoria FROM normativa n JOIN categoria c ON c.id_categoria = n.id_Categoria WHERE n.NroNormativa = %s ;"
        params = (ley,)
        self.mycursor.execute(query, params)
        result = self.mycursor.fetchone()
        if result:
            return result
        return False

    def buscar_por_nroRegistro(self, nroRegistro):
        for registro in self.__baseDeDatos__:
            if (registro.nroRegistro == nroRegistro):
                return registro
        return False
    
    def buscar_por_palabra_clave(self, palabraClave):
        query = "SELECT n.NroNormativa, n.Fecha, n.Descripcion, c.TipoCategoria FROM normativa n JOIN categoria c ON c.id_categoria = n.id_Categoria WHERE n.PalabrasClave LIKE %s ;"
        params = ('%' + palabraClave + '%',)
        self.mycursor.execute(query, params)
        result = self.mycursor.fetchall()
        if result:
            return result
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