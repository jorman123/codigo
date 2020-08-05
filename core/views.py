from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">PORTADA</a>              </li>
        <li>   <a href="/registro_participantes/"> registro_participantes: </a>   </li>
        <li>   <a href="/contact/"> Contacto </a>     </li>
        <li>   <a href="/galeria/"> galeria </a>     </li>
        <li>   <a href="/registro_admin/"> registro_admin: </a>   </li>
        <li>   <a href="/registro_events/"> registro de eventos </a>     </li>
        <li>   <a href="/blog/"> blog </a>     </li>
        <li>   <a href="/planificacion_conferencia/"> planificacion de las conferencias </a>     </li>
    </ul>
"""


def home(request):
    html_responsde = "<h1>La pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def contact(request):
    html_responsde = "<h1>La pagina de contacto</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def galeria(request):
    html_responsde = "<h1>Vestibulo</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def registro_events(request):
    html_responsde = "<h1>registro de eventos</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def registro_participantes(request):
    html_responsde = "<h1>aqui se registraran los participantes</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def registro_admin(request):
    html_responsde = "<h1>aqui se registraran los administradores</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def blog(request):
    html_responsde = "<h1>aqui se archivaran los diferentes tipos de blogs</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def planificacion_conferencia(request):
    html_responsde = "<h1>planificacion de las conferencias</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def home(request, template="home.html"):
    return render(request, template);

def registro_participantes(request, template="registro_participantes.html"):
    return render(request, template);

def contact(request, template="contact.html"):
    return render(request, template);

def galeria(request, template="galeria.html"):
    return render(request, template);

def registro_events(request, template="registro_events.html"):
    return render(request, template);

def registro_admin(request, template="registro_admin.html"):
    return render(request, template);

def blog(request, template="blog.html"):
    return render(request, template);

def planificacion_conferencia(request, template="planificacion_conferencia.html"):
    return render(request, template);