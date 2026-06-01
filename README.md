![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-Fruityvice-orange?style=for-the-badge)
![API](https://img.shields.io/badge/API-TheMealDB-red?style=for-the-badge)

# Calorías y Recetas API

Plataforma web enfocada en el bienestar nutricional, diseñada para la consulta rápida de valor calórico en frutas y la exploración de recetas saludables. Desarrollada sobre **Django 5.2**, la aplicación integra servicios externos vía API REST para proporcionar datos precisos en tiempo real, ofreciendo una experiencia de usuario fluida, moderna y orientada a la vida saludable.

---

## Arquitectura y Características del Sistema

### Lógica de Negocio e Integración

* **Motor de Consumo de APIs (Fruityvice & TheMealDB):** Implementación de servicios dedicados para la recuperación asíncrona de datos nutricionales y catálogo de recetas saludables.
* **Arquitectura de Servicios (`services/`):** Separación de lógica de negocio mediante módulos de servicios, permitiendo una gestión limpia de las peticiones a las APIs externas y el procesamiento de respuestas.
* **Diseño Visual Inspirado en Bienestar:** Interfaz web intuitiva con un enfoque en la legibilidad y la facilidad de uso para el usuario final al buscar alternativas alimenticias.
* **Gestión de Datos Nutricionales:** Estructura de modelos optimizada para el procesamiento, filtrado y presentación de información alimenticia clave.

---

## Demostración Visual
<div align="center">
  <video src="https://github.com/user-attachments/assets/abb6ab2b-5d5d-4e53-94ae-528889390ab2" width="100%" controls></video>
</div>

### Interfaces del Sistema

| Catálogo de Frutas | Catálogo de Recetas Saludables |
| --- | --- |
| <img width="922" height="671" alt="Captura de pantalla 2026-06-01 103029" src="https://github.com/user-attachments/assets/85d7099b-4b00-4817-8b9b-7825e6e5ac6e" /> | <img width="921" height="676" alt="Captura de pantalla 2026-06-01 103053" src="https://github.com/user-attachments/assets/90d33ab6-9da1-4db0-b97b-41807577dcf4" />

---

## Stack Tecnológico

* **Framework:** Django 5.2
* **Lenguaje:** Python 3.13
* **Integración de Datos:** Consumo de APIs (REST)
* **Frontend:** HTML5, CSS3, JavaScript
* **Servidor de Desarrollo:** Django Development Server

---

## Instalación y Configuración

Siga estos pasos para clonar y ejecutar el entorno de desarrollo:

### 1. Clonar el repositorio

```bash
git clone https://github.com/Yudith1924/calorias-recetas-api.git
cd calorias-recetas-api

```

### 2. Configurar entorno y dependencias

```bash
# Crear entorno virtual
python -m venv venv
# Activar entorno (Windows)
venv\Scripts\activate
# Instalar dependencias
pip install -r requirements.txt

```

### 3. Ejecución

```bash
python manage.py runserver

```
