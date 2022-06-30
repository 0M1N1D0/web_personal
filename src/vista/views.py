"""vistas basadas en funciones de la app vista"""

from django.shortcuts import render  # Create your views here.


# vista home
def home(request):
    """renderiza home.html"""
    return render(request, 'vista/home.html')


def about(request):
    """renderiza about.html"""
    return render(request, 'vista/about.html')


def contact(request):
    """renderiza contact.html"""
    return render(request, 'vista/contact.html')

 
