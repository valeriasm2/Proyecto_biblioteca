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

dic_users = {'12334236S':{'nombre':'Juan Perez', 'edad':24, 'tfn':456454847, 'mail':'juanperez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB6384'], 'leidos':['ISB4928', 'ISB8475']},
             '56789102W':{'nombre':'Maria Garcia', 'edad':12, 'tfn':678901234, 'mail':'marigarcia@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB3985'], 'leidos':['ISB2754', 'ISB1329']},
             '12345678A':{'nombre':'Pedro Martínez', 'edad':5, 'tfn':543216789, 'mail':'pedromartinez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB8301'], 'leidos':['ISB4928']},
             '98765432Z':{'nombre':'Ana Martínez', 'edad':30, 'tfn':987654321, 'mail':'anamartinez@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB8475'], 'leidos':['ISB2754','ISB3985','ISB8301']}
             }

letras_dni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

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
                    print("=" * 125 + "\n" + "Listar usuarios por DNI".center(125)+"\n"+"=" * 125)
                    dnis = list(dic_users.keys())
                    datos = ""
                    sep = " "
                    for pasada in range (len(dnis)-1):
                        for i in range (len(dnis)-pasada-1):
                            if dnis[i] > dnis[i+1]:
                                dnis[i],dnis[i+1] = dnis[i+1],dnis[i]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + sep + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(
                            len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                            20) + "\n"
                    print(datos)
                    # dic_users = {'1233423S': {'nombre': 'Juan Perez', 'edad': 24, 'tfn': 456454847,
                    #                           'mail': 'juanperez@gmail.com',
                    #                           'prestamos': ['ISB4578', 'ISB9123', 'ISB6384'],
                    #                           'leidos': ['ISB4928', 'ISB8475']},
                    #              }


                elif opc == 2:
                    print("=" * 125 + "\n" + "Listar usuarios por nombre".center(125)+"\n"+"=" * 125)
                    print("=" * 125 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 125)

                    datos = ""
                    dnis = list(dic_users.keys())
                    sep = " "

                    for pasada in range(len(dnis) - 1):
                        for i in range(len(dnis) - pasada - 1):
                            if dic_users[dnis[i]]["nombre"] > dic_users[dnis[i + 1]]["nombre"]:
                                dic_users[dnis[i]], dic_users[dnis[i + 1]] = dic_users[dnis[i + 1]], dic_users[dnis[i]]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) +sep+ str(dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(20) + "\n"
                    print(datos)

                elif opc == 3:
                    print("=" * 125 + "\n" + "Listar usuarios por cantidad de libros prestados".center(125) + "\n" + "=" * 125)
                    print("=" * 125 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 125)

                    datos = ""
                    sep = ""
                    dnis = list(dic_users.keys())
                    for pasada in range (len(dnis)-1):
                        for i in range (len(dnis)-pasada-1):
                            if len(dic_users[dnis[i]]["prestamos"]) > len(dic_users[dnis[i+1]]["prestamos"]):
                                dic_users[dnis[i + 1]]["prestamos"],dic_users[dnis[i]]["prestamos"] = dic_users[dnis[i]]["prestamos"],dic_users[dnis[i + 1]]["prestamos"]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) +sep+ str(dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(20) + "\n"
                    print(datos)

                elif opc == 4:
                    print("=" * 125 + "\n" + "Listar usuarios por cantidad de libros leídos".center(125))
                    print("=" * 125 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 125)

                    dnis = list(dic_users.keys())
                    datos = ""
                    sep = ""
                    for pasada in range (len(dnis)-1):
                        for i in range (len(dnis)-pasada-1):
                            if len(dic_users[dnis[i]]["leidos"]) < len(dic_users[dnis[i+1]]["leidos"]):
                                dic_users[dnis[i]]["leidos"], dic_users[dnis[i+1]]["leidos"] = dic_users[dnis[i+1]]["leidos"], dic_users[dnis[i]]["leidos"]
                    for dni in dnis:
                        datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + sep + str(
                            dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(
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
                    datos = ""
                    nombre = input("Inserta el nombre: ")
                    while not nombre.isalpha():
                        print("Tiene que ser un digito")
                        nombre = input("Inserta la nombre: ")
                    sep = ""
                    print("=" * 125 + "\n" + "Listar usuarios por cantidad de libros leídos".center(125))
                    print("=" * 125 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 125)
                    dnis = list(dic_users.keys())
                    for dni in dnis:
                        if dic_users[dni]["nombre"].lower().find(nombre.lower()) != -1:
                                datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + sep + str(
                                    dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(
                                    len(dic_users[dni]["prestamos"])).rjust(20) + str(len(dic_users[dni]["leidos"])).rjust(
                                    20) + "\n"
                    print(datos)



                elif opc == 2:
                    dato = ""
                    edad = input("Inserta el edad: ")

                    while not edad.isdigit():
                        print("Tiene que ser un digito")
                        edad = input("Inserta la edad: ")
                    edad = int(edad)
                    print("=" * 125 + "\n" + "Listar usuarios por cantidad de libros leídos".center(125))
                    print("=" * 125 + "\n" + "DNI".ljust(15) + "Nombre".ljust(20) + "Edad".ljust(10) + \
                          "Telefóno".ljust(15) + "Mail".ljust(32) + "Libros prestados".rjust(15) + \
                          "Libros leídos".rjust(15) + "\n" + "=" * 125)
                    datos = ""
                    sep = ""
                    dnis = list(dic_users.keys())
                    for dni in dnis:
                        if str(dic_users[dni]["edad"]).find(str(edad)) != -1:
                            datos += dni.ljust(12) + dic_users[dni]["nombre"].ljust(30) + sep + str(
                                dic_users[dni]["edad"]).rjust(10) + dic_users[dni]["mail"].rjust(32) + str(
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
                    print("Añadir usuario nuevo")
                    letra_encontrada = ""
                    dni = input("Inserta tu dni: ")
                    while not dni[:-1].isdigit():
                        print("El dni tine que contener números")
                        dni = input("Inserta tu dni: ")
                    comparacion = int(dni[:-1]) % len(letras_dni)
                    for i in range (len(letras_dni)):
                        if i == comparacion:
                            letra_encontrada = letras_dni[i]

                    while len(dni) != 9 or not dni[-1:].isalpha() or letra_encontrada.upper() != dni[-1:].upper():
                        if len(dni) != 9:
                            print("La longitud del dni no es correcta")
                        elif not dni[-1:].isalpha():
                            print("No has insertado una letra en el dni")
                        elif letra_encontrada.upper() != dni[-1:].upper():
                            print("El dni no tiene la letra correcta, vuelve a insertarla")
                        input("Enter para seguir")
                        dni = input("\nInserta tu dni: ")

                    nombre = input("Inserta tu nombre: ")
                    while not nombre.replace(" ","").isalpha():
                        print("El nombre solamente puede contener espacios o letras")
                        input("Enter para seguir")
                        nombre = input("\nInserta tu nombre: ")
                    edad = input("Inserta tu edad: ")
                    while not edad.isdigit() or int(edad) > 120:
                        if not edad.isdigit():
                            print("La edad debe de ser un número")
                        elif int(edad) > 120:
                            print("Inserta tu edad")
                        input("Enter para seguir")
                        edad = input("\nInserta tu edad: ")
                    tfn = input("Inserta el telefóno: ")
                    while tfn.startswith("+") or len(tfn) != 9:
                        if tfn.startswith("+"):
                            print("El telefóno tiene que ir sin prefijo")
                        elif len(tfn) != 9:
                            print("La longitud del telefóno no es correcto")
                        input("Enter para seguir")
                        tfn = input("Inserta el telefóno: ")
                    mail = input("Inserta el mail: ")

                    user = mail[:mail.find("@")]
                    dominio = mail[mail.find("@"):]
                    mail_correcto = False
                    print("user",user,"dominio",dominio)
                    print(user[-1:])
                    while not mail_correcto:
                        if not user[0].isalpha():
                            print("El correo tiene que empezar con letras")
                        elif not user[-1:].isalpha() and not user[-1:].isdigit():
                            print("Antes del @ no puede haber ningun caracter que no sea alfabetico o numerico")
                        elif not dominio[:-1].isalpha() and dominio[:-1].isdigit():
                            print("Después del @ no puede haber ningun caracter que no sea alfabetico")
                        elif not dominio[-1:].isalpha():
                            print("El correo tiene que acabar con letras")
                        elif len(dominio[dominio.find("."):]) < 3 or len(dominio[dominio.find("."):]) > 4:
                            print(len(dominio[dominio.find("."):]))
                            print("La longitud del dominio tiene que ser entre 2 y 3 caracteres")
                        else:
                            mail_correcto = True
                            break

                        input("Enter para seguir")
                        mail = input("Inserta el mail: ")



                    dic_users.update({dni:{"nombre":nombre,"edad":edad,"tfn":tfn,"mail":mail,"prestamos":[],"leidos":[]}})
                    print(dic_users)

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
