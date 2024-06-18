from fastapi import FastAPI

from routes import users, root


def create_app():
    ap = FastAPI()

    # set routes
    ap.include_router(root.router)
    ap.include_router(users.router)
    return ap


app = create_app()
