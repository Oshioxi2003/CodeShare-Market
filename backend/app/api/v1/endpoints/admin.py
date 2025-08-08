from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_admin_user
from app.models.user import User
from app.models.product import Product
from app.models.transaction import Transaction

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
