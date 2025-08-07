"""
User Model
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class UserRole(str, enum.Enum):
    """User role enumeration"""
    ADMIN = "admin"
    SELLER = "seller"
    BUYER = "buyer"
    MODERATOR = "moderator"


class User(Base):
    """User model"""
    __tablename__ = "users"
    
    # Basic Information
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    
    # Profile Information
    avatar_url = Column(String(500))
    bio = Column(Text)
    website = Column(String(255))
    github_url = Column(String(255))
    linkedin_url = Column(String(255))
    
    # Account Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)
    role = Column(Enum(UserRole), default=UserRole.BUYER)
    
    # Seller Information
    seller_rating = Column(Float, default=0.0)
    total_sales = Column(Integer, default=0)
    total_earnings = Column(Float, default=0.0)
    commission_rate = Column(Float, default=0.2)  # 20% default commission
    
    # Security
    email_verified_at = Column(DateTime)
    password_reset_token = Column(String(255))
    password_reset_expires = Column(DateTime)
    two_factor_secret = Column(String(255))
    two_factor_enabled = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login_at = Column(DateTime)
    
    # Relationships
    products = relationship("Product", back_populates="seller", cascade="all, delete-orphan")
    purchases = relationship("Transaction", foreign_keys="Transaction.buyer_id", back_populates="buyer")
    sales = relationship("Transaction", foreign_keys="Transaction.seller_id", back_populates="seller")
    reviews_given = relationship("Review", foreign_keys="Review.reviewer_id", back_populates="reviewer")
    reviews_received = relationship("Review", foreign_keys="Review.product_id", back_populates="product")
    
    def __repr__(self):
        return f"<User {self.username}>"
