#IMPORTS
from BaseDeDatos import BaseDeDatos;
from Usuarios import Usuarios;
from Registro import Registro;
from funciones import formulario_registro




baseDeDatos = BaseDeDatos()
usuarios = Usuarios()

#INICIO
salir = False
continuar = False
while salir == False:
    print('')
    print('¡Bienvenido!')
    inicio = None
    while (inicio not in [1, 2, 3]):
        inicio = int(input('Ingrese una opcion: \n 1 - Loguearse \n 2 - Registrarse \n 3 - Salir \n'))
        
        if (inicio not in [1, 2, 3]):
            print('Valor incorrecto')
        elif inicio == 3:
            print('!Hasta pronto!')
            salir = True
            break
        elif inicio == 1:
             while True:
                print('')
                print('LOGIN')
                nombre = input('Ingrese su nombre: ')
                contraseña = input('Ingrese su contraseña: ')
                if usuarios.verificar_login(nombre, contraseña):
                    continuar = True
                    break
                else:
                    print('Usuario o contraseña inválidos')
                    break
        elif inicio == 2:
            #REGISTRO
            while True:
                print('REGISTRO')
                nombre = input('Ingrese su nombre: ')
                if usuarios.existe_usuario(nombre):
                    print('Ya existe el usuario ' + nombre)
                else:
                    contraseña = input('Ingrese su contraseña: ')
                    rol = int(input('Ingrese su rol (1 - usuario, 2 - administrador): '))
                    if rol not in [1, 2]:
                        print('Valor incorrecto')
                        break
                    elif rol == 1:
                        rol = "usuario"
                    elif rol == 2:
                        rol = "admin"
                    usuarios.registrarse(nombre, contraseña, rol)
                    print('Su registro fue exitoso.')
                    break
    
    if continuar == True:
        while salir == False:
            consulta = None
            while (consulta not in [1, 2, 3, 4, 5, 6]):
                print('')
                print('CONSULTAS')
                consulta = int(input('Elija una opción: \n 1 - Nro de ley \n 2 - palabra clave \n 3 - agregar un registro \n 4 - modificar un registro \n 5 - borrar un registro \n 6 - salir \n '))
                if (consulta not in [1, 2, 3, 4, 5, 6]):
                    print('Valor incorrecto')
                elif consulta == 6:
                    print('!Hasta pronto!')
                    salir = True
                    break
                elif consulta == 1:
                    ley = int(input('Ingrese un número de ley: '))
                    consultaPorLey = baseDeDatos.buscar_por_ley(ley)
                    
                    if consultaPorLey != False:
                        print('')
                        print("Nro ley: " + str(consultaPorLey[0]))
                        print("Fecha: " + str(consultaPorLey[1]))
                        print("Descripción: "+ consultaPorLey[2])
                        print("Tipo Categoría: " + consultaPorLey[3])
                        print("Jurisdicción: "+ consultaPorLey[4])
                        print("Órgano Legislativo: " + consultaPorLey[5])
                        print("Tipo Normativa: " + consultaPorLey[6])
                    else:
                        print('No hubo coincidencias')
                        break
                elif consulta == 2:
                    palabraClave = input('Ingrese una palabra clave: ')
                    consultaPorPalabraClave = baseDeDatos.buscar_por_palabra_clave(palabraClave)
                    if consultaPorPalabraClave != False:
                        for objeto in consultaPorPalabraClave:
                            print('')
                            print("Nro ley: " + str(objeto[0]))
                            print("Fecha: " + str(objeto[1]))
                            print("Descripción: "+ objeto[2])
                            print("Tipo Categoría: " + objeto[3])
                            print("Jurisdicción: "+ objeto[4])
                            print("Órgano Legislativo: " + objeto[5])
                            print("Tipo Normativa: " + objeto[6])
                    else: 
                        print('No hubo coincidencias')
                        break
                elif consulta == 3 or consulta == 4 or consulta == 5:
                    usuario = usuarios.buscar_usuario(nombre)
                    if usuario["rol"] != "admin":
                        print('No tiene permisos suficientes')
                        break
                if consulta == 3:
                    print('')
                    print('AGREGAR')
                    formulario = formulario_registro(usuario, baseDeDatos, None)
                if consulta == 4:
                    print('')
                    print('MODIFICAR')
                    error = False
                    while error == False:
                        nroRegistro = int(input('Ingrese el número de registro: '))
                        registro_existe = baseDeDatos.buscar_por_nroRegistro(nroRegistro)
                        if registro_existe == False:
                            error = True
                            print('No hubo coincidencias')
                            break
                        else:
                            formulario = formulario_registro(usuario, baseDeDatos, nroRegistro)
                            break
                if consulta == 5:
                    print('')
                    print('BORRAR')
                    error = False
                    while error == False:
                        nroRegistro = int(input('Ingrese el número de registro: '))
                        registro_existe = baseDeDatos.buscar_por_nroRegistro(nroRegistro)
                        if registro_existe == False:
                            error = True
                            print('No hubo coincidencias')
                            break
                        else:
                            baseDeDatos.admin_borrar(registro_existe, usuario) 
                            print('Se borró con éxito')    
                            break    
    if (salir == True):
        break