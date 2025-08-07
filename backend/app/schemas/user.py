"""
User Schemas
"""
from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    """User role enumeration"""
    ADMIN = "admin"
    SELLER = "seller"
    BUYER = "buyer"
    MODERATOR = "moderator"


class UserBase(BaseModel):
    """Base user schema"""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    bio: Optional[str] = None
    website: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None


class UserCreate(UserBase):
    """User creation schema"""
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)


class UserUpdate(UserBase):
    """User update schema"""
    password: Optional[str] = Field(None, min_length=6)
    avatar_url: Optional[HttpUrl] = None


class UserInDBBase(UserBase):
    """Base user in database schema"""
    id: int
    email: EmailStr
    username: str
    is_active: bool
    is_verified: bool
    is_banned: bool
    role: UserRole
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserResponse(UserInDBBase):
    """User response schema"""
    avatar_url: Optional[HttpUrl] = None
    seller_rating: Optional[float] = None
    total_sales: Optional[int] = None
    last_login_at: Optional[datetime] = None


class UserPublic(BaseModel):
    """Public user information schema"""
    id: int
    username: str
    full_name: Optional[str] = None
    avatar_url: Optional[HttpUrl] = None
    bio: Optional[str] = None
    website: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None
    seller_rating: Optional[float] = None
    total_sales: Optional[int] = None
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserStats(BaseModel):
    """User statistics schema"""
    total_products: int
    total_sales: int
    total_earnings: float
    average_rating: float
    total_reviews: int
    products_sold_this_month: int
    earnings_this_month: float


class SellerProfile(UserPublic):
    """Seller profile schema"""
    total_products: int
    total_reviews: int
    response_time: Optional[str] = None
    member_since: datetime
