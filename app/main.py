from fastapi import FastAPI
from api.v1.endpoints import users, login
from app.core.database import Base, engine
from app.core.exception_handlers import register_exception_handlers

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)

Base.metadata.create_all(bind=engine)

# Registrando los hanlers de errroes
register_exception_handlers(app)


@app.get("/")
async def root():
    return {"message": "Welcome to the API! Check /docs for documentation."}
