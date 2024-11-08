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

dic_users = {'1233423S':{'nombre':'Juan Perez', 'edad':24, 'tfn':456454847, 'mail':'juanperez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB6384', 'ISB8475'], 'leidos':['ISB4928', 'ISB8475', 'ISB8301']},
             '5678910W':{'nombre':'Maria Garcia', 'edad':12, 'tfn':678901234, 'mail':'marigarcia@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB3985'], 'leidos':['ISB2754', 'ISB1329']},
             '12345678A':{'nombre':'Pedro Martínez', 'edad':5, 'tfn':543216789, 'mail':'pedromartinez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB3985', 'ISB8301' , 'ISB7561'], 'leidos':['ISB4928', 'ISB2754', 'ISB6384']},
             '98765432Z':{'nombre':'Ana Martínez', 'edad':30, 'tfn':987654321, 'mail':'anamartinez@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB8475'], 'leidos':['ISB2754','ISB3985','ISB8301']}
             }


menu0232 = " Modificar usuario existente ".center(40, "=") + "\n" + "1) Editar datos personales" + "\n" + "2) Editar préstamos" + \
           "\n" + "3) Añadir libro leído" + "\n" + "4) Volver atrás"

menu02321 = " Editar datos personales ".center(40, "=") + "\n" + "1) Teléfono" + "\n" + "2) Email" + "\n" + "3) Volver atrás"

menu02322 = " Editar préstamos ".center(40, "=") + "\n" + "1) Añadir libro prestado" + "\n" + "2) Eliminar libro prestado" + \
            "\n" + "3) Volver atrás"

# MENÚS GÉNEROS
menu03 = " Gestión de géneros ".center(40, "=") + "\n" + "1) Listar todos los géneros" + "\n" + "2) Añadir nuevo género" + \
         "\n" + "3) Editar género" + "\n" + "4) Eliminar género" + "\n" + "5) Volver atrás"

flg03 = False  # Gestión de Géneros
flg0232 = False  # Modificar usuario existente
flg02321 = False  # Editar datos personales
flg02322 = False  # Editar datos prestamos


# Sección de modificar usuario existente
while flg0232: # Modificar usuario existente
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

        # Editar datos personales
    while flg02321:
        print(menu02321)
        opc = input("Opción: ")
        if not opc.isdigit():
            print("La opción debe ser numérica.")
        elif int(opc) < 1 or int(opc) > 3:
            print("Opción fuera de rango.")
        else:
            if opc == 1:  # Editar teléfono
                nuevo_tfn = input("¿Qué número quieres cambiar? : ")
                # Validar que el número de teléfono tenga 9 dígitos
                if len(nuevo_tfn) == 9 and nuevo_tfn.isdigit():
                    dic_users[dni]["tfn"] = int(nuevo_tfn)
                    print("El teléfono ha sido cambiado correctamente.")
                else:
                    print("El teléfono debe tener 9 dígitos.")

            elif opc == 2: # Editar email
                nuevo_mail = input("¿Qué correo quieres cambiar? : ")
                mail_correcto = True
                # Comprobamos si el correo tiene un '@'
                user = nuevo_mail.find("@")
                if nuevo_mail.count("@") != 1 or user == -1:
                    print("El correo {} es incorrecto (debe tener exactamente un '@').".format(nuevo_mail))
                    mail_correcto = False
                else:
                    # Extraer la parte del usuario y la del dominio
                    usuario = nuevo_mail[0:user]
                    dominio = nuevo_mail[user + 1:]

                    # Verificar que el usuario no tenga puntos consecutivos o que empiece/termine con un punto
                    if ".." in usuario or usuario.startswith(".") or usuario.endswith("."):
                        print("El correo {} es incorrecto (problema en la parte del usuario).".format(nuevo_mail))
                        mail_correcto = False

                    # Verificar que el dominio no tenga puntos consecutivos, que empiece o termine con un punto
                    if ".." in dominio or dominio.startswith(".") or dominio.endswith("."):
                        print("El correo {} es incorrecto (problema en la parte del dominio).".format(nuevo_mail))
                        mail_correcto = False
                    else:
                        # Verificar que el dominio tenga al menos un punto
                        dom = dominio.find(".")
                        if dom == -1:
                            print("El correo {} es incorrecto (dominio sin extensión).".format(nuevo_mail))
                            mail_correcto = False

                # Si el correo es válido, lo asignamos al usuario
                if mail_correcto:
                    dic_users[dni]["mail"] = nuevo_mail
                    print("El correo electrónico ha sido cambiado a: {}".format(nuevo_mail))

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
