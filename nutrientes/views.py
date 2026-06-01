import requests
from django.shortcuts import render


def nutrientes(request):
    # API DE FRUTAS (CALORÍAS)
    frutas_url = "https://www.fruityvice.com/api/fruit/all"
    frutas = []

    try:
        frutas_response = requests.get(frutas_url, timeout=10)
        frutas_response.raise_for_status()
        frutas = frutas_response.json()
    except Exception as e:
        print("Error frutas:", e)
        frutas = []

    # API DE RECETAS SALUDABLES (TheMealDB)
    recetas_url = "https://www.themealdb.com/api/json/v1/1/search.php?s=chicken"
    recetas = []

    try:
        recetas_response = requests.get(recetas_url, timeout=10)
        recetas_response.raise_for_status()
        data = recetas_response.json()
        recetas = data.get("meals", [])
    except Exception as e:
        print("Error recetas:", e)
        recetas = []

    return render(request, "nutrientes.html", {
        "frutas": frutas,
        "recetas": recetas
    })
