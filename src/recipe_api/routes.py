
import fastapi
import sqlalchemy.orm

import recipe_api
import recipe_api.schemas

recipe_router = fastapi.APIRouter(
    prefix="/recipes",
    tags=["recipes"]
)

@recipe_router.get("/",
    response_model=list[recipe_api.schemas.Recipe]
)
async def read_recipes(
    skip: int = 0,
    limit: int = 100,
    db_session: sqlalchemy.orm.Session = fastapi.Depends(recipe_api.get_database)
):
    recipes = recipe_api.get_recipes(
        db_session,
        skip=skip,
        limit=limit
    )
    return recipes


@recipe_router.get("/{recipe_id}",
    response_model=recipe_api.schemas.Recipe
)
async def read_recipe(
    recipe_id: int,
    db_session: sqlalchemy.orm.Session = fastapi.Depends(recipe_api.get_database)
):
    db_recipe = recipe_api.get_recipe_by_id(
        db_session,
        recipe_id=recipe_id
    )
    if db_recipe is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"Recipe not found: {recipe_id}"
        )
    return db_recipe


@recipe_router.post("/",
    response_model=recipe_api.schemas.Recipe
)
async def add_new_recipe(
    recipe: recipe_api.schemas.RecipeCreate,
    db_session: sqlalchemy.orm.Session = fastapi.Depends(recipe_api.get_database)
):
    # db_recipe = recipe_api.get_recipe_by_id(db, recipe.id)
    # if db_recipe:
    #     raise fastapi.HTTPException(
    #         status_code=400,
    #         detail="Recipe already found"
    #     )
    return recipe_api.create_recipe(db_session, recipe)


@recipe_router.put("/{recipe_id}",
    response_model=recipe_api.schemas.Recipe
)
async def update_recipe(
    recipe_id: int,
    recipe: recipe_api.schemas.RecipeCreate,
    db_session: sqlalchemy.orm.Session = fastapi.Depends(recipe_api.get_database)
):
    """Update an existing recipe."""
    db_recipe = recipe_api.get_recipe_by_id(
        db_session,
        recipe_id=recipe_id
    )
    if db_recipe is None:
        raise fastapi.HTTPException(
            status_code=404,
            detail=f"Recipe not found: {recipe_id}"
        )
    db_recipe = recipe_api.update_recipe(
        db_session,
        recipe_id,
        recipe
    )
    return db_recipe

@recipe_router.delete("/{recipe_id}")
async def remove_recipe(
    recipe_id: int,
    db_session: sqlalchemy.orm.Session = fastapi.Depends(recipe_api.get_database)
):
    """Remove a recipe row in the database."""
    recipe_api.delete_recipe_by_id(
        db_session,
        recipe_id=recipe_id
    )
    return {"msg": f"Recipe deleted: {recipe_id}"}
