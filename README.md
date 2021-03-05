# python-graphql-demo

1. Add fastAPI and graphene to project
2. Create "database" of star wars knowledge
3. Create film schema
4. Create film query to return all films
5. Set up FastApi and GraphQL
    ```
    app = FastAPI()
    app.add_route("/", GraphQLApp(
        schema=Schema(query=Query),
        executor_class=AsyncioExecutor)
    )
    ```
6. Run: 
    ```
    uvicorn graphql_demo.main:app --reload
    ```
7. Add input/filter to films query
8. Update Film schema to have a list of characters
9. Add characters to film query
10. Mutation!


```
mutation {
  addFilm(film: {title: "The Force Awakens", episodeId: 7, director: "J. J. Abrams", producer: "Kathleen Kennedy", releaseDate: "2015-12-18", openingCrawl: "Luke Skywalker has vanished.\r\nIn his absence, the sinister\r\nFIRST ORDER has risen from\r\nthe ashes of the Empire\r\nand will not rest until\r\nSkywalker, the last Jedi,\r\nhas been destroyed.\r\n\r\nWith the support of the\r\nREPUBLIC, General Leia Organa\r\nleads a brave RESISTANCE.\r\nShe is desperate to find her\r\nbrother Luke and gain his\r\nhelp in restoring peace\r\nand justice to the galaxy\r\n\r\nLeia has sent her most daring\r\npilot on a secret mission\r\nto Jakku, where an old ally\r\nhas discovered a clue to\r\nLuke's whereabouts.…"}) {
    film {
      title
      episodeId
    }
  }
}
```