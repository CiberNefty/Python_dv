"""
Esta aplicacion funcionara identificando con usuarios que podamos 
registrar en la BD, donde tendra un login y un registro de BD a nivel
de consola con un asistente y luego cuando logremos identificarnos 
vamos a poder guardar nuestras notas personales

PROYECTO Python y Mysql:

- Abrir asistente
- Login o registro
- Si elegimos registro, creará un usuario en la bbdd
- Si elegimos login, identifica al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas.
"""

print("""
Acciones disponibles:
    - Registro
    - Login
""")

# Haremos una variable donde preguntara la accion que desee el usuario.
accion = input('¿Que quiere hacer?: ')

if accion == 'registro':
    print("\nOk! Vamos a registrarte en el sistema...")
    nombre = input('Cual es tu nombre?: ')
    apellidos = input('Cuales son tus apellidos?: ')
    mail = input('Introduce email: ')
    password = input('Introduce tu contraseña: ')
elif accion == 'login':
    print("\nVale! Identificate en el sistema...")
    mail = input('Introduce email: ')
    password = input('Introduce tu contraseña: ')