from fastapi import FastAPI
from api.v1.endpoints import users, login, post
from app.core.database import Base, engine
from app.core.exception_handlers import register_exception_handlers

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(post.router)

# Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup_event():
    print("Creando tablas de base de datos...")
    # Para SQLAlchemy 1.x síncrono:
    Base.metadata.create_all(bind=engine)
    # Para SQLAlchemy 2.0+ asíncrono (si usas AsyncEngine):
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    print("Tablas creadas (o ya existentes).")


# Registrando los hanlers de errroes
register_exception_handlers(app)


@app.get("/")
async def root():
    return {"message": "Welcome to the API! Check /docs for documentation."}
