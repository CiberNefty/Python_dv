"""PARTE 1: Español

# Usa (spacy.blank) para crear un objeto nlp vacío para procesar español ("es").
# Crea un doc e imprime su texto en la pantalla.
"""
# Importamos spaCy
import spacy

# Creamos objeto spacy (NLP) para procesar en español.
nlp = spacy.blank('es')

# Procesamos un texto en un doc.
doc =nlp('Que hace mi papa, vamos por una salchipapas')

# Imprimimos nuestro doc con un atributo text.
print("Texto: ", doc.text)