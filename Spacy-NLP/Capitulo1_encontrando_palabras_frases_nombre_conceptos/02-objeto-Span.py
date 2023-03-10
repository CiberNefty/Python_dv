import spacy

nlp = spacy.blank('es')

doc = nlp('¡Hola Mundo! con Daniel!')

# Un Slice de un Doc en un objeto Span
span = doc[2:5]

# Obtengo el texto del Span a través del atributo .text
print(span.text)