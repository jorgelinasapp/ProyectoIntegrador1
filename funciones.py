from Registro import Registro

def formulario_registro(usuario, baseDeDatos, nroRegistro):
    error = False
    while error == False:
        tipoNormativa = int(input('Tipo Normativa \n Ingrese una de las siguientes opciones: \n 1 - ley \n 2 - decreto \n 3 - resolución \n'))
        if tipoNormativa not in [1, 2, 3]:
            print('Valor incorrecto')
            error = True
            break
        nroNormativa = int(input('Ingrese el número de normativa: '))
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        descripcion = input('Ingrese una descripción: ')
        categoria = int(input('Categoría \n Ingrese una de las siguientes opciones: \n 1 - laboral \n 2 - penal \n 3 - civil \n 4 - comercial \n 5 - familia y sucesiones \n 6 - agrario y ambiental \n 7 - minería \n 8 - derecho informático \n'))
        if categoria not in [1,2,3,4,5,6,7,8]:
            print('Valor incorrecto')
            error = True
            break
        jurisdiccion = int(input('Jurisdicción \n Seleccione una opción: \n 1 - Nacional \n 2 - Provincial \n'))
        if jurisdiccion not in [1,2]:
            print('Valor incorrecto')
            error = True
            break
        elif jurisdiccion == 1:
            organoLegislativo = 1
        elif jurisdiccion == 2:
            organoLegislativo = 2
        finPalabrasClaves = False
        while finPalabrasClaves == False:
            palabrasClaves = []
            palabrasClaves.append(input("Ingrese una palabra clave: "))
            opcion = None
            while opcion not in [1, 2]:
                opcion = int(input('¿Desea ingresar otra palabra clave? \n 1 - Si \n 2 - No \n'))
                if opcion == 1:
                    continue
                elif opcion == 2:
                    finPalabrasClaves = True
                    break
                else:
                    print('Valor incorrecto')
        if error == True:
            return False
        if nroRegistro == None:
            nuevoRegistro = Registro()
            nuevoRegistro.crear_registro(tipoNormativa, nroNormativa, fecha, descripcion, categoria, jurisdiccion, organoLegislativo, palabrasClaves)
            baseDeDatos.admin_agregar(nuevoRegistro, usuario)
            print('Se ha agregado con éxito \n')
            print('')
            print(baseDeDatos.buscar_por_ley(nroNormativa))
            print('')
            break
        else:
            registroExistente = Registro()
            registroExistente.modificar_registro(nroRegistro, tipoNormativa, nroNormativa, fecha, descripcion, categoria, jurisdiccion, organoLegislativo, palabrasClaves)
            baseDeDatos.admin_modificar(registroExistente, usuario)
            print('Se ha modificado con éxito')
            print('')
            for clave, valor in registroExistente.imprimir():
                print(clave, ":", valor)
            print('')
            break