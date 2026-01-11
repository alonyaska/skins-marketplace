from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app.Market.router import get_all_market


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates =Jinja2Templates(directory="app/templates")

@router.get("/market")
async  def get_market_page(
        request: Request,
        markets=Depends(get_all_market)

):
    return  templates.TemplateResponse(
        name="Market.html",
        context={"request": request, "markets": markets}
    )