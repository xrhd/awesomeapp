from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .controllers import router

app = FastAPI(title="VibeRoast")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)
