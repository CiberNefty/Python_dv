""" Paso 1

- Utiliza spacy.blank para crear el objeto nlp para procesar español.
- Procesa el texto y genera un instance de un objeto Doc en la variable doc.
- Selecciona el primer token del Doc e imprime su texto (text) en pantalla.
"""
import spacy

nlp = spacy.blank('es')

# Procesa el texto
doc = nlp('Me gustan las panteras negras y los leones.')

# Selecciona el primer token.
primer_token = doc[0]

# Imprimir en pantalla el token.
print(primer_token.text)