"""Helper functions to provide create, read, update, and delete actions with the database.

"""
import sqlalchemy.orm

import recipe_api.models
import recipe_api.schemas


def get_recipe_by_id(
    db_session: sqlalchemy.orm.Session,
    recipe_id: int
):
    """Querries and returns recipe specified by its id."""
    to_return = db_session.query(
        recipe_api.models.Recipe
    ).filter(
        recipe_api.models.Recipe.id == recipe_id
    ).first()
    return to_return

def get_recipes(
    db_session: sqlalchemy.orm.Session,
    skip: int = 0,
    limit: int = 100
):
    """Querries and returns all the recipes in the database."""
    return db_session.query(
        recipe_api.models.Recipe
    ).offset(
        skip
    ).limit(
        limit
    ).all()

def create_recipe(
    db_session: sqlalchemy.orm.Session,
    recipe: recipe_api.schemas.RecipeCreate
):
    """Creates a new recipe row in the database."""
    db_recipe = recipe_api.models.Recipe(
        name = recipe.name,
        body = recipe.body
    )
    db_session.add(db_recipe)
    db_session.commit()
    db_session.refresh(db_recipe)
    return db_recipe

def delete_recipe_by_id(
    db_session: sqlalchemy.orm.Session,
    recipe_id: int
):
    """Deletes a recipe out of the database"""
    db_session.query(
        recipe_api.models.Recipe
    ).filter(
        recipe_api.models.Recipe.id == recipe_id
    ).delete(
        synchronize_session=False
    )
    db_session.commit()

def update_recipe(
    db_session: sqlalchemy.orm.Session,
    recipe_id: int,
    recipe: recipe_api.schemas.RecipeCreate
):
    """Updates an existing recipe row in the database."""
    id_querry = db_session.query(
        recipe_api.models.Recipe
    ).filter(
        recipe_api.models.Recipe.id == recipe_id
    )
    id_querry.update(
        {
            "name": recipe.name,
            "body": recipe.body
        }
    )
    db_session.commit()
    db_recipe = id_querry.first()
    return db_recipe
    