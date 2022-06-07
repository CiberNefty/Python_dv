# como capturar excepciones y manjear errores en codigo 
# susceptible a fallos/errores


"""try:
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
    """
# Multiples ecepciones
try:
    numero = int(input('Numero para elevarlo al cuadrado: '))
    print('El cuadrado es: '+str(numero*numero))
except TypeError:
    print('Debes convertir tus cadenas a enteros en el codigo')
#except ValueError:
    #print('Introduce un numero correcto.')
except Exception as e: # Aqui eestamos guardando la excepcion en una variable
    print(type(e))
    print('Ha ocurrido un error: ',type(e).__name__) # la constante que es .__name__ de esta manera me mostrara el error que hay.
