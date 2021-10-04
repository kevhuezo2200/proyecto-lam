from django.shortcuts import render, HttpResponse
from .models import Project


html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contactame</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,"principal/home.html")

def about(request):
   return render(request,"principal/about.html")


def contact(request):
    return render(request,"principal/contacto.html")

# modificacion para pantalla admin 

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "principal/portafolio.html", {'projects':projects})