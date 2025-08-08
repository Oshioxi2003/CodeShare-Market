from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from app.core.deps import get_db, get_current_seller_user, PaginationParams
from app.models.product import Product
from app.schemas.product import ProductBase, ProductDetail, ProductListResponse, ProductCreate

router = APIRouter()


@router.get("/", response_model=ProductListResponse)
async def list_products(
    db: Session = Depends(get_db),
    pagination: PaginationParams = Depends(),
    q: Optional[str] = None,
    category_id: Optional[int] = None,
):
    query = db.query(Product)
    if q:
        query = query.filter(Product.title.ilike(f"%{q}%"))
    if category_id:
        query = query.filter(Product.category_id == category_id)

    total = query.count()
    items = (
        query.order_by(Product.created_at.desc())
        .offset(pagination.skip)
        .limit(pagination.limit)
        .all()
    )
    return {"items": items, "total": total, "page": pagination.page, "page_size": pagination.page_size}


@router.get("/{product_id}", response_model=ProductDetail)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@router.post("/", response_model=ProductDetail, status_code=status.HTTP_201_CREATED)
async def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    _seller=Depends(get_current_seller_user),
):
    product = Product(
        title=data.title,
        slug=data.title.lower().replace(" ", "-"),
        description=data.description,
        price=data.price,
        currency=data.currency,
        seller_id=_seller.id,
        category_id=data.category_id,
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
