import graphene
from graphene import ObjectType

class Character(ObjectType):
    name = graphene.String()
    birth_year = graphene.String()
    eye_colour = graphene.String()
    gender = graphene.String()
    hair_colour = graphene.String()
    height = graphene.Int()
    mass = graphene.Float()
    skin_color = graphene.String()
    # homeworld = Planet

class Film(ObjectType):
    title = graphene.String(required=True)
    episode_id = graphene.Int(required=True)
    opening_crawl = graphene.String(description="The opening paragraphs at the beginning of the film.")
    director = graphene.String()
    producers = graphene.List(graphene.String)
    release_date = graphene.String()
    characters = graphene.List(Character)
