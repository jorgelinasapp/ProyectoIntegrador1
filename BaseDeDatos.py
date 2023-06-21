from Registro import Registro
import mysql.connector
from datetime import datetime


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
        query = """
                SELECT n.NroNormativa, n.Fecha, n.Descripcion, c.TipoCategoria, j.Jurisdiccion, o.OrganoLegislativo, t.TipoNormativa 
                FROM normativa n 
                JOIN categoria c ON c.id_categoria = n.id_Categoria 
                JOIN jurisdiccion j ON j.id_Jurisdiccion = n.id_Jurisdiccion 
                JOIN organolegislativo o ON o.id_OrganoLegislativo = n.id_OrganoLegislativo 
                JOIN tiponormativa t ON t.id_TipoNormativa = n.id_TipoNormativa 
                WHERE NroNormativa = %s;
                """
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
        query = """SELECT n.NroNormativa, n.Fecha, n.Descripcion, c.TipoCategoria, j.Jurisdiccion, o.OrganoLegislativo, t.TipoNormativa 
                FROM normativa n 
                JOIN categoria c ON c.id_categoria = n.id_Categoria 
                JOIN jurisdiccion j ON j.id_Jurisdiccion = n.id_Jurisdiccion 
                JOIN organolegislativo o ON o.id_OrganoLegislativo = n.id_OrganoLegislativo 
                JOIN tiponormativa t ON t.id_TipoNormativa = n.id_TipoNormativa 
                WHERE n.PalabrasClave LIKE %s ;
                """
        params = ('%' + palabraClave + '%',)
        self.mycursor.execute(query, params)
        result = self.mycursor.fetchall()
        if result:
            return result
        return False

        
    def admin_agregar(self, registro, usuario):
        if usuario["rol"] == "admin" and isinstance(registro, Registro):
            fecha_str = registro.fecha
            fecha = datetime.strptime(fecha_str, "%d/%m/%y")
            fecha_mysql = fecha.strftime("%Y-%m-%d")
            stringDePalabras = ', '.join(registro.palabrasClaves)
            
            query = '''
                    INSERT INTO normativa (NroNormativa, id_TipoNormativa, Fecha, Descripcion, id_Categoria, id_Jurisdiccion, id_OrganoLegislativo, PalabrasClave)
                    SELECT %s, t.id_TipoNormativa, %s, %s, c.id_Categoria, j.id_Jurisdiccion, o.id_OrganoLegislativo, %s
                    FROM categoria c
                    JOIN jurisdiccion j ON j.Jurisdiccion = %s
                    JOIN organolegislativo o ON o.OrganoLegislativo = %s
                    JOIN tiponormativa t ON t.TipoNormativa = %s
                    WHERE c.TipoCategoria = %s;
                    '''
            params = (registro.nroNormativa, registro.tipoNormativa, fecha_mysql, registro.descripcion, stringDePalabras, registro.jurisdiccion, registro.organoLegislativo, registro.tipoCategoria)
            self.mycursor.execute(query, params)
            self.mydb.commit()
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