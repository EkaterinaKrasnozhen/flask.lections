from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(max_length=10)
    

class User(BaseModel):
    age: int = Field(default=0)