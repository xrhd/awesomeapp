from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from .models import calculate_vibe

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.post("/rate")
def rate_vibe(request: Request, name: str = Form(...), emoji: str = Form(...)):
    result = calculate_vibe(name, emoji)
    return templates.TemplateResponse(request=request, name="result.html", context={
        "score": result.score, 
        "message": result.message,
        "color_class": result.color_class
    })
