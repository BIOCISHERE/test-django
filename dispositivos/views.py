from django.shortcuts import render
from django.http import HttpResponse
from dispositivos.services import cargar_dispositivos, cargar_zonas

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
    zonas = cargar_zonas()
    activos = sum(
        1 for item in zonas
        if item["estado"] == "Activo"
    )
    contexto = {
        "zonas": zonas,
        "total": len(zonas),
        "total_activos": activos
    }
    return render(
        request, "dispositivos/zonas.html", contexto
    )

def catalogo(request):
    dispositivos = cargar_dispositivos()
    activos = sum(
        1 for item in dispositivos
        if item["estado"] == "Activo"
    )
    contexto = {
        "dispositivos": dispositivos,
        "total": len(dispositivos),
        "total_activos": activos,
    }
    return render(
        request, "dispositivos/catalogo.html", contexto
    )