from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q: # проверяем не на соответствия условиям, а был ли передан параметр, проверяет на условия fastapi сам
        results.update({"q": q}) # q необязательный парамаетр, если не передать - все ок
    return results


# @app.get("/items/")
# async def read_items(q: str = Query(..., min_length=3)): # так параметр q обязательный ...
#     results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
#     if q:
#         results.update({"q": q})
#     return results

# все наследуется от Param:

# в моделях Filed
# если часть строки адреса Path
# если пара ключ: занчение Query


if __name__ == '__main__':
    uvicorn.run(
    "ex_query:app",
    reload=True
    )
