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
tablaJuegos = [
    {
        'Accion': 'GTA',
        'Accion': 'COD',
        'Accion': 'PUGB',
    },
    {
        'AVENTURA': 'ASSASINS',
        'AVENTURA': 'CRASH',
        'AVENTURA': 'Prince of persia'
    },
    {
        'DEPORTES': 'FIFA 21',
        'DEPORTES': 'PRO 21',
        'DEPORTES': 'MOTO GP 21'
    }

]
for tablaGames in tablaJuegos:
    print(f"ACCION\n{tablaGames['ACCION']['AVENTURA']}")