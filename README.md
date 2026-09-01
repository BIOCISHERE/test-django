# Proyecto Integrado / EcoEnergy

Backend desarrollado en Python con Django para el proyecto EcoEnergy.

## Descripción y objetivo

Este repositorio corresponde al backend del proyecto EcoEnergy dentro del contexto de Proyecto Integrado. Su objetivo es servir como base de desarrollo para la lógica de negocio, la gestión de datos y la exposición de servicios del backend mediante Django.

Actualmente, el proyecto está en una estructura inicial de Django con configuración estándar y SQLite como base de datos local de desarrollo.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python
- pip
- Git
- Un entorno virtual (.venv)

## Clonación del repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
```

> Sustituye la URL y el nombre del directorio por los datos reales del proyecto.

## Creación y activación de .venv

Desde la raíz del proyecto, crea un entorno virtual y actívalo:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Instalación desde requirements.txt

Instala las dependencias del proyecto:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Comandos de verificación

Para comprobar que la configuración del proyecto está correcta:

```bash
python manage.py check
```

Para iniciar el servidor de desarrollo local:

```bash
python manage.py runserver
```

Para aplicar posibles cambios de base de datos y dejarla preparada para el desarrollo:

```bash
python manage.py migrate
```

## Estado actual

El proyecto se encuentra en una etapa inicial de desarrollo. La estructura base de Django ya está creada y la configuración actual incluye SQLite como motor de base de datos.

## Próximos pasos

- Definir la arquitectura del backend.
- Crear las aplicaciones necesarias para la lógica de negocio.
- Configurar modelos, endpoints y servicios según corresponda.
- Validar la base de datos y la configuración del entorno.
- Añadir pruebas y revisar la seguridad de la aplicación.
- Preparar la estructura para el siguiente ciclo de desarrollo.

## Nota

Este README es una versión inicial del proyecto y puede completarse con información más específica cuando se definan detalles reales del repositorio, como la URL exacta, la descripción funcional completa y cualquier requisito adicional del entorno de desarrollo.