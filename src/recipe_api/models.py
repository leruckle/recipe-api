"""The ORM for the database.
"""

import sqlalchemy
import sqlalchemy.orm

import recipe_api

class Recipe(recipe_api.Base):
    """Top-level database model for recipes.
    """
    __tablename__ = "recipes"
    id   = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    body = sqlalchemy.Column(sqlalchemy.String)
