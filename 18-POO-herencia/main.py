import clases

persona = clases.Persona()
persona.setNombre('Daniel')
persona.setApellidos('Vera')
persona.setAltura("176 cm")
persona.setEdad("239 años")

print(f'La persona {persona.getNombre()} {persona.getApellidos()}')
# Tambien podria llamar a un metodo en concreto que tenga mi objeto
print(persona.hablar())

print('-------------------------------')
informatico = clases.Informatico()
informatico.setNombre('Juan')
informatico.setApellidos('Vera')

print(f'El informatico es: {informatico.getNombre()} {informatico.getApellidos()}')
print(f'Sabe estos lenguajes: {informatico.getLenguajes()}')
print(informatico.caminar())
print(informatico.experiencia)
print('-------------------------------')

tecnico = clases.TecnicoRedes()
tecnico.setNombre('Manuel')
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())