#Tutustu avoimeen OpenWeather-säärajapintaan:
# https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
# ja tulostaa sitä vastaavan säätilan tekstin
# sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen,
# jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
import requests
import json

hakusana = input("Paikkakunta: ")
api_key = "5da11975d5115d045c40fd4444d69e47"
url = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={api_key}"
vastaus = requests.get(url)
säätila = vastaus.json()
sää = säätila["weather"][0]["description"]

lampötila = säätila["main"]["temp"] - 273.15

print(f"Sää paikkakunnalla {hakusana}: {sää}")
print(f"Lämpötila on {lampötila:.1f} astetta")