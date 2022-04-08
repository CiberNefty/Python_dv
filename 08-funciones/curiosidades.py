"""
        CURIOSIDADES
    RECOMENDACIONES FUNCIONES
1. Recomendacion cuando vayamos a realizar una funcion
deajr todas las funciones al comienzo del programa.
2. en ves de realizar un print dentro de una funcion,
  es mejor que una funcion devuelva un dato.
3. podemos acceder a variables locales dentro de nuestras
 funciones y, cuando vayamos a ejecutar cada funcion es necesario
 que esten definidas esas variables antes de llamar a la funcion.
4. Otra recomendacion es que por regla general a no se de que vayan
a impimir una cosa en concreto, lo recomendable es que le pase los valores 
como parametro a la funciones y que las funciones se encanrgen de mostrar esos datos
""" 
def mi_funcion(nombre):
    return "Hola que tal " + nombre 

def mi_segunda_funcion(apellido):
    return "Hola que tal 2 " + apellido

nombre = "DAniel"
apellido = "Vera"

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellido))

