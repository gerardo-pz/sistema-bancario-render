# 💳 Sistema Bancario

Sistema web desarrollado con **Django** para la gestión de operaciones bancarias básicas como creación de cuentas, envío de transacciones, auditoría y administración de usuarios. Diseñado para simular el comportamiento de una plataforma bancaria real.

---

## 📚 Tabla de Contenidos

- [🎯 Objetivo](#-objetivo)
- [🚀 Funcionalidades Principales](#-funcionalidades-principales)
- [🛠️ Tecnologías Utilizadas](#️-tecnologías-utilizadas)
- [⚙️ Instalación y Ejecución Local](#️-instalación-y-ejecución-local)
- [🚀 Despliegue en Render](#-despliegue-en-render)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)

---

## 🎯 Objetivo

Este proyecto tiene como propósito simular un sistema bancario básico que permita registrar usuarios, gestionar sus cuentas, realizar transacciones entre ellas y mantener un historial auditable de todas las operaciones.

---

## 🚀 Funcionalidades Principales

- 🧑 Registro y autenticación de usuarios
- 💼 Creación y gestión de cuentas bancarias
- 💸 Transferencias entre cuentas
- 📬 Gestión de solicitudes (autorizaciones, revisiones)
- 📜 Auditoría de eventos y operaciones del sistema
- 📚 Implementación de estructuras de datos clásicas (pila, cola, árbol binario, lista enlazada)

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.11
- **Framework:** Django 5.2.1
- **Base de datos:** PostgreSQL 
- **Servidor:** Gunicorn
- **Archivos estáticos:** WhiteNoise
- **Estilos:** Bootstrap
- **Otros:** 
  - Django Admin
  - Django ORM
  - dj-database-url

---

## ⚙️ Instalación y Ejecución Local

Sigue estos pasos para correr el proyecto localmente:

### 1. Clona el repositorio

```bash
git clone https://github.com/syderkkk/sistema-bancario.git
cd sistema-bancario
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

```bash
# Copia el archivo de ejemplo
cp env.example .env

# Edita el archivo .env con tus configuraciones locales
# Asegúrate de cambiar SECRET_KEY y configurar DATABASE_URL
```

### 5. Ejecuta las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crea un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Ejecuta el servidor

```bash
python manage.py runserver
```

El proyecto estará disponible en `http://localhost:8000`

---

## 🚀 Despliegue en Render

Este proyecto está configurado para ser desplegado fácilmente en Render. Sigue estos pasos:

### 1. Preparación del repositorio

Asegúrate de que tu código esté en GitHub con todos los archivos de configuración:
- `requirements.txt`
- `Procfile`
- `runtime.txt`
- `render.yaml`
- `env.example`

### 2. Conectar con Render

1. Ve a [Render](https://render.com) y crea una cuenta
2. Conecta tu repositorio de GitHub
3. Selecciona el repositorio del sistema bancario

### 3. Configurar el servicio

1. Render detectará automáticamente el archivo `render.yaml`
2. Se configurará automáticamente:
   - Base de datos PostgreSQL
   - Variables de entorno necesarias
   - Comandos de construcción y inicio

### 4. Variables de entorno en Render

Render configurará automáticamente estas variables:
- `DATABASE_URL` - Proporcionada por la base de datos PostgreSQL
- `SECRET_KEY` - Generada automáticamente
- `DEBUG` - Configurada como "False" para producción

### 5. Despliegue automático

Render ejecutará automáticamente:
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py collectstatic --noinput`
- `gunicorn sistema_bancario.wsgi:application`

### 6. Verificar el despliegue

Una vez desplegado, podrás acceder a tu aplicación en la URL proporcionada por Render.

### 📁 Estructura del Proyecto
```text
sistema-bancario/
├── auditoria/         # Módulo de auditoría de operaciones
├── cuentas/           # Lógica para cuentas bancarias
├── solicitudes/       # Gestión de solicitudes entre usuarios/cuentas
├── transacciones/     # Envío y recepción de dinero
├── usuarios/          # Registro y autenticación de usuarios
├── utils/             # Implementaciones de estructuras de datos
├── sistema_bancario/  # Configuración global del proyecto Django
├── manage.py          # Script de gestión del proyecto
├── requirements.txt   # Lista de dependencias
├── Procfile           # Configuración para Render
├── runtime.txt        # Versión de Python
├── render.yaml        # Configuración de Render
├── env.example        # Variables de entorno de ejemplo
└── .gitignore         # Archivos ignorados por Git
```