class Usuarios:
    def __init__(self):
        self.__usuarios__ = []

    def existe_usuario(self, nombre):
        for usuario in self.__usuarios__:
            if usuario['nombre'] == nombre:
                return True
        return False

    def verificar_login(self, nombre, contraseña):
        for usuario in self.__usuarios__:
            if usuario['nombre'] == nombre and usuario['contraseña'] == contraseña:
                return True
        return False

    def registrarse(self, nombre, contraseña, rol):
        usuario = {
            'nombre': nombre,
            'contraseña': contraseña,
            'rol': rol
        }
        self.__usuarios__.append(usuario)