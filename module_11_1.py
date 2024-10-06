import requests

"""Requests — это библиотека в Python, которая позволяет взаимодействовать с веб-ресурсами и глобальной сетью.
Она предоставляет разработчику обширный пул функций для работы со всеми видами HTTP-запросов."""

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")