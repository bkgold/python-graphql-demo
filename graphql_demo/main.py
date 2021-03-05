from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema, Field, Int
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from .schemas import Film
import graphql_demo.swapi as swapi
from .helper import get_fields


class Query(ObjectType):
    all_films = Field(List(Film), description="Get all films in the OG Star Wars franchise")
    async def resolve_all_films(self, info):
        return swapi.get_films()   

    films = Field(List(Film), episodes=List(Int), description="Get films by episode")
    async def resolve_films(self, info, episodes=[]):
        films = swapi.get_films()   
        requested_fields = get_fields(info)

        if len(episodes) > 0:
            films = [film for film in films if film['episode_id'] in episodes]
        
        if ('characters' in requested_fields):
            for f in films: 
                f['characters'] = swapi.get_characters_for_film(f)
        
        return films
    
# swapi.create_films_db()
# swapi.create_characters_db()

app = FastAPI()
app.add_route("/", GraphQLApp(
  schema=Schema(query=Query),
  executor_class=AsyncioExecutor)
)
