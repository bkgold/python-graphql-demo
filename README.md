# python-graphql-demo

1. Create temporary database
2. Set up FastApi and GraphQL
    ```
    app = FastAPI()
    app.add_route("/", GraphQLApp(
        schema=Schema(query=Query),
        executor_class=AsyncioExecutor)
    )
    ```


Run: 
```
uvicorn graphql_demo.main:app --reload
```