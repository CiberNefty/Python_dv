cantantes = ['2pac','Drake','Bad Bunny','Julio Iglesias']
numeros = [1,2,5,8,3,5]

# Ordenar 
#print(numeros)

# METODO sort() -- Ayuda a que las listas esten ordenadas.
numeros.sort()#print(numeros)

# METODO para AÑADIR ELEMENTOS A UNA LISTA.
cantantes.append("Natos y Waor")
cantantes.insert(1, "David Bisbal") # Este metodo nuevo admite dos valores el primero es la posicion de la lista y el segundo es el valor

#print(cantantes)

# ELIMIAR ELEMENTOS DE UNA LISTA
cantantes.pop(1)

# Eliminar elementos por el valor que tiene en concreto.
cantantes.remove("Bad Bunny")

#print(cantantes)

# DAR LA VUELTA A UNA LISTA.
# El MEtodo reverse() toma como ejemplo que en vesz de pasar por el 1 pasa por el ultimo, tambie se puede con valores str

#print(numeros)
numeros.reverse()
#print(numeros)

# Buscar dentro de una lista.
print('Drake' in cantantes) # con esta especie de operador nos mostrara si esta el valor y, nos devuelve  TRUE OR FALSE.

# CONTAR ELEMTENOS.
print(cantantes)
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO
numeros.append(8)
print(numeros.count(8)) # La funcion count() me ayuda a verificar si ese valor cuantas veces esta repetido.

# CONSEGUIR INDICE.
print(cantantes.index("Drake")) # Aqui observamos en que posicion se encuentra tal valor.

# UNIR DOS LISTAS
cantantes.extend(numeros)

print(cantantes)