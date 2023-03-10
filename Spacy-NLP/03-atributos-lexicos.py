"""
i es el índice del token dentro del documento padre.

text devuelve el texto del token.

is_alpha, is_punct y like_num devuelven valores booleanos que indican si un token está compuesto por caracteres alfabéticos, 
si es un signo de puntuación, o si parece ser un número. Por ejemplo, el token "10" - uno, cero - o la palabra "diez" - D, I, E, Z."""

import spacy

nlp = spacy.blank('es')

doc = nlp("Eso cuesta $5.")

print("Indicice: ",[token.i for token in doc])
print("is_punct: ",[token.is_punct for token in doc])
print("like_num: ",[token.like_num for token in doc])