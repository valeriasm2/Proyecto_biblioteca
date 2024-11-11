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
             '5674910K':{'nombre':'Pedro Martínez', 'edad':5, 'tfn':543216789, 'mail':'pedromartinez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB3985', 'ISB8301' , 'ISB7561'], 'leidos':['ISB4928', 'ISB2754', 'ISB6384']},
             '98765432Z':{'nombre':'Ana Martínez', 'edad':30, 'tfn':987654321, 'mail':'anamartinez@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB8475'], 'leidos':['ISB2754','ISB3985','ISB8301']}
             }

# Menús de usuario y géneros
menu0232 = " Modificar usuario existente ".center(40, "=") + "\n" + \
           "1) Editar datos personales" + "\n" + "2) Editar préstamos" + \
           "\n" + "3) Añadir libro leído" + "\n" + "4) Volver atrás"

menu02321 = " Editar datos personales ".center(40, "=") + "\n" + \
            "1) Teléfono" + "\n" + "2) Email" + "\n" + "3) Volver atrás"

menu02322 = " Editar préstamos ".center(40, "=") + "\n" + \
            "1) Añadir libro prestamos" + "\n" + "2) Eliminar libro prestamos" + \
            "\n" + "3) Volver atrás"

menu03 = " Gestión de géneros ".center(40, "=") + "\n" + \
         "1) Listar todos los géneros" + "\n" + "2) Añadir nuevo género" + \
         "\n" + "3) Editar género" + "\n" + "4) Eliminar género" + "\n" + \
         "5) Volver atrás"

# Variables de control
flg0232 = False  # Modificar usuario existente
flg02321 = False  # Editar datos personales
flg02322 = False  # Editar préstamos
flg03 = False  # Gestión de géneros

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
            if libro_leido in dic_libros    :
                if libro_leido not in dic_users[dni]["leidos"]:
                    dic_users[dni]["leidos"].append(libro_leido)
                    print("Libro añadido a la lista de leídos.")
            #print(dic_users)

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
                    #print(dic_users)
                else:
                    print("El teléfono debe tener 9 dígitos numéricos.")

            # Editar email
            elif opc == 2:
                nuevo_mail = input("Ingrese el nuevo correo electrónico: ")
                mail_correcto = True
                # Verificar formato del correo
                ini = nuevo_mail.find("@")
                if nuevo_mail.count("@") != 1 or ini == -1:
                    print("Correo inválido: debe contener un solo '@'.")
                    mail_correcto = False
                else:
                    usuario = nuevo_mail[:ini]
                    dominio = nuevo_mail[ini + 1:]

                    if ".." in usuario or usuario.startswith(".") or usuario.endswith("."):
                        print("Correo inválido: error en la parte del usuario.")
                        mail_correcto = False

                    if ".." in dominio or dominio.startswith(".") or dominio.endswith("."):
                        print("Correo inválido: error en la parte del dominio.")
                        mail_correcto = False
                    elif "." not in dominio:
                        print("Correo inválido: dominio sin extensión.")
                        mail_correcto = False

                if mail_correcto:
                    dic_users[dni]["mail"] = nuevo_mail
                    print("Correo actualizado a:", nuevo_mail)

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
            if opc == 1:
                libro_prestamos = input("Introduce el isbn del libro prestamos: ")
                if libro_prestamos in dic_libros:
                    if libro_prestamos not in dic_users[dni]["prestamos"]:
                        dic_users[dni]["prestamos"].append(libro_prestamos)
                        print("Libro añadido a la lista de prestamos.")
                    else:
                        print("El libro ya exite en la lista.")
                print(dic_users)
            elif opc == 2:
                libro_a_eliminar = input("Introduce el isbn del libro a eliminar: ")
                if libro_a_eliminar in dic_users[dni]["prestamos"]:
                    dic_users[dni]["prestamos"].remove(libro_a_eliminar)
                    print("Libro eliminado de la lista de prestamos.")
                print(dic_users)

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
