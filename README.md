# Proyecto Integrado / EcoEnergy

## Descripción

Proyecto Django de backend para EcoEnergy, con una estructura inicial basada en la aplicación `dispositivos`. El proyecto incluye una vista de inicio, una vista de zonas y una vista de catálogo de dispositivos.

## Objetivo

Servir como base de desarrollo del backend del proyecto EcoEnergy, con navegación simple entre páginas y datos de ejemplo en contexto para comprobar el renderizado de plantillas.

## Estructura del proyecto

Los archivos verificados en el repositorio son:

```text
.
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dispositivos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
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
└── .venv/
```

## Plantillas del proyecto

La plantilla base se encuentra en `templates/base.html` y define la navegación principal:

- Inicio
- Dispositivos
- Zonas

La navegación usa las rutas nombradas de Django:

```django
<a href="{% url 'dispositivos:inicio' %}">Inicio</a>
<a href="{% url 'dispositivos:catalogo' %}">Dispositivos</a>
<a href="{% url 'dispositivos:zonas' %}">Zonas</a>
```

Las plantillas verificadas son:

- `templates/dispositivos/inicio.html`
- `templates/dispositivos/catalogo.html`
- `templates/dispositivos/zonas.html`

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

## Claves de contexto

Las vistas verificadas en `dispositivos/views.py` envían estas claves a las plantillas:

### `inicio`

```python
contexto = {
    "sistema": "EcoEnergy",
    "mensaje": "Monitoreo energético responsable",
    "asignatura": "Programación Back End",
}
```

### `zonas`

```python
{"zonas": [
    {"nombre": "Oficina Central", "responsable": "Área de Administración"},
    {"nombre": "Planta de Producción", "responsable": "Área de Operaciones"},
    {"nombre": "Bodega", "responsable": "Área de Logística"},
]}
```

### `catalogo`

```python
{"dispositivos": [
    {"nombre": "Medidor inteligente", "estado": "Activo"},
    {"nombre": "Sensor de temperatura", "estado": "Activo"},
    {"nombre": "Climatizador", "estado": "Revisión"},
]}
```

## Requisitos previos

- Python
- `pip`
- Git
- Entorno virtual (`.venv`)

## Instalación y ejecución

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verificación de configuración Django:

```bash
python manage.py check
```

Arranque del servidor de desarrollo:

```bash
python manage.py runserver
```

## Prueba de navegación

Se comprobó que las rutas nombradas de Django se resuelven correctamente y que la estructura de navegación está definida en la plantilla base.

### Navegación esperada

1. Abrir `http://127.0.0.1:8000/`
2. Comprobar que aparece la página de inicio con el texto de contexto
3. Usar el menú para acceder a:
    - `http://127.0.0.1:8000/dispositivos/`
    - `http://127.0.0.1:8000/zonas/`

### Verificación de rutas por nombre

Se ejecutó esta comprobación en el proyecto:

```bash
python manage.py shell -c "from django.urls import reverse; print(reverse('dispositivos:inicio')); print(reverse('dispositivos:catalogo')); print(reverse('dispositivos:zonas'))"
```

Resultado verificado:

- `reverse('dispositivos:inicio')` → `/`
- `reverse('dispositivos:catalogo')` → `/dispositivos/`
- `reverse('dispositivos:zonas')` → `/zonas/`

## Estado actual

El proyecto se encuentra en una etapa inicial de desarrollo con configuración base de Django y una navegación simple entre páginas. Los datos mostrados en las vistas son datos de ejemplo definidos directamente en `dispositivos/views.py`.

## Próximos pasos

- Definir modelos y persistencia de datos reales.
- Ampliar la lógica de negocio de la aplicación `dispositivos`.
- Añadir más templates y rutas según el alcance del proyecto.
- Revisar la configuración para entornos de desarrollo y producción.
