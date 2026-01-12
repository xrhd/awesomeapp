from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from .models import search_quotes

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def get_home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/search")
def search(request: Request, q: str = Query("")):
    results = search_quotes(q)
    return templates.TemplateResponse(request=request, name="quote_card.html", context={
        "quotes": results
    })
