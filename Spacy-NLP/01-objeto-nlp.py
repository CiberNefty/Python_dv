#Importa spaCy
import spacy

# Creamos un objeto nlp vaio para procesar español
nlp = spacy.blank('es')

# Creado al procesar un string de texto con un objeto nlp
doc = nlp('¡Hello Word! daniel Vera')

# Itera sobre los token en un Doc
for token in doc:
    print(token.text)