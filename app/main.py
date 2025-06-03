from fastapi import FastAPI
from app.core.database import Base, engine
from models.user import User

app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
