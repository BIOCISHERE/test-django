# Proyecto Integrado / EcoEnergy

## Descripción y objetivo

Proyecto Django para EcoEnergy con una estructura inicial orientada a la visualización de datos de ejemplo mediante plantillas. El repositorio incluye una página de inicio, una vista de zonas y un catálogo de dispositivos.

## Estructura del proyecto

La estructura real del repositorio incluye los siguientes elementos:

```text
.
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── data/
│   ├── dispositivos.json
│   └── zonas.json
├── dispositivos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── dispositivos/
│       ├── catalogo.html
│       ├── inicio.html
│       └── zonas.html
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
├── .venv/
└── ...
```

## Archivo JSON y estructura de datos

Los archivos JSON reales del proyecto se encuentran en la carpeta `data/`:

- `data/dispositivos.json`
- `data/zonas.json`

### `data/dispositivos.json`

```json
[
    {
        "id": 1,
        "nombre": "Medidor inteligente",
        "estado": "Activo",
        "consumo_kwh": 18.4
    },
    {
        "id": 2,
        "nombre": "Climatizador",
        "estado": "Revisión",
        "consumo_kwh": 32.7
    }
]
```

### `data/zonas.json`

```json
[
    {
        "id": 1,
        "nombre": "Oficina Central",
        "responsable": "Administración",
        "estado": "Activo",
        "consumo_promedio_kwh": 45.2
    },
    {
        "id": 2,
        "nombre": "Planta de Producción",
        "responsable": "Operaciones",
        "estado": "Revisión",
        "consumo_promedio_kwh": 128.6
    }
]
```

## Función de carga de datos

La carga de datos se realiza en `dispositivos/services.py`.

```python
import json
from django.conf import settings

def cargar_dispositivos():
    ruta = settings.BASE_DIR / "data" / 'dispositivos.json'
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de dispositivos")
    return datos

def cargar_zonas():
    ruta = settings.BASE_DIR / "data" / 'zonas.json'
    with ruta.open(encoding="utf-8") as archivo:
        datos = json.load(archivo)
    if not isinstance(datos, list):
        raise ValueError("Se esperaba una lista de zonas")
    return datos
```

## Rutas funcionales

La configuración principal de URLs está en `config/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("dispositivos.urls")),
]
```

La aplicación `dispositivos` define estas rutas en `dispositivos/urls.py`:

```python
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("zonas/", views.zonas, name="zonas"),
    path("dispositivos/", views.catalogo, name="catalogo"),
]
```

### URLs disponibles

- `/` → vista de inicio
- `/zonas/` → vista de zonas
- `/dispositivos/` → vista de catálogo de dispositivos

## Dependencia externa

El proyecto incluye la dependencia `django-bootstrap5` en `requirements.txt`:

```text
django-bootstrap5==26.3
```

### Justificación y prueba

La dependencia está siendo usada en la plantilla base `templates/base.html`:

```django
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
```

Esto confirma que la biblioteca Bootstrap 5 de Django está integrada en la interfaz. La evidencia del proyecto es que `requirements.txt` contiene la dependencia y la plantilla usa sus etiquetas de carga y renderizado.

## Requisitos previos

- Python
- `pip`
- Git
- Entorno virtual `.venv`

## Instalación desde `requirements.txt`

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Verificación

Se comprobó la configuración del proyecto y la resolución de rutas con estos comandos:

```bash
python manage.py check
```

```bash
python manage.py shell -c "from django.urls import reverse; print(reverse('dispositivos:inicio')); print(reverse('dispositivos:catalogo')); print(reverse('dispositivos:zonas'))"
```

### Resultado verificado

- `reverse('dispositivos:inicio')` → `/`
- `reverse('dispositivos:catalogo')` → `/dispositivos/`
- `reverse('dispositivos:zonas')` → `/zonas/`

## Estado actual

El proyecto está en una etapa inicial de desarrollo con Django, navegación básica y carga de datos desde archivos JSON locales. La lógica actual no usa base de datos todavía y los datos mostrados son datos de ejemplo.

## Próximos pasos

- Definir modelos y persistencia de datos.
- Ampliar la lógica de negocio de la aplicación `dispositivos`.
- Revisar la configuración para un entorno más completo de desarrollo y despliegue.
