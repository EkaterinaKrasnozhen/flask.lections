#pip install databases[aiosqlite]
# CRUD: create, read, update, delete

from typing import List
import databases
from pydantic import BaseModel, Field
import sqlalchemy
from fastapi import FastAPI
import uvicorn

DATABASE_URL = "sqlite:///mydatabase.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), # первичный ключ авто 1, 2 ,3
    sqlalchemy.Column("name", sqlalchemy.String(32)), # строка не более 32 симовла
    sqlalchemy.Column("email", sqlalchemy.String(128)),
    )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) # движок, словарь нужен для работы с бд sqlite, ЕСЛИ MSQL И ТД connect args не нужно
metadata.create_all(engine) # формируем таблицы

app = FastAPI()


@app.on_event("startup")# сработает по событию start up
async def startup():
    await database.connect() # асинхронный запрос


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    

class UserIn(BaseModel):
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


class User(BaseModel):
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)


# @app.get("/fake_users/{count}") # в настоящих проектах так не делать чтобы не хакнули
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email) # модель pydentic через . свойства
    query = users.insert().values(**user.model_dump()) # делает тоже что строкой выше
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query) # верни всех


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump()) # вместо dict() dump
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id) # в таблице польз колонка с id как у user_id
    return await database.fetch_one(query)# верни одного


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


if __name__ == '__main__':
    uvicorn.run(
    "data_base:app",
    reload=True
    )