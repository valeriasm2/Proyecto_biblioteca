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
                         'prestamos':['ISB4578', 'ISB9123', 'ISB6384'], 'leidos':['ISB4928', 'ISB8475']},
             '5678910W':{'nombre':'Maria Garcia', 'edad':12, 'tfn':678901234, 'mail':'marigarcia@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB3985'], 'leidos':['ISB2754', 'ISB1329']},
             '12345678A':{'nombre':'Pedro Martínez', 'edad':5, 'tfn':543216789, 'mail':'pedromartinez@gmail.com',
                         'prestamos':['ISB4578', 'ISB9123', 'ISB8301'], 'leidos':['ISB4928']},
             '98765432Z':{'nombre':'Ana Martínez', 'edad':30, 'tfn':987654321, 'mail':'anamartinez@gmail.com',
                         'prestamos':['ISB1329', 'ISB7561', 'ISB8475'], 'leidos':['ISB2754','ISB3985','ISB8301']}
             }
