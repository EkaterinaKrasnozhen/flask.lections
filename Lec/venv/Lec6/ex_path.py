from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


# @app.get("/items/{item_id}") # item id часть пути поэтому path
# async def read_item(item_id: int = Path(..., ge=1)):
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q} # path только для части пути


if __name__ == '__main__':
    uvicorn.run(
    "ex_path:app",
    reload=True
    )