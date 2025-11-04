import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.HiddenMarkovModel import HiddenMarkovModel
from schemas.symbol_properties import SymbolProperties
from entities.Granularity import Granularity

print(HiddenMarkovModel.GetRegimes(
    symbolInfos=SymbolProperties(
        symbol="AAPL",
        start_date="2020-01-01",
        end_date="2020-10-31",
        granularity=Granularity.ONE_DAY
    ),
    n_regimes=3
))