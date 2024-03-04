from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    print(name)
    return ORJSONResponse({"message": f"{name}"})
