import json


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
    films = None
    with open("./films.json", "r+") as fs:
        films = json.load(fs)

        for existing_film in films:
            if film["episode_id"] == existing_film["episode_id"]:
                raise Exception(f"Episode {film.episode_id} already exists!")

        films.append(film)
        fs.seek(0)
        json.dump(films, fs, indent=4)
    return films[-1]
