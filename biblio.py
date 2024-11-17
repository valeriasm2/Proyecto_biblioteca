import random

dic_libros = {
    'ISB4578': {'Título': 'Don Quijote de la Mancha', 'Autor': 'Miguel de Cervantes', 'Año': 1605, 'Cantidad': 4,
                'Género': [1, 4, 7], 'Edad': 'Adultos'},
    'ISB9123': {'Título': 'Cien años de soledad', 'Autor': 'Gabriel García Márquez', 'Año': 1967, 'Cantidad': 6,
                'Género': [2, 4, 9], 'Edad': 'Adultos'},
    'ISB6384': {'Título': 'Orgullo y prejuicio', 'Autor': 'Jane Austen', 'Año': 1813, 'Cantidad': 3, 'Género': [3, 4, 9],
                'Edad': 'Adolescentes y Adultos'},
    'ISB2754': {'Título': 'Matar a un ruiseñor', 'Autor': 'Harper Lee', 'Año': 1960, 'Cantidad': 5, 'Género': [4, 9, 10],
                'Edad': 'Adolescentes y Adultos'},
    'ISB8301': {'Título': '1984', 'Autor': 'George Orwell', 'Año': 1949, 'Cantidad': 7, 'Género': [5, 4, 10],
                'Edad': 'Adultos'},
    'ISB4928': {'Título': 'El Principito', 'Autor': 'Antoine de Saint-Exupéry', 'Año': 1943, 'Cantidad': 10,
                'Género': [6, 7, 10], 'Edad': 'Todas las edades'},
    'ISB8475': {'Título': 'La Odisea', 'Autor': 'Homero', 'Año': 1614, 'Cantidad': 2, 'Género': [7, 1, 6],
                'Edad': 'Adultos'},
    'ISB1329': {'Título': 'Harry Potter y la piedra filosofal', 'Autor': 'J.K. Rowling', 'Año': 1997, 'Cantidad': 8,
                'Género': [8, 6], 'Edad': 'Infantil y Juvenil'},
    'ISB7561': {'Título': 'Crimen y castigo', 'Autor': 'Fiódor Dostoyevski', 'Año': 1866, 'Cantidad': 4,
                'Género': [9, 10], 'Edad': 'Adultos'},
    'ISB3985': {'Título': 'En el camino', 'Autor': 'Jack Kerouac', 'Año': 1957, 'Cantidad': 5, 'Género': [10, 4],
                'Edad': 'Adultos'}
}

dic_generos = {
    1: 'Aventura', 2: 'Realismo Mágico', 3: 'Romance', 4: 'Ficción', 5: 'Distopía', 6: 'Fantasía', 7: 'Épica',
    8: 'Fantasía', 9: 'Novela psicológica', 10: 'Novela'}

dic_users = {
    '12334236A': {
        'nombre': 'Juan Perez', 'edad': 24, 'tfn': 456454847, 'mail': 'juanperez@gmail.com',
        'prestamos': ['ISB4578', 'ISB9123', 'ISB6384', 'ISB8475'],
        'leidos': ['ISB4928', 'ISB8475', 'ISB8301', 'ISB2754', 'ISB7561']
    },
    '56789102D': {
        'nombre': 'Maria Garcia', 'edad': 12, 'tfn': 678901234, 'mail': 'marigarcia@gmail.com',
        'prestamos': ['ISB1329', 'ISB7561', 'ISB3985'],
        'leidos': ['ISB2754', 'ISB1329', 'ISB6384']
    },
    '56749108N': {
        'nombre': 'Pedro Martínez', 'edad': 5, 'tfn': 543216789, 'mail': 'pedromartinez@gmail.com',
        'prestamos': ['ISB4578', 'ISB9123', 'ISB3985', 'ISB8301', 'ISB7561'],
        'leidos': ['ISB4928', 'ISB2754', 'ISB6384', 'ISB7561', 'ISB9123', 'ISB1329']
    },
    '98765434F': {
        'nombre': 'Ana Martínez', 'edad': 30, 'tfn': 987654321, 'mail': 'anamartinez@gmail.com',
        'prestamos': ['ISB1329', 'ISB7561', 'ISB8475'],
        'leidos': ['ISB2754', 'ISB3985', 'ISB8301', 'ISB4578', 'ISB6384', 'ISB4928', 'ISB9123']
    }
}

# MENÚ PRINCIPAL
menu00 = " Menú principal ".center(40, "=") + "\n" + "1) Gestión de Libros" + "\n" + \
         "2) Gestión de Usuarios" + "\n" + "3) Gestión de Géneros" + "\n" + "4) Exit" + "\n"

# MENÚS DICCIONARIO LIBROS
menu01 = " Gestión de Libros ".center(40, "=") + "\n" + "1) Listar todos los libros" + "\n" + \
         "2) Buscar libro" + "\n" + "3) Editar libro" + "\n" + "4) Volver atrás"
menu012 = " Buscar libro ".center(40, "=") + "\n" + "1) Por título" + "\n" + "2) Por autor" + \
          "\n" + "3) Por género" + "\n" + "4) Volver atrás"
menu013 = " Editar libro ".center(40, "=") + "\n" + "1) Añadir nuevo libro" + "\n" + "2) Editar libro existente" + \
          "\n" + "3) Eliminar libro" + "\n" + "4) Volver atrás"
menu0132 = " Editar libro existente ".center(40, "=") + "\n" + "1) Editar título" + "\n" + "2) Editar Autor" + \
           "\n" + "3) Editar Género" + "\n" + "4) Volver atrás"

# MENÚS USUARIOS
menu02 = " Gestión de usuarios ".center(40, "=") + "\n" + "1) Listar usuarios" + "\n" + "2) Buscar usuarios" + \
         "\n" + "3) Editar usuarios" + "\n" + "4) Volver atrás"
menu021 = " Listar usuarios ".center(40, "=") + "\n" + "1) Por DNI" + "\n" + "2) Por nombre" + "\n" + \
          "3) Por cantidad de libros prestados" + "\n" + "4) Por cantidad de libros leídos" + "\n" + "5) Volver atrás"
menu022 = " Buscar usuarios ".center(40, "=") + "\n" + "1) Por nombre" + "\n" + "2) Por edad" + "\n" + "3) Volver atrás"
menu023 = " Editar usuarios ".center(40, "=") + "\n" + "1) Añadir usuario nuevo" + "\n" + "2) Modificar usuario existente" + \
          "\n" + "3) Eliminar usuario" + "\n" + "4) Volver atrás"
menu0232 = " Modificar usuario existente ".center(40, "=") + "\n" + "1) Editar datos personales" + "\n" + "2) Editar préstamos" + \
           "\n" + "3) Añadir libro leído" + "\n" + "4) Volver atrás"
menu02321 = " Editar datos personales ".center(40, "=") + "\n" + "1) Teléfono" + "\n" + "2) Email" + "\n" + "3) Volver atrás"
menu02322 = " Editar préstamos ".center(40, "=") + "\n" + "1) Añadir libro prestado" + "\n" + "2) Eliminar libro prestado" + \
            "\n" + "3) Volver atrás"

# MENÚS GÉNEROS
menu03 = " Gestión de géneros ".center(40, "=") + "\n" + "1) Listar todos los géneros" + "\n" + "2) Añadir nuevo género" + \
         "\n" + "3) Editar género" + "\n" + "4) Eliminar género" + "\n" + "5) Volver atrás"

# Inicialización de flgs
flg00 = True  # Menú principal
flg01 = False  # Gestión de Libros
flg02 = False  # Gestión de Usuarios
flg03 = False  # Gestión de Géneros
flg012 = False  # Buscar libro
flg013 = False  # Editar libro
flg0132 = False  # Editar libro existente
flg021 = False  # Listar usuarios
flg022 = False  # Buscar usuarios
flg023 = False  # Editar usuarios
flg0232 = False  # Modificar usuario existente
flg02321 = False  # Editar datos personales
flg02322 = False  # Editar datos prestamos

# Letras dni, para confirmar que el DNI del usuario es correcto
letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
#Separación para la cabecera
sep = " "
#Cabecera de la tabla de usuarios
cabecera_tabla_usuarios = "DNI".ljust(12) + "Nombre".ljust(30) + sep +"Edad".rjust(10) + "Mail".rjust(42) + "Telefóno".rjust(20) + "Prestamos".rjust(20) + "Leidos".rjust(20) + "\n" + "="*155

# Menú principal
while flg00:
    print(menu00)
    opc = input("Opción: ")
    if not opc.isdigit():
        print("La opción debe ser numérica.")
    elif int(opc) < 1 or int(opc) > 4:
        print("Opción fuera de rango.")
    else:
        opc = int(opc)
        if opc == 1:
            flg00 = False
            flg01 = True
        elif opc == 2:
            flg00 = False
            flg02 = True
        elif opc == 3:
            flg00 = False
            flg03 = True
        elif opc == 4:
            print("Saliendo del programa...")
            flg00 = False

    # Sección de gestión de libros
    while flg01:
        print(menu01)
        opc = input("Opción: ")
        if not opc.isdigit():
            print("La opción debe ser numérica.")
        elif int(opc) < 1 or int(opc) > 4:
            print("Opción fuera de rango.")
        else:
            opc = int(opc)
            datos =""
            if opc == 1:
                cabecera = ("\n" + "Listar todos los libros".center(153,"*") + "\n" + "Clave".ljust(10) + "Título".ljust(40) + "Autor".ljust(30) + "Año".ljust(8) +
                            "Cantidad".rjust(5) + " "*5 + "Género".ljust(30) + "Edad".ljust(15) + "\n" + "*"*153 + "\n")
                for clave, valor in dic_libros.items():
                    generos_str = ""

                    #Agregar cada género con una coma entre ellos
                    for i in range(len(valor["Género"])):
                        genero_id = valor["Género"][i]
                        if genero_id in dic_generos:
                            generos_str += dic_generos[genero_id]
                            if i < len(valor["Género"]) - 1:  #Si no es el último género
                                generos_str += ", "

                    datos += (clave.ljust(10) + valor["Título"].ljust(40) + valor["Autor"].ljust(30) + str(valor["Año"]).ljust(8) +
                              str(valor["Cantidad"]).rjust(8) + " "*5 + generos_str.ljust(30) + valor["Edad"]).ljust(15) + "\n"
                print(cabecera+datos)
                input("\nPresiona una tecla para continuar.")
            elif opc == 2:
                print("Buscar libro")
                flg01 = False
                flg012 = True
            elif opc == 3:
                print("Editar libro")
                flg01 = False
                flg013 = True
            elif opc == 4:
                flg01 = False
                flg00 = True  # Regresar al menú principal

        # Sección de buscar libro
        while flg012:
            print(menu012)
            opc = input("Opción: ")
            if not opc.isdigit():
                print("La opción debe ser numérica.")
            elif int(opc) < 1 or int(opc) > 4:
                print("Opción fuera de rango.")
            else:
                opc = int(opc)
                if opc == 1:
                    cabecera = ("\n" + "Buscar por título".center(153, "*") + "\n" + "Clave".ljust(
                        10) + "Título".ljust(40) + "Autor".ljust(30) + "Año".ljust(8) +
                                "Cantidad".rjust(5) + " " * 5 + "Género".ljust(30) + "Edad".ljust(
                                15) + "\n" + "*" * 153 + "\n")
                    datos = ""
                    titulo = input("\nTítulo para buscar: ").lower()

                    for clave,valor in dic_libros.items():
                        if titulo in valor["Título"].lower():
                            generos_str = ""
                            # Agregar cada género con una coma entre ellos
                            for i in range(len(valor["Género"])):
                                genero_id = valor["Género"][i]
                                if genero_id in dic_generos:
                                    generos_str += dic_generos[genero_id]
                                    if i < len(valor["Género"]) - 1:  # Si no es el último género
                                        generos_str += ", "

                            datos += (clave.ljust(10) + valor["Título"].ljust(40) + valor["Autor"].ljust(30) + str(valor["Año"]).ljust(8) +
                                      str(valor["Cantidad"]).rjust(8) + " " * 5 + generos_str.ljust(30) + valor["Edad"]).ljust(15) + "\n"

                    # Verificar si se encontraron libros
                    if datos:
                        print(cabecera+datos)
                    else:
                        print("\nNo hay ningún título que contenga {}".format(titulo))
                    input("\nPresiona una tecla para continuar.")

                elif opc == 2:
                    cabecera = ("\n" + "Buscar por autor".center(153, "*") + "\n" + "Clave".ljust(
                        10) + "Título".ljust(40) + "Autor".ljust(30) + "Año".ljust(8) +
                                "Cantidad".rjust(5) + " " * 5 + "Género".ljust(30) + "Edad".ljust(
                                15) + "\n" + "*" * 153 + "\n")
                    datos = ""
                    autor = input("\nAutor para buscar: ").lower()

                    for clave, valor in dic_libros.items():
                        if autor in valor["Autor"].lower():
                            generos_str = ""
                            # Agregar cada género con una coma entre ellos
                            for i in range(len(valor["Género"])):
                                genero_id = valor["Género"][i]
                                if genero_id in dic_generos:
                                    generos_str += dic_generos[genero_id]
                                    if i < len(valor["Género"]) - 1:  # Si no es el último género
                                        generos_str += ", "

                            datos += (clave.ljust(10) + valor["Título"].ljust(40) + valor["Autor"].ljust(30) + str(
                                valor["Año"]).ljust(8) +
                                      str(valor["Cantidad"]).rjust(8) + " " * 5 + generos_str.ljust(30) + valor[
                                          "Edad"]).ljust(15) + "\n"

                    # Verificar si se encontraron libros
                    if datos:
                        print(cabecera + datos)
                    else:
                        print("\nNo hay ningún autor que contenga {}".format(autor))
                    input("\nPresiona una tecla para continuar.")

                elif opc == 3:
                    cabecera = ("\n" + "Buscar por género".center(153, "*") + "\n" + "Clave".ljust(
                        10) + "Título".ljust(40) + "Autor".ljust(30) + "Año".ljust(8) +
                                "Cantidad".rjust(5) + " " * 5 + "Género".ljust(30) + "Edad".ljust(
                                15) + "\n" + "*" * 153 + "\n")
                    datos = ""
                    genero = input("\nGénero para buscar: ").lower()

                    for clave, valor in dic_libros.items():
                        generos_str = ""
                        # Agregar cada género con una coma entre ellos
                        for i in range(len(valor["Género"])):
                            genero_id = valor["Género"][i]
                            if genero_id in dic_generos:
                                generos_str += dic_generos[genero_id]
                                if i < len(valor["Género"]) - 1:  # Si no es el último género
                                    generos_str += ", "
                        if genero in generos_str.lower():
                            datos += (clave.ljust(10) + valor["Título"].ljust(40) + valor["Autor"].ljust(30) + str(
                                valor["Año"]).ljust(8) +
                                      str(valor["Cantidad"]).rjust(8) + " " * 5 + generos_str.ljust(30) + valor[
                                          "Edad"]).ljust(15) + "\n"

                    # Verificar si se encontraron libros
                    if datos:
                        print(cabecera + datos)
                    else:
                        print("\nNo hay ningún género que contenga {}".format(genero))
                    input("\nPresiona una tecla para continuar.")

                elif opc == 4:
                    flg012 = False
                    flg01 = True  # Regresar al menú de gestión de libros

        # Sección de editar libro
        while flg013:
            print(menu013)
            opc = input("Opción: ")
            if not opc.isdigit():
                print("La opción debe ser numérica.")
            elif int(opc) < 1 or int(opc) > 4:
                print("Opción fuera de rango.")
            else:
                opc = int(opc)
                if opc == 1:
                    print("Añadir nuevo libro")

                    #generamos un id de libro aleatorio
                    id_libro = ""
                    while True:
                        id_numero = random.randint(1000, 9999)
                        id_libro = "ISB{}".format(id_numero)
                        if id_libro not in dic_libros:
                            break

                    print("ID generado automáticamente: {}".format(id_libro))

                    #título del libro
                    print("Ingrese el título del libro:")
                    titulo = input()
                    while len(titulo) == 0:
                        print("El título no puede estar vacío.")
                        titulo = input()

                    #autor del libro
                    print("Ingrese el autor del libro:")
                    autor = input()
                    while len(autor) == 0:
                        print("El autor no puede estar vacío.")
                        autor = input()

                    #género del libro
                    print("Seleccione un género:")
                    for clave, valor in dic_generos.items():
                        print("{}. {}".format(clave,valor))
                    genero = None
                    while genero not in dic_generos:
                        genero_input = input()
                        if genero_input.isdigit():
                            genero = int(genero_input)
                            if genero not in dic_generos:
                                print("Opción de género inválida.")
                        else:
                            print("Debe ingresar un número válido.")

                    #año de publicación
                    print("Ingrese el año de publicación:")
                    year = input()
                    while not year.isdigit() or len(year) != 4 or int(year) < 1000 or int(year) > 9999:
                        print("El año debe ser un número de 4 dígitos válido.")
                        year = input()

                    #edad del libro
                    edades_disponibles = list(set([datos['Edad'] for datos in dic_libros.values()]))
                    print("Seleccione la edad recomendada para el libro:")
                    for i, edad in enumerate(edades_disponibles, 1):
                        print("{}. {}".format(i,edad))
                    edad_seleccionada = None
                    while edad_seleccionada not in edades_disponibles:
                        edad_input = input()
                        if edad_input.isdigit():
                            opcion_edad = int(edad_input)
                            if 1 <= opcion_edad <= len(edades_disponibles):
                                edad_seleccionada = edades_disponibles[opcion_edad - 1]
                            else:
                                print("Opción de edad inválida.")
                        else:
                            print("Debe ingresar un número válido.")

                    #cantidad de libros
                    print("Ingrese la cantidad de libros disponibles:")
                    cantidad = input()
                    while not cantidad.isdigit() or int(cantidad) <= 0:
                        print("La cantidad debe ser un número entero mayor a 0.")
                        cantidad = input()

                    #añadimos el nuevo libro al diccionario libros
                    dic_libros[id_libro] = {"Título": titulo, "Autor": autor, "Género": [genero], "Año": int(year), "Cantidad": int(cantidad), "Edad": edad_seleccionada}

                    print("Libro añadido exitosamente con ID {}:".format(id_libro))
                    print(dic_libros[id_libro])

                    print("Libro añadido correctamente. Regresando al menú principal.")


                elif opc == 2:
                    print("Editar libro existente")
                    flg013 = False
                    flg0132 = True
                elif opc == 3:
                    id_libro = input("Ingrese el ID del libro a eliminar:")
                    if id_libro in dic_libros:
                        #si el libro existe, se elimina
                        del dic_libros[id_libro]
                        print("El libro con ID {} ha sido eliminado exitosamente.".format(id_libro))
                    else:
                        #si el libro no existe:
                        print("No se encontró un libro con el ID {}.".format(id_libro))
                elif opc == 4:
                    flg013 = False
                    flg01 = True  # Regresar al menú de gestión de libros

            #editar libro existente
            while flg0132:
                print(menu0132)
                opc = input("Opción: ")
                if not opc.isdigit():
                    print("La opción debe ser numérica.")
                elif int(opc) < 1 or int(opc) > 4:
                    print("Opción fuera de rango.")
                else:
                    opc = int(opc)
                    #editar título
                    if opc == 1:
                        print("Ingrese el ID del libro a editar:")
                        id_libro = input().upper()
                        if id_libro not in dic_libros:
                            print("El ID no existe.")
                        else:
                            print("Ingrese el nuevo título:")
                            nuevo_titulo = input()
                            while len(nuevo_titulo) == 0:
                                print("El título no puede estar vacío.")
                                nuevo_titulo = input()
                            dic_libros[id_libro]["Título"] = nuevo_titulo
                            print("Título actualizado exitosamente.")

                    #editar autor
                    elif opc == 2:
                        print("Ingrese el ID del libro a editar:")
                        id_libro = input().upper()
                        if id_libro not in dic_libros:
                            print("El ID no existe.")
                        else:
                            print("Ingrese el nuevo autor:")
                            nuevo_autor = input()
                            while len(nuevo_autor) == 0:
                                print("El autor no puede estar vacío.")
                                nuevo_autor = input()
                            dic_libros[id_libro]["Autor"] = nuevo_autor
                            print("Autor actualizado exitosamente.")

                    #editar género
                    elif opc == 3:
                        print("Ingrese el ID del libro a editar:")
                        id_libro = input().upper()
                        if id_libro not in dic_libros:
                            print("El ID no existe.")
                        else:
                            print("Seleccione un género para el libro:")
                            for clave, valor in dic_generos.items():
                                print("{}. {}".format(clave, valor))
                            genero = None
                            while genero not in dic_generos:
                                genero_input = input()
                                if genero_input.isdigit():
                                    genero = int(genero_input)
                                    if genero not in dic_generos:
                                        print("Opción de género inválida.")
                                else:
                                    print("Debe ingresar un número válido.")
                            dic_libros[id_libro]["Género"] = [genero]
                            print("Género actualizado exitosamente.")

                    # Regresar al menú de editar libro
                    elif opc == 4:
                        flg0132 = False
                        flg013 = True  # Regresar al menú principal de gestión de libros

    # GESTIÓN USUARIOS
    while flg02:
        print(menu02)
        opc = input("Opción: ")
        if not opc.isdigit():
            print("La opción debe ser numérica.")
        elif int(opc) < 1 or int(opc) > 4:
            print("Opción fuera de rango.")
        else:
            opc = int(opc)
            if opc == 1:
                flg02 = False
                flg021 = True
            elif opc == 2:
                print("Buscar usuario")
                flg02 = False
                flg022 = True
            elif opc == 3:
                print("Editar usuario")
                flg02 = False
                flg023 = True
            elif opc == 4:
                flg02 = False
                flg00 = True  # Regresar al menú principal

        # Sección de listar usuarios
        while flg021:
            print(menu021)
            opc = input("Opción: ")
            if not opc.isdigit():
                print("La opción debe ser numérica.")
            elif int(opc) < 1 or int(opc) > 5:
                print("Opción fuera de rango.")
            else:
                opc = int(opc)
                if opc == 1: # Se lista usuarios por dni
                    print("=" * 155 + "\n" + "Listar usuarios por DNI".center(155)+"\n"+"=" * 155)
                    dnis = list(dic_users.keys()) # Se guardan los "ids" de los elementos del diccionario
                    datos = "" #variable que después se utilizará para imprimir los dnis ordenados
                    # Método burbuja para ordenar
                    for pasada in range (len(dnis)-1): # se resta uno al len de dnis, porque solamente se comprobará en este caso 3 veces, si añadiera más gente se sumaría más
                        for i in range (len(dnis)-pasada-1): # se resta la pasada (indice) del anterior bucle con la resta anterior, ya que las comprobaciones suman al indice y va restando la longitud, porque se van comprobando menos veces.
                            if dnis[i] > dnis[i+1]: #se compara el elemento anterior sea más grande que el siguiente elemento
                                dnis[i],dnis[i+1] = dnis[i+1],dnis[i] #en el caso que se cumpla lo anterior, se cambian la posición entre ellos para ordenar
                    print(cabecera_tabla_usuarios)
                    for dni in dnis: #para poder acceder a los elementos dentro del diccionario hago un for de la variable que contiene las keys.
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30)  + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) +str(dic_users[dni]["tfn"]).rjust(20)+ str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos) # se imprime la información de dentro del diccionario, con estilos


                elif opc == 2: # Se lista por nombre
                    print("=" * 155 + "\n" + "Listar usuarios por nombre".center(155)+"\n"+"=" * 155)
                    print(cabecera_tabla_usuarios)
                    datos = ""
                    dnis = list(dic_users.keys())
                    #Método burbuja para ordenar
                    for pasada in range(len(dnis) - 1):
                        for i in range(len(dnis) - pasada - 1):
                            if dic_users[dnis[i]]["nombre"] > dic_users[dnis[i + 1]]["nombre"]:
                                dic_users[dnis[i]], dic_users[dnis[i + 1]] = dic_users[dnis[i + 1]], dic_users[dnis[i]]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos)

                elif opc == 3: # Se lista por libros prestados
                    print("=" * 155 + "\n" + "Listar usuarios por cantidad de libros prestados".center(155) + "\n" + "=" * 155)
                    print(cabecera_tabla_usuarios)
                    datos = ""
                    dnis = list(dic_users.keys())
                    #Método burbuja
                    for pasada in range (len(dnis)-1):
                        for i in range (len(dnis)-pasada-1):
                            if len(dic_users[dnis[i]]["prestamos"]) < len(dic_users[dnis[i+1]]["prestamos"]):
                                dic_users[dnis[i + 1]]["prestamos"],dic_users[dnis[i]]["prestamos"] = dic_users[dnis[i]]["prestamos"],dic_users[dnis[i + 1]]["prestamos"]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos)
                elif opc == 4: #Se lista por la cantidad de libros leídos
                    print("=" * 155 + "\n" + "Listar usuarios por cantidad de libros leídos".center(155)+ "\n"+  "=" * 155)
                    print(cabecera_tabla_usuarios)
                    dnis = list(dic_users.keys())
                    datos = ""
                    for pasada in range (len(dnis)-1):
                        for i in range (len(dnis)-pasada-1):
                            if len(dic_users[dnis[i]]["leidos"]) < len(dic_users[dnis[i+1]]["leidos"]):
                                dic_users[dnis[i]]["leidos"], dic_users[dnis[i+1]]["leidos"] = dic_users[dnis[i+1]]["leidos"], dic_users[dnis[i]]["leidos"]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos)
                elif opc == 5:
                    flg021 = False
                    flg02 = True  # Regresar al menú de gestión de usuarios

        # Sección de buscar usuarios
        while flg022:
            print(menu022)
            opc = input("Opción: ")
            if not opc.isdigit():
                print("La opción debe ser numérica.")
            elif int(opc) < 1 or int(opc) > 3:
                print("Opción fuera de rango.")
            else:
                opc = int(opc)
                if opc == 1:
                    datos = "" # se inicia una variable donde más tarde se guardarán los datos para enseñarlos.
                    nombre = input("Inserta el nombre: ") #se pide que el usuario ponga una letra para encontrar el usuario que quiere (que el nombre contenga la letra)
                    while not nombre.isalpha(): # se mira lo que ha introducido el usuario sea una letra
                        print("Tiene que ser letras") # si no lo es, enseña este mensaje de error y vuelve a pedirle que inserte el texto
                        nombre = input("Inserta la nombre: ")
                    print("=" * 155 + "\n" + "Listar usuarios por cantidad de libros leídos".center(155)+"\n"+"=" * 155)
                    print(cabecera_tabla_usuarios)
                    dnis = list(dic_users.keys()) #se agrupa en una lista los "ids" de los elementos del diccionario.
                    for dni in dnis: #para sacar todos los elementos del diccionario se hace este bucle.
                        if dic_users[dni]["nombre"].lower().find(nombre.lower()) != -1: #se mira de que en el apartado nombre del diccionario,
                            # si se encuentra la letra que ha puesto el usuario. Si es diferente a -1 es que se ha encontrado la letra en algún usuario.
                            datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                                dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                                dic_users[dni]["tfn"]).rjust(20) + str(
                                len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                                20) + "\n"
                    print(datos) # se enseña los datos de la gente ordenada con estilos.
                elif opc == 2:
                    datos = ""
                    sep = ""
                    dnis = list(dic_users.keys()) # se agrupan todas las "ids" de los elementos dentro de una lista.
                    edad = input("Inserta el edad: ") #le decimos al usuario que inserte la edad del usuario que quiere buscar
                    while not edad.isdigit():# se comprueba de que lo que ha metido el usuario sea un número
                        print("Tiene que ser un digito") #si no lo es, enseñara este mensaje de error y nos volverá a preguntar la edad
                        edad = input("Inserta la edad: ")
                    edad = int(edad)
                    print("=" * 155 + "\n" + "Listar usuarios por cantidad de libros leídos".center(155) +"\n"+"="*155)
                    print(cabecera_tabla_usuarios)
                    for dni in dnis:
                        if str(dic_users[dni]["edad"]).find(str(edad)) != -1:
                            datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                                dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                                dic_users[dni]["tfn"]).rjust(20) + str(
                                len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                                20) + "\n"
                    print(datos)

                elif opc == 3:
                    flg022 = False
                    flg02 = True  # Regresar al menú de gestión de usuarios

        # Sección de editar usuarios
        while flg023:
            print(menu023)
            opc = input("Opción: ")
            if not opc.isdigit():
                print("La opción debe ser numérica.")
            elif int(opc) < 1 or int(opc) > 4:
                print("Opción fuera de rango.")
            else:
                opc = int(opc)
                if opc == 1:
                    print("=" * 155 + "\n" + "Añadir usuario nuevo".center(155) + "\n" + "=" * 155)
                    dni = input("Inserta tu dni: ").upper() #le pedimos a la persona que nos inserte el dni
                    comparacion = (int(dni[:-1]) % len(letras_dni)) #hace el calculo del (todas los números del dni) % 23
                    listado_dnis = list(dic_users.keys())

                    while not dni[:-1].isdigit() or len(dni) != 9 or not dni[-1:].isalpha() or letras_dni[comparacion].upper() != dni[-1:].upper() or dni in listado_dnis: #mira de que el len del dni sea igual a nueve, de que el
                        if not dni[:-1].isdigit(): #mira que todos los carácteres del dni menos el último sean números
                            print("El dni tine que contener números")
                        elif len(dni) != 9: # ultimo elemento sea una letra, y que la letra que le pone el usuario al dni sea la misma que en el calculo que acabamos de hacer
                            print("La longitud del dni no es correcta")
                        elif not dni[-1:].isalpha():
                            print("No has insertado una letra en el dni")
                        elif letras_dni[comparacion].upper() != dni[-1:].upper():
                            print("El dni no tiene la letra correcta, vuelve a insertarla")
                        elif dni in listado_dnis:
                            print("El dni ya ha sido asignado")
                        input("Enter para seguir")
                        dni = input("\nInserta tu dni: ").upper()
                        comparacion = (int(dni[:-1]) % len(letras_dni)) #recalcula el valor del dni, por si nos hemos equivocado

                    nombre = input("Inserta tu nombre: ") #le pide al usuario que se inserte el nombre
                    while not nombre.replace(" ","").isalpha(): #mira si hay espacios y los substituye y comprueba que el resto de la cadena son letras
                        print("El nombre solamente puede contener espacios o letras") #mensaje de error si hemos introducido algo que está mal
                        input("Enter para seguir")
                        nombre = input("\nInserta tu nombre: ")

                    edad = input("Inserta tu edad: ") #le pudo al usuario que inserte la edad
                    while not edad.isdigit() or int(edad) > 120: #comprueba que la edad sea un número y no sea mayor que 120
                        if not edad.isdigit(): #si no es un número
                            print("La edad debe de ser un número") #imprime este mensaje de error
                        elif int(edad) > 120: # si la edad es mayor a 120
                            print("Tienes que insertar tu edad real") #imprime este mensaje de error
                        input("Enter para seguir")
                        edad = input("\nInserta tu edad: ")

                    tfn = input("Inserta el telefóno: ") #le pide al usuario que inserte el telefóno.
                    while tfn.startswith("+") or len(tfn) != 9 or not tfn.isdigit(): #mira que el telefóno no empiece por un + (empezaria por prefijo),
                        #o si la longitud no es la correcta, o que el telefóno no sea un digito
                        if tfn.startswith("+"):
                            print("El telefóno tiene que ir sin prefijo")
                        elif len(tfn) != 9:
                            print("La longitud del telefóno no es correcto")
                        elif not tfn.isdigit():
                            print("El número de telefóno son digitos")
                        input("Enter para seguir")

                        tfn = input("Inserta el telefóno: ")
                    mail_correcto = False #iniciamos una flg para el mail.
                    while not mail_correcto:
                        mail = input("Inserta el mail: ")
                        user = mail[:mail.find("@")] #separamos el user del mail
                        dominio = mail[mail.find("@")+1:] #separamos el dominio del mail
                        if not user[0].isalpha(): #comprueba de que el user del mail tiene que empezar con una letra.
                            print("El correo tiene que empezar con letras")
                        elif not user[-1:].isalnum(): #comprueba del que el final del user (antes del @) sea diferente a una letra o un número.
                            print("Antes del @ no puede haber ningun caracter que no sea alfabetico o numerico")
                        elif not dominio[0].isalnum():#mira de que el dominio (después del @) sea una letra o un número.
                            print("Después del @ no puede haber ningun caracter que no sea alfabetico")
                        elif not dominio[-1:].isalpha(): #mira que el parte final del dominio (por ejemplo: es, com) el último elemento sea una letra.
                            print("El correo tiene que acabar con letras")
                        elif len(dominio[dominio.find("."):]) < 3 or len(dominio[dominio.find("."):]) > 4: #mira que en el dominio después del punto hayan 3 o 4 elementos más
                            #esto hace de la extensión del dominio sea de 2 o de 3 de longitud
                            print("La longitud del dominio tiene que ser entre 2 y 3 caracteres")

                        else:
                            mail_correcto = True #si está correcto la flag para de ejecutarse
                            break #hace un break para salir


                    datos = ""

                    print(155*"=" + "\n" + "Mostrar usuarios".center(155) + "\n" + 155*"=" + "\n"+ cabecera_tabla_usuarios)
                    dic_users.update({dni:{"nombre":nombre.title(),"edad":edad,"tfn":tfn,"mail":mail,"prestamos":[],"leidos":[]}})
                    dnis = list(dic_users.keys())
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos) # se muestan los datos por pantalla.

                elif opc == 2:
                    cabecera = "\n" + " Modificar Usuario Existente ".center(40, "=")
                    print(cabecera)
                    flg023 = False

                    # Inicializar la variable 'dni' antes de usarla
                    dni = input("Ingrese el DNI del usuario a modificar: ")
                    if dni not in dic_users:
                        print("El DNI no está registrado.")
                    else:
                        flg0232 = True
                elif opc == 3:
                    datos = "" #iniciamos la variable datos, para después ponerle toda la estructura de la tabla
                    print(155 * "=" + "\n" + "Eliminar usuario".center(
                        155) + "\n" + 155 * "=" + "\n" + cabecera_tabla_usuarios)
                    #se hace una tabla de mostración para que los usuarios puedan ver el dni que quieren eliminar.
                    dnis = list(dic_users.keys()) #se agrupan todas las ids de los elementos del diccionario en una lista.
                    for dni in dnis: # se pasa por toda la lista y saca los elementos enteros para mostrarlos bonitos
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos) # se muestan los datos por pantalla.
                    user_dni = input("Inserta el dni de la persona que quieres eliminar: ") # se pregunta que persona quieren eliminar
                    while not user_dni in dnis: #si el dni que pone no existe, significa que no está dentro del diccionario, es decir que no se puede eliminar.
                        print("No existe el usuario que quieres borrar")
                        user_dni = input("Inserta el dni de la persona que quieres eliminar: ")
                    del dic_users[user_dni] # se elimina el usuario

                    dnis = list(dic_users.keys()) # se vuelve hacer una lista, ya que si se elimina un elemento y lo listamos saldrá un error de que ya no existe y que no lo encuentra.
                    datos = "" #se reinicia datos para que no salga la misma tabla que anteriormente
                    #mostramos la tabla para enseñar los usuarios que quedan
                    print(155 * "=" + "\n" + "Eliminar usuario".center(
                        155) + "\n" + 155 * "=" + "\n" + cabecera_tabla_usuarios)
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(43) + str(
                            dic_users[dni]["tfn"]).rjust(20) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos)  # se muestan los datos por pantalla.
                    if datos == "": #si se han eliminado todos los usuarios
                        print("No quedan usuarios en la tabla")

                elif opc == 4:
                    flg023 = False
                    flg02 = True  # Regresar al menú de gestión de usuarios

            # Sección de Modificar Usuario Existente
            while flg0232:
                print(menu0232)
                opc = input("Opción: ")
                if not opc.isdigit() or not 1 <= int(opc) <= 4:
                    print("Opción fuera de rango.")
                else:
                    opc = int(opc)
                    # Editar datos personales
                    if opc == 1:
                        flg0232 = False
                        flg02321 = True
                    # Editar préstamos
                    elif opc == 2:
                        flg0232 = False
                        flg02322 = True

                    # Añadir libro leído
                    elif opc == 3:
                        cabecera = "\n" + " Añadir libro leído ".center(40, "=")
                        print(cabecera)
                        libro_leido = input("Añada el isbn del libro leído: ")
                        if libro_leido in dic_libros:
                            if libro_leido not in dic_users[dni]["leidos"]:
                                dic_users[dni]["leidos"].append(libro_leido)
                                print("Libro '{}' añadido a la lista de leídos.".format(libro_leido))
                        print("Press to continue...\n")
                    elif opc == 4:  # Volver atrás
                        flg0232 = False
                        flg023 = True  # Regresar al menú de gestión de usuarios

                # Submenú: Editar datos personales
                while flg02321:
                    print(menu02321)
                    opc = input("Opción: ")
                    if not opc.isdigit() or not 1 <= int(opc) <= 3:
                        print("Opción fuera de rango.")
                    else:
                        opc = int(opc)
                        # Editar teléfono
                        if opc == 1:
                            cabecera = "\n" + " Editar teléfono ".center(40, "=")
                            print(cabecera)
                            nuevo_tfn = input("Ingrese el nuevo número de teléfono (9 dígitos): ")
                            # Validación de que el teléfono tiene 9 dígitos y es numérico
                            if len(nuevo_tfn) == 9 and nuevo_tfn.isdigit():
                                dic_users[dni]["tfn"] = int(nuevo_tfn)
                                print("El teléfono ha sido cambiado correctamente.")
                            else:
                                print("El teléfono debe tener 9 dígitos numéricos.")
                            input("Presione Enter para continuar...\n")

                        # Editar email
                        elif opc == 2:
                            cabecera = "\n" + " Editar email ".center(40, "=")
                            print(cabecera)

                            nuevo_mail = input("Ingrese el nuevo correo electrónico: ")
                            mail_correcto = True

                            # Verificar si el correo contiene exactamente un '@'
                            ini = nuevo_mail.find("@")
                            if nuevo_mail.count("@") != 1 or ini == -1:
                                print("Correo inválido: debe contener un solo '@'.")
                                mail_correcto = False

                            if mail_correcto:
                                usuario = nuevo_mail[:ini]
                                dominio = nuevo_mail[ini + 1:]

                                # Validación de errores en la parte del usuario
                                if ".." in usuario or usuario[0] == "." or usuario[-1] == ".":
                                    print("Correo inválido: error en la parte del usuario.")
                                    mail_correcto = False

                                # Validación de errores en la parte del dominio
                                elif ".." in dominio or dominio[0] == "." or dominio[-1] == ".":
                                    print("Correo inválido: error en la parte del dominio.")
                                    mail_correcto = False
                                elif "." not in dominio:
                                    print("Correo inválido: dominio sin extensión.")
                                    mail_correcto = False

                            if mail_correcto:
                                dic_users[dni]["mail"] = nuevo_mail
                                print("Correo actualizado a:", nuevo_mail)
                            else:
                                input("Presione Enter para continuar...\n")

                        # Volver atrás
                        elif opc == 3:
                            flg02321 = False
                            flg0232 = True



                # Editar datos préstamos
                while flg02322:
                    print(menu02322)
                    opc = input("Opción: ")
                    if not opc.isdigit():
                        print("La opción debe ser numérica.")
                    elif int(opc) < 1 or int(opc) > 3:
                        print("Opción fuera de rango.")
                    else:
                        opc = int(opc)
                        # Añadir libro
                        if opc == 1:
                            cabecera = "\n" + " Añadir Libro ".center(40, "=")
                            print(cabecera)
                            libro_prestamos = input("Introduce el ISBN del libro préstamos: ")
                            if libro_prestamos in dic_libros:
                                if libro_prestamos not in dic_users[dni]["prestamos"]:
                                    dic_users[dni]["prestamos"].append(libro_prestamos)
                                    print("Libro añadido a la lista de préstamos.")
                                else:
                                    print("El libro ya existe en la lista.")
                                input("Presione Enter para continuar...\n")
                        # Eliminar libro
                        elif opc == 2:
                            libro_a_eliminar = input("Introduce el ISBN del libro a eliminar: ")
                            if libro_a_eliminar in dic_users[dni]["prestamos"]:
                                dic_users[dni]["prestamos"].remove(libro_a_eliminar)
                                print("Libro eliminado de la lista de préstamos.")
                            input("Presione Enter para continuar...\n")
                        elif opc == 3:
                            flg02322 = False
                            flg0232 = True

    # GESTIÓN DE GÉNEROS
    while flg03:
        print(menu03)
        opc = input("Opción: ")
        if not opc.isdigit():
            print("La opción debe ser numérica.")
        elif int(opc) < 1 or int(opc) > 5:
            print("Opción fuera de rango.")
        else:
            opc = int(opc)
            # Listar todos los géneros
            if opc == 1:
                cabecera = "\n" + " Listado de Géneros ".center(35, "=") + "\n" + "ID".ljust(15) + "Género".ljust(
                    20) + "\n" + "=" * 35
                print(cabecera)
                lista_generos = list(dic_generos.keys())
                for pasada in range(len(lista_generos) - 1):
                    for i in range(len(lista_generos) - 1 - pasada):
                        if lista_generos[i] > lista_generos[i + 1]:
                            lista_generos[i], lista_generos[i + 1] = lista_generos[i + 1], lista_generos[i]
                for id_genero in lista_generos:
                    datos = str(id_genero).ljust(15) + dic_generos[id_genero].ljust(20)
                    print(datos)
                input("Press to continue..." + "\n")

            # Añadir nuevo género
            elif opc == 2:
                cabecera = "\n" + " Añadir Nuevo Género ".center(40, "=")
                print(cabecera)
                nuevo_genero = input("Introduce el nombre del nuevo género: ")
                existe = False
                for clave, valor in dic_generos.items():
                    if valor == nuevo_genero:
                        existe = True
                        break
                if existe:
                    print("El género ya existe.")
                    input("Press to continue..." + "\n")
                else:
                    nuevo_id = len(dic_generos) + 1
                    dic_generos[nuevo_id] = nuevo_genero  # Añadir el nuevo género al diccionario
                    print("Género '{}' añadido correctamente con el ID {}.".format(nuevo_genero, nuevo_id))
                    input("Press to continue..." + "\n")

            # Editar género
            elif opc == 3:
                cabecera = "\n" + " Editar género ".center(40, "=")
                print(cabecera)
                id_genero = input("Introduce el ID del género a editar: ")

                # Convertir id_genero a entero para que coincida con las claves del diccionario
                if id_genero.isdigit():
                    id_genero = int(id_genero)
                    if id_genero in dic_generos:
                        nuevo_genero = input("Introduce el nuevo nombre del género: ")
                        dic_generos[id_genero] = nuevo_genero  # Editar el género en el diccionario
                        print("Género con ID {} editado correctamente.".format(id_genero))
                    else:
                        print("El ID ingresado no existe.")
                else:
                    print("El ID debe ser un número entero.")
                input("Press to continue..." + "\n")

            # Eliminar género
            elif opc == 4:
                cabecera = "\n" + " Eliminar género ".center(40, "=")
                print(cabecera)
                id_genero = input("Introduce el ID del género a eliminar: ")
                # Verificar que id_genero es un número
                if id_genero.isdigit():
                    id_genero = int(id_genero)
                    # Verificar si el ID existe en el diccionario de géneros
                    if id_genero in dic_generos:
                        print("¿Está seguro de eliminar el género con ID {}? (s/n)".format(id_genero))
                        confirmacion = input()
                        if confirmacion == 's':  # Confirmación para eliminar
                            del dic_generos[id_genero]
                            print("Género con ID {} eliminado correctamente.".format(id_genero))
                        elif confirmacion == 'n':  # Cancelar eliminación
                            print("El género no fue eliminado.")
                        else:
                            print("Opción inválida. Se esperaba 's' o 'n'.")
                    else:
                        print("El ID ingresado no existe.")
                else:
                    print("El ID debe ser un número entero.")
                input("Presione Enter para continuar...\n")

            elif opc == 5:
                flg03 = False
                flg00 = True  # Regresar al menú principal
