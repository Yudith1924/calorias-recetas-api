import requests

FRUITYVICE_URL = "https://www.fruityvice.com/api/fruit/all"

def get_all_fruits():
    try:
        response = requests.get(FRUITYVICE_URL, timeout=10)

        if response.status_code != 200:
            return []

        return response.json()

    except Exception:
        return []
