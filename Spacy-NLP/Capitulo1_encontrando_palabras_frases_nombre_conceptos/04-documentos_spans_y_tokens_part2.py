""" Paso 2
- Utiliza spacy.blank para crear el objeto nlp para procesar español.
- Procesa el texto y genera un instance de un objeto Doc en la variable doc.
- Crea un slice de Doc para los tokens “panteras negras” y “panteras negras y los leones”."""
import spacy

nlp = spacy.blank('es')

# Procesamos texto.
doc = nlp('Me gustan las panteras negras y los leones.')

# Un slice del Doc para "Panteras negras"
panteras_negras = doc[3:5]
print(panteras_negras.text)

# Un slice del Doc para "panteras negras y los leones" (sin el ".")
panteras_negras_y_los_leones = doc[3:8]
print(panteras_negras_y_los_leones.text)