from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article

# Create your views here.
# MVC = Model View Contoler
# MVT = Model Template View

layout = """
<h1>Sitio Web con Django | Daniel Vera</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Pagian Pruebas</a>
    </li>
    <li>
        <a href="/contacto-dos">Contacto</a>
    </li>
</ul>
<hr/>
"""

def index(request):
    """
    html = ""
        <h1>Inicio</h1/>
        <p>Años hasta el 2050:</p>        
        <ul>
        ""
    
    year = 2025

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>
    """

    year = 2025
    haasta = range(year, 2051)

    nombre = 'Daniel V'
    lenguajes = ['Python','Java','Javascript','C++','PHP']

#    return HttpResponse(layout+html)
    return render(request, 'index.html', {
        'mi_title':'Inicio',
        'mi_variable': "Soy un dato que esta en la vista",
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years' : haasta
    })

def hola_mundo(request):
#    return HttpResponse(layout+"""
#        <h1>Hola Mundo con DJANGO</h1>
#    <h3>Soy Daniel aqui retomando conceptos con django.</h3>""")
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        #return redirect('/inicio') # A una url
        #return redirect('/contacto/Esteban/gGomez') # A una url con parametros
        return redirect('contacto', nombre = "Felipe", apellido = 'Ibarguen') # A una url siendo mas compleja llamando parametros 

    #return HttpResponse(
    #    layout+"""
    #    <h1>Pagina de mi Web</h1>
    #    <p>Creado por daniel</p>
    #    """)
    return render(request, 'pagina.html',
                  {'texto':'Este es un texto',
                   'lista':['uno','dos','tres']})

#def contacto (request, nombre, apellido):
#def contacto (request, nombre="Jose", apellido="Jose"):
def contacto (request, nombre="", apellido=""):
    html = ''
    if nombre and apellido:
        html +="<p>El nombre compelto es:</p>"
        html +=f"<h3>{nombre} {apellido}</h3>"

    return HttpResponse(layout+f"<h1>Contacto {nombre} {apellido}</h1>" +html)

def crear_articulo(request, title, content, public):
    # Crear objeto de tipo del modelo (tabla) para guardar registro
    articulo = Article(
        title = title,
        content = content,
        public = public,
    )
    # Guardar objeto en la DB
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong>- {articulo.content}")

# Como sacar informacion (select)
def articulo(request, title):
    # Mostrar algunn articulo toca hacer una consulta a la DB haciendo uso de nuesto modelo
    #articulo = Article.objects.get(pk = 6)
    #articulo = Article.objects.get(id = 6)
    #articulo = Article.objects.get(title = "Titulo 1 Prueba")
    try:
        articulo = Article.objects.get(title = title, public = False)
        response = F"Articulo: <br/>{articulo.id}.{articulo.title}"
    except:
        response = "<h1>Articulo no encontrado. Busca otro.</h1>"
    return HttpResponse(response)