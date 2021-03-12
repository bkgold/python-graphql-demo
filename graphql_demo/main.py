from fastapi import FastAPI
from graphene import ObjectType, List, Schema, Field, Mutation, Int, Argument
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from .schemas import Film, AddFilmInput
import graphql_demo.swapi as swapi
from .helper import get_fields


class DemoQuery(ObjectType):
    # This is the name of our query
    all_films = Field(
        List(Film), description="Get all films in the OG Star Wars franchise"
    )
    # Resolver method must be prefixed with `resolve_` followed by the query name
    async def resolve_all_films(self, info):
        return swapi.get_films()

    films = Field(List(Film), episodes=List(Int), description="Get films by episode")
    # The resolver method takes 2 positional arguments. The interesting one here is `info`. We can use the `info` argument to get the requested fields so we don't overfetch.
    async def resolve_films(self, info, episodes=[]):
        films = swapi.get_films()
        requested_fields = get_fields(info)

        if len(episodes) > 0:
            films = [film for film in films if film["episode_id"] in episodes]

        if "characters" in requested_fields:
            for f in films:
                f["characters"] = swapi.get_characters_for_film(f)

        return films


class AddFilm(Mutation):
    # This is what we return to the user on success
    film = Field(Film)

    class Arguments:
        film = Argument(AddFilmInput)

    async def mutate(self, info, film):
        new_film = swapi.add_film(film)
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
