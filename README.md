# Calorías y Recetas API

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-Fruityvice-orange?style=for-the-badge)
![API](https://img.shields.io/badge/API-TheMealDB-red?style=for-the-badge)

Plataforma web enfocada en el bienestar nutricional, diseñada para la consulta rápida de valor calórico en frutas y la exploración de recetas saludables. Desarrollada sobre **Django 5.2**, la aplicación integra servicios externos vía API REST para proporcionar datos precisos en tiempo real, ofreciendo una experiencia de usuario fluida, moderna y orientada a la vida saludable.

---

## Arquitectura y Características

* **Motor de Consumo de APIs:** Integración eficiente con *Fruityvice* y *TheMealDB* para la recuperación asíncrona de datos nutricionales y recetas.
* **Arquitectura de Servicios (`services/`):** Separación de lógica mediante módulos dedicados, garantizando un código limpio y fácil de mantener.
* **Diseño Orientado al Usuario:** Interfaz intuitiva y legible, facilitando la búsqueda de alternativas alimenticias de forma rápida.
* **Gestión de Datos:** Modelos optimizados para el procesamiento y filtrado de información nutricional clave.

---

## Demostración Visual

<video src="https://github.com/user-attachments/assets/abb6ab2b-5d5d-4e53-94ae-528889390ab2" width="100%" controls></video>

### Interfaces del Sistema

| Catálogo de Frutas | Catálogo de Recetas Saludables |
| :---: | :---: |
| ![Frutas](https://github.com/user-attachments/assets/85d7099b-4b00-4817-8b9b-7825e6e5ac6e) | ![Recetas](https://github.com/user-attachments/assets/90d33ab6-9da1-4db0-b97b-41807577dcf4) |

---

## Instalación y Configuración

Sigue estos pasos para clonar y ejecutar el entorno de desarrollo:

1. **Clonar el repositorio:**
```bash
   git clone [https://github.com/Yudith1924/calorias-recetas-api.git](https://github.com/Yudith1924/calorias-recetas-api.git)
   cd calorias-recetas-api

```

2. **Configurar entorno y dependencias:**
```bash
python -m venv venv
# Activar en Windows:
venv\Scripts\activate

# Instalar dependencias:
pip install -r requirements.txt

```


3. **Migraciones:**
```bash
python manage.py migrate

```


4. **Ejecución:**
```bash
python manage.py runserver

```



---

## Stack Tecnológico

* **Framework:** Django 5.2
* **Lenguaje:** Python 3.13
* **Integración:** REST APIs (Fruityvice, TheMealDB)
* **Frontend:** HTML5, CSS3, JavaScript
* **Servidor:** Django Development Server
