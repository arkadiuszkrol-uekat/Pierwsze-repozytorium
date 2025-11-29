import requests
from typing import List

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, address_1: str, city: str,
                 state_province: str, postal_code: str, country: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.website_url = website_url

    def __str__(self) -> str:
        return f"{self.name} ({self.brewery_type}) - {self.address_1}, {self.city}, {self.state_province}, {self.country} | {self.website_url}"

# ---- pobranie danych z API ----
url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # wyrzuci wyjątek, jeśli kod HTTP != 200
except requests.RequestException as e:
    print(f"Błąd połączenia z API: {e}")
    data = []
else:
    try:
        data = response.json()
    except ValueError:
        print("Błąd: odpowiedź z API nie jest poprawnym JSON-em")
        print("Odpowiedź API:", response.text)
        data = []

# ---- tworzenie obiektów Brewery ----
breweries: List[Brewery] = []

for item in data:
    brewery = Brewery(
        id=item.get("id", ""),
        name=item.get("name", ""),
        brewery_type=item.get("brewery_type", ""),
        address_1=item.get("address_1", ""),
        city=item.get("city", ""),
        state_province=item.get("state_province", ""),
        postal_code=item.get("postal_code", ""),
        country=item.get("country", ""),
        website_url=item.get("website_url", "")
    )
    breweries.append(brewery)

# ---- wyświetlenie obiektów ----
if breweries:
    for b in breweries:
        print(b)
else:
    print("Brak pobranych browarów.")