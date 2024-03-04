import json
from typing import Union

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse, JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/", response_class=JSONResponse)
async def root():
    oo = {"hello": "world"}
    return json.dumps(oo)


class Item(BaseModel):
    name: str
    email: Union[str, None] = None
    age: int


@app.post(
    "/items/",
    response_model=Item,
    response_class=ORJSONResponse,
    summary="Create an item",
)
async def create_item(item: Item):
    return item
