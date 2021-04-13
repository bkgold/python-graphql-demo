# Python GraphQL Demo

This repo is an example of a simple GraphQL API Python server. This demo uses the the [Star Wars API](https://swapi.dev/) as a sample data source. 

This demo uses:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Graphene](https://graphene-python.org/)

## Follow along with the demo

1. Create a new project
```
poetry new swapi-graphql
cd swapi-graphql
```
2. Add fastAPI, graphene and uvicorn to your project
```
poetry add fastapi graphene uvicorn
```
3. Create film schema
```
import graphene
from graphene import ObjectType

class Film(ObjectType):
    title = graphene.String(required=True)
    episode_id = graphene.Int(required=True)
    opening_crawl = graphene.String(description="The opening paragraphs at the beginning of the film.")
    director = graphene.String()
    producer = graphene.String()
    release_date = graphene.String()
```
4. Create film query to return all films
```
from graphene import ObjectType, Field, List
from .schema import Film
import swapi_graphql.db as db


class Query(ObjectType):
    films = Field(
        List(Film), description="Get films in the Lucas-era Star Wars franchise"
    )

    async def resolve_films(self, info):
        return db.get_films()
```
5. Set up FastApi and GraphQL
```
from fastapi import FastAPI
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from graphene import Schema, ObjectType, Field, List

app = FastAPI()
app.add_route(
    "/graphql", GraphQLApp(schema=Schema(query=Query), executor_class=AsyncioExecutor)
)
```
6. Run the server using uvicorn
```
uvicorn swapi_graphql.main:app --reload
```
7. Add a filter to the films query
```
class Query(ObjectType):
    films = Field(
        List(Film),
        episode_ids=List(Int),
        description="Get films in the Lucas-era Star Wars franchise",
    )

    async def resolve_films(self, info, episode_ids=[]):
        films = db.get_films()

        if episode_ids:
            films = [film for film in films if film["episode_id"] in episode_ids]

        return films
```
8. Update Film schema to have a list of characters
```
class Character(ObjectType):
    name = graphene.String()
    birth_year = graphene.String()
    eye_color = graphene.String()
    gender = graphene.String()
    hair_colour = graphene.String()
    height = graphene.Int()
    mass = graphene.Float()
    skin_color = graphene.String()

class Film(ObjectType):
    ...
    characters = graphene.List(Character)
```
9. Return characters in films query
```
async def resolve_films(self, info, episodes=[]):
    ...
    for f in films:
        f["characters"] = db.get_characters_for_film(f)
```
10. Mutation!
```
class AddFilm(Mutation):
    film = Field(Film)

    class Arguments:
        film = Argument(AddFilmInput)

    async def mutate(self, info, film):
        new_film = db.add_film(film)
        return AddFilm(film=new_film)

class AddFilmInput(InputObjectType):
    title = graphene.String(required=True)
    episode_id = graphene.Int(required=True)
    opening_crawl = graphene.String()
    director = graphene.String()
    producer = graphene.String()
    release_date = graphene.String()

mutation {
  addFilm(film: {title: "The Force Awakens", episodeId: 7, director: "J. J. Abrams", producer: "Kathleen Kennedy", releaseDate: "2015-12-18", openingCrawl: "Luke Skywalker has vanished.\r\nIn his absence, the sinister\r\nFIRST ORDER has risen from\r\nthe ashes of the Empire\r\nand will not rest until\r\nSkywalker, the last Jedi,\r\nhas been destroyed.\r\n\r\nWith the support of the\r\nREPUBLIC, General Leia Organa\r\nleads a brave RESISTANCE.\r\nShe is desperate to find her\r\nbrother Luke and gain his\r\nhelp in restoring peace\r\nand justice to the galaxy.\r\n\r\nLeia has sent her most daring\r\npilot on a secret mission\r\nto Jakku, where an old ally\r\nhas discovered a clue to\r\nLuke's whereabouts...."}) {
    film {
      title
      episodeId
    }
  }
}
```
11. Error handling
```
for existing_film in films:
    if film["episode_id"] == existing_film["episode_id"]:
        raise Exception(f"Episode {film.episode_id} already exists!")

```
