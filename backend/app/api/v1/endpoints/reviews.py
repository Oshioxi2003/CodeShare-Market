from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_db
from app.models.review import Review
from app.schemas.review import ReviewBase

router = APIRouter()


@router.get("/product/{product_id}", response_model=List[ReviewBase])
async def list_reviews(product_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.product_id == product_id).order_by(Review.created_at.desc()).all()
    return reviews
