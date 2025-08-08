from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, HttpUrl


class CategoryBase(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    id: int
    title: str
    slug: str
    price: float
    currency: str
    rating: Optional[float] = 0.0
    total_reviews: Optional[int] = 0
    demo_url: Optional[HttpUrl] = None
    video_url: Optional[HttpUrl] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ProductDetail(ProductBase):
    description: str
    short_description: Optional[str] = None
    programming_language: Optional[str] = None
    framework: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    seller_id: int
    category_id: Optional[int] = None


class ProductCreate(BaseModel):
    title: str
    description: str
    price: float
    currency: str = "USD"
    category_id: Optional[int] = None


class ProductListResponse(BaseModel):
    items: List[ProductBase]
    total: int
    page: int
    page_size: int


class CategoryListResponse(BaseModel):
    items: List[CategoryBase]
    total: int
