from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    contexto = {
        "sistema": "EcoEnergy",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }
    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

def zonas(request):
    zonas = [
        {"nombre": "Oficina Central", "responsable": "Área de Administración"},
        {"nombre": "Planta de Producción", "responsable": "Área de Operaciones"},
        {"nombre": "Bodega", "responsable": "Área de Logística"},
    ]
    return render (
        request,
        "dispositivos/zonas.html",
        {"zonas": zonas}
    )

def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"},
    ]
    return render(
        request,
        "dispositivos/catalogo.html",
        {"dispositivos": dispositivos},
    )