"""
i es el índice del token dentro del documento padre.

text devuelve el texto del token.

is_alpha, is_punct y like_num devuelven valores booleanos que indican si un token está compuesto por caracteres alfabéticos, 
si es un signo de puntuación, o si parece ser un número. Por ejemplo, el token "10" - uno, cero - o la palabra "diez" - D, I, E, Z."""

import spacy

nlp = spacy.blank('es')

doc = nlp("Eso cuesta $5.")

print("Indicice: ",[token.i for token in doc]) # Aqui arroja una lista de indices por cada token que encuentre en formato numerico.
print("Texto: ", [token.text for token in doc]) # Aqui arroja una lista de token que encuentre sin importar los signos.

print("is_alpha: ",[token.is_alpha for token in doc]) # Aqui va a detallar cuales son valores alpha como palabras clave
print("is_punct: ",[token.is_punct for token in doc]) # Aqui arroja valores bool y valor True cuando encuentra signos de puntuacion.
print("like_num: ",[token.like_num for token in doc]) # Aqui arroja valores True o False cuando encuentre un numero.