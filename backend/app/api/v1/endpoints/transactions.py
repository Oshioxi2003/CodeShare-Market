from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_active_user
from app.models.transaction import (
    Transaction,
    PaymentMethod,
    TransactionStatus,
)
from app.models.product import Product
from app.schemas.transaction import (
    TransactionBase,
    TransactionCreate,
    PaymentInitResponse,
    PaymentVerifyRequest,
)
from app.models.user import User
from app.services import payment
from app.core.config import settings

router = APIRouter()


@router.get("/my/purchases", response_model=List[TransactionBase])
async def my_purchases(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    txs = db.query(Transaction).filter(Transaction.buyer_id == current_user.id).order_by(Transaction.created_at.desc()).all()
    return txs


@router.get("/my/sales", response_model=List[TransactionBase])
async def my_sales(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    txs = db.query(Transaction).filter(Transaction.seller_id == current_user.id).order_by(Transaction.created_at.desc()).all()
    return txs


@router.post("/create", response_model=PaymentInitResponse)
async def create_transaction(
    payload: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    product = db.query(Product).filter(Product.id == payload.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    transaction = Transaction(
        transaction_id=str(uuid4()),
        amount=product.price,
        currency=product.currency,
        product_id=product.id,
        buyer_id=current_user.id,
        seller_id=product.seller_id,
        payment_method=payload.payment_method,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return_url = f"{settings.FRONTEND_URL}/payments/return"
    if payload.payment_method == PaymentMethod.VNPAY:
        payment_url = payment.create_vnpay_payment(
            transaction.transaction_id, transaction.amount, return_url
        )
    else:
        res = payment.create_paypal_payment(
            transaction.transaction_id, transaction.amount, return_url, return_url
        )
        payment_url = res["approval_url"]

    return {
        "transaction_id": transaction.transaction_id,
        "payment_url": payment_url,
    }


@router.post("/verify")
async def verify_transaction(
    payload: PaymentVerifyRequest,
    db: Session = Depends(get_db),
):
    transaction = (
        db.query(Transaction)
        .filter(Transaction.transaction_id == payload.transaction_id)
        .first()
    )
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    transaction.status = (
        TransactionStatus.COMPLETED
        if payload.status == "success"
        else TransactionStatus.FAILED
    )
    db.commit()
    return {"status": transaction.status}
