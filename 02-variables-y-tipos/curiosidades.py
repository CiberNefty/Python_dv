mi_texto = " 'curioso' "
mi_texto2 = "Master en \"python\""

texto_unido = mi_texto+" "+ mi_texto2
print(texto_unido)

texto_unido = mi_texto+" \n"+ mi_texto2 #Esto me dara un salto de linea (\n)
print(texto_unido)

texto_unido = mi_texto+" \t"+ mi_texto2 # Esto me dara una tabulacion 
print(texto_unido)

texto_unido = mi_texto+" \r"+ mi_texto2 # Esto me borrara lo que hay antes de la instruccion  \r
print(texto_unido)
