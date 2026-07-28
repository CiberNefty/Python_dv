from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormularioArticle
from django.contrib import messages
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

def save_article(request): # Esta funcion sera enviada por medio de un formulario es igual a la funcion de arriba

    # Comprobar que nos llegan datos por GET

    if request.method == 'POST':
        # Recibimos datos
        title = request.POST['title']

        # Podemos hacer validaciones Manuales
        if len(title) <= 5:
            return HttpResponse("El titulo es muy pequeño")

        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public,
        )
        # Guardar objeto en la DB
        articulo.save()

        return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong>- {articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo.</h2>")

def create_article(request): # Esta funcion va a dar soporte para visualizar una plantilla



    return render(request, 'create_article.html')

# Funcion para formulario de django (forms.py)
def create_full_article(request):

    # COMPROBAR SI NOS LLEGAN DATOS DE NUESTRO FORMULARIO POR POST
    if request.method == 'POST':
        formulario = FormularioArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get("title")
            content = data_form["content"]
            public = data_form["public"]

            articulo = Article(
                        title = title,
                        content = content,
                        public = public,
            )
            # Guardar objeto en la DB
            articulo.save()

            # Crear Mensaje flash (sesion que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect("articulos")
            #return HttpResponse(title+" - "+content+" - "+ str(public))


    else:
        # Si no llega generamos un formulario vacio   
        formulario = FormularioArticle()

    return render(request, 'create_full_article.html',
                  {'form':formulario})

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

# Actualizar resgistros:
def editar_articulo(request, id):
    # Objetemos dato con get
    articulo = Article.objects.get(pk = id)
    
    # Actualizar resgistros desde los datos del modelo
    articulo.title = 'Batman'
    articulo.content = 'Articulo de batman'
    articulo.public = False

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title}</strong>- {articulo.content}")

# Mostrar todos los articurlos
def articulos (request):
    #articulos = Article.objects.all()
    articulos = Article.objects.all().order_by('-id')
    #articulos = Article.objects.order_by('-title')
    #articulos = Article.objects.order_by('id')[:3]
    #articulos = Article.objects.order_by('id')[1:4]

    #  Consultas con condiciones
    # articulos = Article.objects.filter(title = "Batman", id = 3)
    # articulos = Article.objects.filter(title__contains = "articulo") # SQL == (LIKE)
    # articulos = Article.objects.filter(title__exact = "articulo") 
    # articulos = Article.objects.filter(title__iexact = "articulo") 
    #articulos = Article.objects.filter(id__gte=9) # mayor igual a 
    """
    articulos = Article.objects.filter(id__lte=9) # menores iguales a
    articulos = Article.objects.filter(
        #Q(title__contains = "2") | Q(title__contains = "3")
        Q(title__contains = "2") | Q(public = True)
    ) # OR (from django.db.models import Q)
    """
    """
    articulos = Article.objects.filter(
                                        title__contains = 'Articulo',
                                    ).exclude(
                                        public = False
                                    )
    """
    # CONSULTAS CRUDAS CON DJANGO
    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Articulo 2' AND public = 1 ")

    #return HttpResponse(articulos)
    return render(request, 'articulos.html',{
        'articuloss': articulos
    })

# Borrar Elementos
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk = id)
    articulo.delete()

    return redirect('articulos')
