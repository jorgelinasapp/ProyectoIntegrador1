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
   