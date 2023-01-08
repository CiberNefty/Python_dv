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
from usuarios import acciones # Estamos importando el modulo acciones desde el paquete usuarios.

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazel = acciones.Acciones() # Aqui tenemos un objeto que es el instaciador de la clase.
# Haremos una variable donde preguntara la accion que desee el usuario.
accion = input('¿Que quiere hacer?: ')

if accion == 'registro':
    hazel.registro() # Aqui llamamos a el objeto y luego nos invocara lo que es el metodo registro.
    
elif accion == 'login':
    hazel.login()