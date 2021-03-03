from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Field
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from .schemas import Film
import json
import requests

class Query(ObjectType):
  films = None
  films = List(Film, description="Get all films from the Star Wars franchise")

  async def resolve_films(self, info):
    response = requests.get("https://swapi.dev/api/films/")
    films = response.json()['results']
    return films

app = FastAPI()
app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
