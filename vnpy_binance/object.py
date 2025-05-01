from dataclasses import dataclass
from datetime import datetime as Datetime
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.object import BaseData


@dataclass
class FundingRateData(BaseData):
    """
    Funding rate data of a certain futures contract.
    """

    symbol: str
    exchange: Exchange
    datetime: Datetime

    funding_rate: float
    price: float

    def __post_init__(self) -> None:
        """"""
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"
