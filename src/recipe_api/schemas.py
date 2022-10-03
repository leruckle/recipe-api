import pydantic




class RecipeBase(pydantic.BaseModel):
    name: str
    body: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
