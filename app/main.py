from fastapi import FastAPI
from api.v1.endpoints import users
from app.core.database import Base, engine
from models.user import User

app = FastAPI()

app.include_router(users.router)
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Welcome to the API! Check /docs for documentation."}
