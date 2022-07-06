# Capturar Excepcione y manejar errores en codigo 
# Suceptible a fallos / errores

"""try:
    nombre = input("cual es tu nombre Nombre?: ")

    if len(nombre) > 1: # Aqui le estamos diciendo que si nombre tiene una longitud mayor que 1, entra y guarda ese valor en una nueva variable.
        nombre_usuario = 'El nombre es '+ nombre

    print(nombre_usuario)
except: # Esta es el manejo de excepciones.
    print('Ha ocurrido un error, mete bien el nombre.') 
else: # La instruccion else en manejo de excepciones nos brindara algo siempre y cuando algo no falle
    print('Todo a funcionado correctamente')
finally: # la Instruccion finally siempre se va a ejecutar
    print('FIn de la iteracion')"""

# MULTIPLES EXCEPCIONES
"""try:
    numero = int(input('Numero para elevarlo al cuadrado: '))
    print("El cuadrado es: "+str(numero*numero))
except TypeError: #Aqui capturamos la excepcion que queremos.
    print('Debes convertir tus cadenas en enteros en el cogio!!')
#except ValueError:
#    print('Intruduce un numero correcto. !!')
    # Podemos capturar los errores para que se muestren de una manera mas amigable
except Exception as e: # Podemos guardar una excepcion en una variable luego despues del as.
    print(type(e)) # Podemos mostrar la excepcion con type(nombre de la variable que contiene el error.)
    print('Ha ocurrido un error: ',type(e).__name__)
"""

# EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCIONES
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al Master en Python {nombre} !!")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Existe un error: ", e)