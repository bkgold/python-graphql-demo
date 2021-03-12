import json
import requests


def get_swapi_data(url):
    response = requests.get(url)
    return response.json()


def get_all_results(response, results):
    if response["next"]:
        response = get_swapi_data(response["next"])
        results += response["results"]
        return get_all_results(response, results)
    else:
        return response, results


def create_films_db():
    films = get_swapi_data("https://swapi.dev/api/films/")["results"]
    with open("films.json", "w") as out:
        json.dump(films, out, indent=4)


def create_characters_db():
    response = get_swapi_data("https://swapi.dev/api/people/")
    characters = response["results"]
    _, all_characters = get_all_results(response, characters)
    with open("characters.json", "w") as out:
        json.dump(all_characters, out, indent=4)
