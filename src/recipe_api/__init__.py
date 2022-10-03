# type: ignore  # <- this handles 'Not Accessed' errors in linter

import recipe_api.schemas

import recipe_api.database
from recipe_api.database import (
    Base,
    get_database
)

import recipe_api.models

import recipe_api.routes
from recipe_api.routes import (
    recipe_router
)

import recipe_api.crud
from recipe_api.crud import (
    get_recipe_by_id,
    get_recipes,
    create_recipe,
    delete_recipe_by_id,
    update_recipe
)
