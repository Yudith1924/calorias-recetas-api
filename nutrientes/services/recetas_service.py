import requests

THEMEALDB_URL = "https://www.themealdb.com/api/json/v1/1/search.php"

HEADERS = {
    "User-Agent": "Django-App/1.0"
}

def get_recipes(query="chicken"):
    """
    Obtiene recetas saludables desde TheMealDB
    """
    try:
        response = requests.get(
            THEMEALDB_URL,
            params={
                "s": query
            },
            headers=HEADERS,
            timeout=10
        )

        if response.status_code != 200:
            return []

        data = response.json()
        return data.get("meals", []) or []

    except Exception as e:
        print("Error TheMealDB:", e)
        return []
