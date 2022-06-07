# como capturar excepciones y manjear errores en codigo 
# susceptible a fallos/errores


try:
    nombre = input("¿Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = 'El nombre es '+ nombre
    print(nombre_usuario)
except:
    print('Ha ocurido un error, mete bien el nombre.')

else:
    print('Todo ha funcionado correctamente.')
finally:
    print('Fin de la iteracion !!')