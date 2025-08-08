from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_db, get_current_active_user
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionBase
from app.models.user import User

router = APIRouter()


@router.get("/my/purchases", response_model=List[TransactionBase])
async def my_purchases(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    txs = db.query(Transaction).filter(Transaction.buyer_id == current_user.id).order_by(Transaction.created_at.desc()).all()
    return txs


@router.get("/my/sales", response_model=List[TransactionBase])
async def my_sales(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    txs = db.query(Transaction).filter(Transaction.seller_id == current_user.id).order_by(Transaction.created_at.desc()).all()
    return txs
