from fastapi import FastAPI
from graphene import ObjectType, List, Schema, Field, Mutation, Int, Argument
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from .schemas import Film, AddFilmInput
import graphql_demo.db as db
from .helper import get_fields


class DemoQuery(ObjectType):
    films = Field(
        List(Film),
        episode_ids=List(Int),
        description="Get films in the Lucas-era Star Wars franchise",
    )

    async def resolve_films(self, info, episode_ids=[]):
        films = db.get_films()
        requested_fields = get_fields(info)

        if len(episode_ids) > 0:
            films = [film for film in films if film["episode_id"] in episode_ids]

        if "characters" in requested_fields:
            for f in films:
                f["characters"] = db.get_characters_for_film(f)

        return films


class AddFilm(Mutation):
    film = Field(Film)

    class Arguments:
        film = Argument(AddFilmInput)

    async def mutate(self, info, film):
        new_film = db.add_film(film)
        return AddFilm(film=new_film)


class DemoMutation(ObjectType):
    add_film = AddFilm.Field()


# swapi.create_films_db()
# swapi.create_characters_db()


app = FastAPI()
app.add_route(
    "/",
    GraphQLApp(
        schema=Schema(query=DemoQuery, mutation=DemoMutation),
        executor_class=AsyncioExecutor,
    ),
)
