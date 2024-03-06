from fastapi import FastAPI
from api.routes import users

app = FastAPI()

app.include_router(users.router)
for route in app.routes:
    print(route)


@app.get("/health")
async def health():
    return "ok"
