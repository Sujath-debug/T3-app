from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import engine
from . import models
from .routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    models.Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router, tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "BSML RUNNING!"}

@app.get("/health")
def health():
    return {"status": "healthy"}
