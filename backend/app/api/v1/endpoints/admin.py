from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_db, get_current_admin_user
from app.models.user import User
from app.models.product import Product
from app.models.transaction import Transaction
from app.schemas.user import UserResponse
from app.schemas.product import ProductBase
from app.schemas.transaction import TransactionBase

router = APIRouter()


@router.get("/stats")
async def admin_stats(
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin_user),
):
    users = db.query(User).count()
    products = db.query(Product).count()
    sales = db.query(Transaction).count()
    return {"users": users, "products": products, "transactions": sales}


@router.get("/users", response_model=List[UserResponse])
async def admin_users(
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin_user),
):
    return db.query(User).order_by(User.created_at.desc()).all()


@router.get("/products", response_model=List[ProductBase])
async def admin_products(
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin_user),
):
    return db.query(Product).order_by(Product.created_at.desc()).all()


@router.get("/transactions", response_model=List[TransactionBase])
async def admin_transactions(
    db: Session = Depends(get_db),
    _admin: User = Depends(get_current_admin_user),
):
    return db.query(Transaction).order_by(Transaction.created_at.desc()).all()
