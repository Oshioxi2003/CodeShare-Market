from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.models.product import ProductCategory
from app.schemas.product import CategoryBase, CategoryListResponse

router = APIRouter()


@router.get("/", response_model=CategoryListResponse)
async def list_categories(db: Session = Depends(get_db)):
    items = db.query(ProductCategory).order_by(ProductCategory.name.asc()).all()
    return {"items": items, "total": len(items)}
