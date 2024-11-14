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
    '1233423S': {
        'nombre': 'Juan Perez', 'edad': 24, 'tfn': 456454847, 'mail': 'juanperez@gmail.com',
        'prestamos': ['ISB4578', 'ISB9123', 'ISB6384', 'ISB8475'],
        'leidos': ['ISB4928', 'ISB8475', 'ISB8301', 'ISB2754', 'ISB7561']
    },
    '5678910W': {
        'nombre': 'Maria Garcia', 'edad': 12, 'tfn': 678901234, 'mail': 'marigarcia@gmail.com',
        'prestamos': ['ISB1329', 'ISB7561', 'ISB3985'],
        'leidos': ['ISB2754', 'ISB1329', 'ISB6384']
    },
    '5674910K': {
        'nombre': 'Pedro Martínez', 'edad': 5, 'tfn': 543216789, 'mail': 'pedromartinez@gmail.com',
        'prestamos': ['ISB4578', 'ISB9123', 'ISB3985', 'ISB8301', 'ISB7561'],
        'leidos': ['ISB4928', 'ISB2754', 'ISB6384', 'ISB7561', 'ISB9123', 'ISB1329']
    },
    '9876543Z': {
        'nombre': 'Ana Martínez', 'edad': 30, 'tfn': 987654321, 'mail': 'anamartinez@gmail.com',
        'prestamos': ['ISB1329', 'ISB7561', 'ISB8475'],
        'leidos': ['ISB2754', 'ISB3985', 'ISB8301', 'ISB4578', 'ISB6384', 'ISB4928', 'ISB9123']
    }
}

# MENÚ PRINCIPAL
menu00 = " Menú principal ".center(40, "=") + "\n" + "1) Gestión de Libros" + "\n" + \
         "2) Gestión de Usuarios" + "\n" + "3) Gestión de Géneros" + "\n" + "4) Exit"

# MENÚS DICCIONARIO LIBROS
menu01 = " Gestión de Libros ".center(40, "=") + "\n" + "1) Listar todos los libros" + "\n" + \
         "2) Buscar libro" + "\n" + "3) Editar libro" + "\n" + "4) Volver atrás"
menu012 = " Buscar libro ".center(40, "=") + "\n" + "1) Por título" + "\n" + "2) Por autor" + \
          "\n" + "3) Por género" + "\n" + "4) Volver atrás"
menu013 = " Editar libro ".center(40, "=") + "\n" + "1) Añadir nuevo libro" + "\n" + "2) Editar libro existente" + \
          "\n" + "3) Eliminar libro" + "\n" + "4) Volver atrás"
menu0132 = " Editar libro existente ".center(40, "=") + "\n" + "1) Editar título" + "\n" + "2) Editar género" + \
           "\n" + "3) Volver atrás"

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
            if opc == 1:
                print("Listar todos los libros")
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
                    print("Buscar por título")
                elif opc == 2:
                    print("Buscar por autor")
                elif opc == 3:
                    print("Buscar por género")
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
                elif opc == 2:
                    print("Editar libro existente")
                    flg013 = False
                    flg0132 = True
                elif opc == 3:
                    print("Eliminar libro")
                elif opc == 4:
                    flg013 = False
                    flg01 = True  # Regresar al menú de gestión de libros

            # Sección de editar libro existente
            while flg0132:
                print(menu0132)
                opc = input("Opción: ")
                if not opc.isdigit():
                    print("La opción debe ser numérica.")
                elif int(opc) < 1 or int(opc) > 3:
                    print("Opción fuera de rango.")
                else:
                    opc = int(opc)
                    if opc == 1:
                        print("Editar título")
                    elif opc == 2:
                        print("Editar género")
                    elif opc == 3:
                        flg0132 = False
                        flg013 = True  # Regresar al menú de editar libro

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
                    print("=" * 123 + "\n" + "Listar usuarios por DNI".center(123))
                    dato = ""
                    libros_leidos = 0
                    libros_prestados = 0
                    dni_ordenado = []
                    print("=" * 123 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(
                        10) + "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(
                        15) + "Libros leídos".rjust(15) + "\n" + "=" * 123)
                    for clave, valor in dic_users.items():
                        if len(dni_ordenado) == 0:
                            dni_ordenado.append((clave, valor))
                        else:
                            insert_name = False
                            for i in range(len(dni_ordenado)):
                                tupla = dni_ordenado[i]
                                clave1 = tupla[0]
                                valor1 = tupla[1]
                                if clave < clave1:
                                    dni_ordenado.insert(i, (clave, valor))
                                    insert_name = True
                                    break
                            if not insert_name:
                                dni_ordenado.append((clave, valor))

                    for clave, valor in dni_ordenado:
                        for prestamos in valor["prestamos"]:
                            libros_prestados += 1
                        for leidos in valor["leidos"]:
                            libros_leidos += 1
                        dato += clave.ljust(15) + valor["nombre"].ljust(20) + str(valor["edad"]).ljust(
                            10) + str(valor["tfn"]).ljust(15) + \
                                valor["mail"].ljust(32) + str(libros_prestados).rjust(15) + str(
                            libros_leidos).rjust(15) + "\n"
                        libros_leidos = 0
                        libros_prestados = 0
                    print(dato)
                #listar por nombres
                elif opc == 2:
                    print("=" * 123 + "\n" + "Listar usuarios por nombre".center(123))
                    nombre_ordenado = []
                    libros_prestados = 0
                    libros_leidos = 0
                    dato = ""
                    print("=" * 123 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 123)
                    for clave, valor in dic_users.items():
                        if len(nombre_ordenado) == 0:
                            nombre_ordenado.append((clave, valor))
                        else:
                            insert_name = False
                            for l in range(len(nombre_ordenado)):
                                tupla = nombre_ordenado[l]
                                clave1 = tupla[0]
                                valor1 = tupla[1]
                                if valor["nombre"] < valor1["nombre"]:
                                    nombre_ordenado.insert(l, (clave, valor))
                                    insert_name = True
                                    break
                            if not insert_name:
                                nombre_ordenado.append((clave, valor))

                    for clave, valor in nombre_ordenado:
                        for prestamos in valor["prestamos"]:
                            libros_prestados += 1
                        for leidos in valor["leidos"]:
                            libros_leidos += 1
                        dato += clave.ljust(15) + valor["nombre"].ljust(20) + str(valor["edad"]).ljust(10) + str(
                            valor["tfn"]).ljust(15) + \
                                valor["mail"].ljust(32) + str(libros_prestados).rjust(15) + str(libros_leidos).rjust(
                            15) + "\n"
                        libros_leidos = 0
                        libros_prestados = 0
                    print(dato)
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

            # Iniciar con la opción de modificar usuario existente
            dni = input("Ingrese el DNI del usuario a modificar: ")
            if dni not in dic_users:
                print("El DNI no está registrado.")
            else:
                flg0232 = True

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
                        print("Editar datos personales")
                        flg0232 = False
                        flg02321 = True

                    # Editar préstamos
                    elif opc == 2:
                        print("Editar préstamos")
                        flg0232 = False
                        flg02322 = True

                    # Añadir libro leído
                    elif opc == 3:
                        libro_leido = input("Añada el isbn del libro leido: ")
                        if libro_leido in dic_libros:
                            if libro_leido not in dic_users[dni]["leidos"]:
                                dic_users[dni]["leidos"].append(libro_leido)
                                print("Libro añadido a la lista de leídos.")
                        # print(dic_users)
                    elif opc == 4:  # Volver atrás
                        flg0232 = False

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
                            nuevo_tfn = input("Ingrese el nuevo número de teléfono (9 dígitos): ")
                            if len(nuevo_tfn) == 9 and nuevo_tfn.isdigit():
                                dic_users[dni]["tfn"] = int(nuevo_tfn)
                                print("El teléfono ha sido cambiado correctamente.")
                                input("Press to continue..." + "\n")
                                # print(dic_users)
                            else:
                                print("El teléfono debe tener 9 dígitos numéricos.")
                                input("Press to continue..." + "\n")

                        # Editar email
                        elif opc == 2:
                            nuevo_mail = input("Ingrese el nuevo correo electrónico: ")
                            mail_correcto = True
                            # Verificar formato del correo
                            ini = nuevo_mail.find("@")
                            if nuevo_mail.count("@") != 1 or ini == -1:
                                print("Correo inválido: debe contener un solo '@'.")
                                input("Press to continue..." + "\n")
                                mail_correcto = False
                            else:
                                usuario = nuevo_mail[:ini]
                                dominio = nuevo_mail[ini + 1:]

                                # Validación de errores en la parte del usuario
                                if ".." in usuario or usuario[0] == "." or usuario[-1] == ".":
                                    print("Correo inválido: error en la parte del usuario.")
                                    input("Press to continue..." + "\n")
                                    mail_correcto = False

                                # Validación de errores en la parte del dominio
                                if ".." in dominio or dominio[0] == "." or dominio[-1] == ".":
                                    print("Correo inválido: error en la parte del dominio.")
                                    input("Press to continue..." + "\n")
                                    mail_correcto = False
                                elif "." not in dominio:
                                    print("Correo inválido: dominio sin extensión.")
                                    input("Press to continue..." + "\n")
                                    mail_correcto = False

                            if mail_correcto:
                                dic_users[dni]["mail"] = nuevo_mail
                                print("Correo actualizado a:", nuevo_mail)
                                input("Press to continue..." + "\n")
                        # Volver atrás
                        elif opc == 3:
                            flg02321 = False
                            flg0232 = True

                # Editar datos prestamos
                while flg02322:
                    print(menu02322)
                    opc = input("Opción: ")
                    if not opc.isdigit():
                        print("La opción debe ser numérica.")
                    elif int(opc) < 1 or int(opc) > 3:
                        print("Opción fuera de rango.")
                    else:
                        opc = int(opc)
                        # añadir libro
                        if opc == 1:
                            libro_prestamos = input("Introduce el isbn del libro prestamos: ")
                            if libro_prestamos in dic_libros:
                                if libro_prestamos not in dic_users[dni]["prestamos"]:
                                    dic_users[dni]["prestamos"].append(libro_prestamos)
                                    print("Libro añadido a la lista de prestamos.")
                                else:
                                    print("El libro ya existe en la lista.")
                                    input("Press to continue..." + "\n")

                            # print(dic_users)
                        # elimiinar libro
                        elif opc == 2:
                            libro_a_eliminar = input("Introduce el isbn del libro a eliminar: ")
                            if libro_a_eliminar in dic_users[dni]["prestamos"]:
                                dic_users[dni]["prestamos"].remove(libro_a_eliminar)
                                print("Libro eliminado de la lista de prestamos.")
                                input("Press to continue..." + "\n")
                            # print(dic_users)
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
                cabecera = "\n" + " Listado de Géneros ".center(35, "=") + "\n" + "ID".ljust(15) + "Género".ljust(20) + "\n" + "=" * 35
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
                cabecera = "\n" + " Añadir Nuevo Género ".center(40, "*")
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
                    print("Género '{}' añadido correctamente con el ID {}.".format(nuevo_genero , nuevo_id))
                    input("Press to continue..." + "\n")

            # Editar género
            elif opc == 3:
                cabecera = "\n" + " Editar género ".center(40, "*")
                print(cabecera)
                id_genero = input("Introduce el ID del género a editar: ")
                if id_genero in dic_generos:
                    nuevo_genero = input("Introduce el nuevo nombre del género: ")
                    dic_generos[id_genero] = nuevo_genero
                    print("Género '{}' editado correctamente.".format(nuevo_genero))
                    input("Press to continue..." + "\n")

            # Eliminar género
            elif opc == 4:
                print("Eliminar género")
                id_genero = input("Introduce el ID del género a eliminar: ")
                if id_genero in dic_generos:
                    print("¿Está seguro de eliminar el género con ID {}? (s/n)".format(id_genero))
                    del dic_generos[id_genero]
                    print("Género con ID {} eliminado correctamente.".format(id_genero))
                    input("Press to continue..." + "\n")

            elif opc == 5:
                flg03 = False
                flg00 = True  # Regresar al menú principal
