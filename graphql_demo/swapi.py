import json
import requests


def get_swapi_data(url): 
    response = requests.get(url)
    return response.json()


def get_characters_for_film(film): 
    character_urls = film['characters']
    characters = [get_swapi_data(url) for url in character_urls]
    return characters


def get_films(info): 
    films = get_swapi_data("https://swapi.dev/api/films/")['results']
    

    return films