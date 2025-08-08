from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TransactionBase(BaseModel):
    id: int
    transaction_id: str
    amount: float
    currency: str
    status: str
    product_id: int
    buyer_id: int
    seller_id: int
    created_at: datetime

    class Config:
        from_attributes = True
