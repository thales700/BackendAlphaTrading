from pydantic import BaseModel
from Entities.Granularity import Granularity


class SymbolProperties(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    granularity: Granularity
