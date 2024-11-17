import random

dic_libros = {
    'ISB4578': {'Título': 'Don Quijote de la Mancha', 'Autor': 'Miguel de Cervantes', 'Año': 1605, 'Cantidad': 4, 'Género': [1, 4], 'Edad': 'Adultos'},
    'ISB9123': {'Título': 'Cien años de soledad', 'Autor': 'Gabriel García Márquez', 'Año': 1967, 'Cantidad': 6, 'Género': [2, 4], 'Edad': 'Adultos'},
    'ISB6384': {'Título': 'Orgullo y prejuicio', 'Autor': 'Jane Austen', 'Año': 1813, 'Cantidad': 3, 'Género': [3, 10], 'Edad': 'Adolescentes y Adultos'},
    'ISB2754': {'Título': 'Matar a un ruiseñor', 'Autor': 'Harper Lee', 'Año': 1960, 'Cantidad': 5, 'Género': [4, 10], 'Edad': 'Adolescentes y Adultos'},
    'ISB8301': {'Título': '1984', 'Autor': 'George Orwell', 'Año': 1949, 'Cantidad': 7, 'Género': [5, 4], 'Edad': 'Adultos'},
    'ISB4928': {'Título': 'El Principito', 'Autor': 'Antoine de Saint-Exupéry', 'Año': 1943, 'Cantidad': 10, 'Género': [6, 4], 'Edad': 'Todas las edades'},
    'ISB8475': {'Título': 'La Odisea', 'Autor': 'Homero', 'Año': 1614, 'Cantidad': 2, 'Género': [7, 1], 'Edad': 'Adultos'},
    'ISB1329': {'Título': 'Harry Potter y la piedra filosofal', 'Autor': 'J.K. Rowling', 'Año': 1997, 'Cantidad': 8, 'Género': [8], 'Edad': 'Infantil y Juvenil'},
    'ISB7561': {'Título': 'Crimen y castigo', 'Autor': 'Fiódor Dostoyevski', 'Año': 1866, 'Cantidad': 4, 'Género': [9, 10], 'Edad': 'Adultos'},
    'ISB3985': {'Título': 'En el camino', 'Autor': 'Jack Kerouac', 'Año': 1957, 'Cantidad': 5, 'Género': [10, 4], 'Edad': 'Adultos'}
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
                print("Listar usuarios")
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
                if opc == 1:
                    print("Listar usuarios por DNI")
                elif opc == 2:
                    print("Listar usuarios por nombre")
                elif opc == 3:
                    print("Listar usuarios por cantidad de libros prestados")
                elif opc == 4:
                    print("Listar usuarios por cantidad de libros leídos")
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
                    print("Buscar por nombre")
                elif opc == 2:
                    print("Buscar por edad")
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
                    print("Añadir usuario nuevo")
                elif opc == 2:
                    print("Modificar usuario existente")
                    flg023 = False
                    flg0232 = True
                elif opc == 3:
                    print("Eliminar usuario")
                elif opc == 4:
                    flg023 = False
                    flg02 = True  # Regresar al menú de gestión de usuarios

            # Sección de modificar usuario existente
            while flg0232:
                print(menu0232)
                opc = input("Opción: ")
                if not opc.isdigit():
                    print("La opción debe ser numérica.")
                elif int(opc) < 1 or int(opc) > 4:
                    print("Opción fuera de rango.")
                else:
                    opc = int(opc)
                    if opc == 1:
                        print("Editar datos personales")
                        flg0232 = False
                        flg02321 = True
                    elif opc == 2:
                        print("Editar préstamos")
                        flg0232 = False
                        menu02322 = True
                    elif opc == 3:
                        print("Añadir libro leído")
                    elif opc == 4:
                        flg0232 = False
                        flg023 = True  # Regresar al menú de editar usuarios
                while flg02321:
                    print(menu02321)
                    opc = input("Opción: ")
                    if not opc.isdigit():
                        print("La opción debe ser numérica.")
                    elif int(opc) < 1 or int(opc) > 3:
                        print("Opción fuera de rango.")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            print("Teléfono")
                        elif opc == 2:
                            print("Email")
                        elif opc == 3:
                            flg02321 = False
                            flg0232 = True

                while flg02322:
                    print(menu02322)
                    opc = input("Opción: ")
                    if not opc.isdigit():
                        print("La opción debe ser numérica.")
                    elif int(opc) < 1 or int(opc) > 3:
                        print("Opción fuera de rango.")
                    else:
                        opc = int(opc)
                        if opc == 1:
                            print("Añadir libro prestado")
                        elif opc == 2:
                            print("Eliminar libro prestado")
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
            if opc == 1:
                print("Listar todos los géneros")
            elif opc == 2:
                print("Añadir nuevo género")
            elif opc == 3:
                print("Editar género")
            elif opc == 4:
                print("Eliminar género")
            elif opc == 5:
                flg03 = False
                flg00 = True  # Regresar al menú principal
