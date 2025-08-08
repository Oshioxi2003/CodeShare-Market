from datetime import datetime
from datetime import datetime

from pydantic import BaseModel

from app.models.transaction import PaymentMethod


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


class TransactionCreate(BaseModel):
    product_id: int
    payment_method: PaymentMethod


class PaymentInitResponse(BaseModel):
    transaction_id: str
    payment_url: str


class PaymentVerifyRequest(BaseModel):
    transaction_id: str
    status: str
