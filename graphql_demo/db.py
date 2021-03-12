import json
import requests


def get_characters_for_film(film):
    characters = None
    with open("./characters.json") as cs:
        characters = json.load(cs)
    return [c for c in characters if c["url"] in film["characters"]]


def get_films():
    films = None
    with open("./films.json") as fs:
        films = json.load(fs)
    return films


def add_film(film):
    with open("./films.json", "r+") as fs:
        films = json.load(fs)
        print(film)
        films.append(film)
        fs.seek(0)
        json.dump(films, fs, indent=4)
    return films[-1]


def get_all_results(response, results):
    if response["next"]:
        response = get_swapi_data(response["next"])
        results += response["results"]
        return get_all_results(response, results)
    else:
        return response, results
