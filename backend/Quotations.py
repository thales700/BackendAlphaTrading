import yfinance as yf
import pandas as pd
from Symbols import Symbols
from typing import Union, Optional

class Quotations:
    def __init__(self) -> None:
        self.symbolsValues = [key for key in Symbols.__members__.keys()]
    
    def _VerifySymbol(self, symbol: str) -> bool:
        return symbol in self.symbolsValues
    
    def Get(self, symbol: str, start_date: str, end_date: str) -> Union[pd.DataFrame, None]:
        if not self._VerifySymbol(symbol):
            return None
        else:
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=start_date, end=end_date)
            df = pd.DataFrame(data)
            return df

print(Quotations().Get(Symbols.AAPL.value, "2023-01-01", "2025-01-31"))