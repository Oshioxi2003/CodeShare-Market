from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    id: int
    rating: int
    title: Optional[str] = None
    comment: str
    product_id: int
    reviewer_id: int
    created_at: datetime

    class Config:
        from_attributes = True
