from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Field, Int
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from .schemas import Film
import graphql_demo.swapi as swapi

class Query(ObjectType):
    all_films = None
    all_films = List(Film, description="Get all films from the Star Wars franchise")
    async def resolve_all_films(self, info):
        return swapi.get_films(info)


    films = Field(List(Film), episodes=List(Int), description="Get films by episode")
    async def resolve_films(self, info, episodes=[]):
        films = swapi.get_films(info)
        if not episodes:
            return films
        else:
            return [film for film in films if film['episode_id'] in episodes]
    

app = FastAPI()
app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
