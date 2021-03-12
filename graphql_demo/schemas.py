import graphene
from graphene import ObjectType, InputObjectType

class Character(ObjectType):
    name = graphene.String()
    birth_year = graphene.String()
    eye_colour = graphene.String()
    gender = graphene.String()
    hair_colour = graphene.String()
    height = graphene.Int()
    mass = graphene.Float()
    skin_color = graphene.String()

# This is how we use the SDL to define our Film type
# We have a number of fields similar to those in the SWAPI REST API
# And we have given these types (at this point all of type String)
class Film(ObjectType):
    title = graphene.String(required=True)
    episode_id = graphene.Int(required=True)
    opening_crawl = graphene.String(description="The opening paragraphs at the beginning of the film.")
    director = graphene.String()
    producer = graphene.String()
    release_date = graphene.String()
    characters = graphene.List(Character)

class AddFilmInput(InputObjectType):
    title = graphene.String(required=True)
    episode_id = graphene.Int(required=True)
    opening_crawl = graphene.String()
    director = graphene.String()
    producer = graphene.String()
    release_date = graphene.String()