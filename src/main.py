from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .controllers import router
from .models import load_data
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_data()
    yield

app = FastAPI(title="Awesome App", lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
