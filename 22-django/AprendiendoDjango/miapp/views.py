from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Model View Contoler
# MVT = Model Template View

def index(request):

    html = """
        <h1>Inicio</h1/>
        <p>Años hasta el 2050:</p>        
        <ul>
        """
    
    year = 2025

    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"

    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("""
        <h1>Hola Mundo con DJANGO</h1>
    <h3>Soy Daniel aqui retomando conceptos con django.</h3>""")

def pagina(request):
    return HttpResponse(
        """
        <h1>Pagina de mi Web</h1>
        <p>Creado por daniel</p>
        """)