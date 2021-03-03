import graphene

class CourseType(graphene.ObjectType):
    id = graphene.String(required=True)
    title = graphene.String(required=True)
    instructor = graphene.String(required=True)
    publish_date = graphene.String()

class Film(graphene.ObjectType):
    title = graphene.String()
    episode_id = graphene.Int()
    opening_crawl = graphene.String(description="The opening paragraphs at the beginning of this film.")
    director = graphene.String()
    producers = graphene.List(graphene.String)
    release_date = graphene.String()

