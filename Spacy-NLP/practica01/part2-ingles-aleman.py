"""PARTE 1: Ingles - Aleman

# Usa spacy.blank para crear un objeto nlp vacío para procesar inglés ("en" y 'de').
# Crea un doc e imprime su texto en la pantalla.
"""
import spacy

#nlp = spacy.blank('en') # Ingles
nlp = spacy.blank('de') # aleman

doc = nlp("This is a sentence.")
doc = nlp("Liebe Grüße!")

print(doc.text)

