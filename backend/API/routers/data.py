from fastapi import APIRouter
from Services.Quotations import Quotations

router = APIRouter()
@router.get("/data/{symbol}")
def get_data(symbol: str, start_date: str, end_date: str, granularity: str):
    return {"symbol": symbol, "start_date": start_date, "end_date": end_date, "granularity": granularity}