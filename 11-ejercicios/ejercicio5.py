"""
Ejercicio5.
Crear una lista con el contenido de esta tabla:
ACCION      AVENTURA           DEPORTES
GTA         ASSASINS            FIFA 21    
COD         CRASH               PRO 21
PUGB        Prince of persia    MOTO GP 21

- Guardarla en un listado de disccionarios
- Mostrar esta informacion ordenada
"""
tablaJuegos = [ # Entonces tenemos una lista de disccionarios y dentro de los diccionarios tenemos una lista.
    {
        'categoria': 'ACCION',
        'juegos': ['GTA', 'COD', 'PUGB'],
    },
    {
        'categoria': 'AVENTURA',
        'juegos': ['ASSASINS', 'CRASH','Prince of Persia']   
    },
    {
        'categoria': 'DEPORTER',
        'juegos': ['FIFA 21','PRO 21','MOTO GP 21']
    }
]
for categoria in tablaJuegos: # Recorreme toda la tabla y en cada iteracion creame una variable categoria.
    print(f"---------------- {categoria['categoria']} ----------------")
    for juego in categoria['juegos']: # significa que recorra la lista de juegos y vaya creando la variable juego en cada vuelta que demos a esa lista
        print(juego)
