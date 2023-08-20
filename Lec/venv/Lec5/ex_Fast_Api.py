
from fastapi import FastAPI, Request
import logging
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
app = FastAPI(openapi_url="/api/v1/openapi.json")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

#pip install fastapi
#pip install "uvicorn[standard]"
#uvicorn ex_Fast_Api:app --reload
# посмотреть документацию /docs или /redoc (без тестирования)



class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


# @app.get("/")
# async def root():# карутина
#     return {"message": "Hello World"}


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None): #?q=txt
#     return {"item_id": item_id, "q": q}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# @app.get("/")
# async def read_root():
#     logger.info('Отработал GET запрос.')
#     return {"Hello": "World"}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World</h1>"


# @app.get("/message")
# async def read_message():
#     message = {"message": "Hello World"}
#     return JSONResponse(content=message, status_code=200)


@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "name": name})


@app.post("/items/")
async def create_item(item: Item): # post добавление новых данных
    logger.info('Отработал POST запрос.')
    return item


@app.put("/items/{item_id}")# put для изменения данных сущетвующих что и на что
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item id = {item_id}.')
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):# лучше не удалять а isactive True/False
    logger.info(f'Отработал DELETE запрос для item id = {item_id}.')
    return {"item_id": item_id}


...
@app.get("/users/{user_id}/orders/{order_id}")
async def read_item(user_id: int, order_id: int):
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit} # /items/?limit=25&skip=10


def custom_openapi():# внесение данных в документацию
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
        )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


# curl -X 'POST' 'http://127.0.0.1:8000/items/' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "BestSale", "description": "The best of the best", "price": 9.99, "tax": 0.99}'