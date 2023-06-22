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
        query = """
                SELECT *
                FROM normativa 
                WHERE id_Normativa = %s;
                """
        params = (nroRegistro,)
        self.mycursor.execute(query, params)
        result = self.mycursor.fetchone()
        if result:
            return result
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
                    SELECT %s, %s,  %s, %s, %s, %s, %s, %s                       
                    '''
            params = (registro.nroNormativa, registro.tipoNormativa, fecha_mysql, registro.descripcion, registro.tipoCategoria, registro.jurisdiccion, registro.organoLegislativo, stringDePalabras)
            self.mycursor.execute(query, params)
            self.mydb.commit()
            return True
        return False
    
    def admin_modificar(self, registro, usuario):
        if (usuario["rol"] == "admin" and isinstance(registro, Registro)):
            fecha_str = registro.fecha
            fecha = datetime.strptime(fecha_str, "%d/%m/%y")
            fecha_mysql = fecha.strftime("%Y-%m-%d")
            stringDePalabras = ', '.join(registro.palabrasClaves) 
            query = '''
                    UPDATE normativa 
                    SET NroNormativa = %s, id_TipoNormativa = %s, Fecha= %s, Descripcion= %s, id_Categoria= %s, id_Jurisdiccion= %s, id_OrganoLegislativo= %s, PalabrasClave= %s
                    WHERE id_Normativa = %s
                    '''
            params = (registro.nroNormativa, registro.tipoNormativa, fecha_mysql, registro.descripcion, registro.tipoCategoria, registro.jurisdiccion, registro.organoLegislativo, stringDePalabras, registro.nroRegistro )
            self.mycursor.execute(query, params)
            self.mydb.commit()
            return True
        return False

    def admin_borrar(self, nroRegistro):
        query = '''
                DELETE FROM normativa 
                WHERE id_Normativa = %s
                '''
        params = (nroRegistro,)
        self.mycursor.execute(query, params)
        self.mydb.commit()
        return True
