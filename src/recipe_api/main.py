import fastapi

import recipe_api
import recipe_api.database

recipe_api.database.Base.metadata.create_all(
    bind=recipe_api.database.engine
)

app = fastapi.FastAPI(
    title="Recipe API"
)

app.include_router(recipe_api.recipe_router)


@app.get("/")
async def root():
    return {"msg": "Welcome to the Recipe API"}
