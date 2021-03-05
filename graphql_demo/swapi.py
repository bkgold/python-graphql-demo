import json
import requests


def get_swapi_data(url): 
    response = requests.get(url)
    return response.json()


def create_films_db(): 
    films = get_films()
    with open('films.json', 'w') as out:
        json.dump(films, out, indent=4)


def create_characters_db(): 
    response = get_swapi_data("https://swapi.dev/api/people/")
    characters = response['results']
    _, all_characters = get_all_results(response, characters)
    with open('characters.json', 'w') as out:
        json.dump(all_characters, out, indent=4)


def get_characters_for_film(film): 
    characters = None
    with open("./characters.json") as c:
      characters = json.load(c)
    return [c for c in characters if c['url'] in film['characters']]


def get_films(): 
    films = None
    with open("./films.json") as films:
      films = json.load(films)
    return films
    


def get_all_results(response, results):
    if response['next']:
        response = get_swapi_data(response['next'])
        results += response['results']
        return get_all_results(response, results)
    else: 
        return response, results
