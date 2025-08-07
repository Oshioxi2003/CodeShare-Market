"""
Product Model
"""
from sqlalchemy import Column, Integer, String, Float, Text, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class ProductStatus(str, enum.Enum):
    """Product status enumeration"""
    DRAFT = "draft"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    SUSPENDED = "suspended"


class ProductCategory(Base):
    """Product category model"""
    __tablename__ = "product_categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    icon = Column(String(50))
    parent_id = Column(Integer, ForeignKey("product_categories.id"))
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    products = relationship("Product", back_populates="category")
    children = relationship("ProductCategory")


class Product(Base):
    """Product model"""
    __tablename__ = "products"
    
    # Basic Information
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    short_description = Column(String(500))
    
    # Pricing
    price = Column(Float, nullable=False)
    discount_price = Column(Float)
    currency = Column(String(3), default="USD")
    
    # Technical Details
    programming_language = Column(String(50))
    framework = Column(String(100))
    database_type = Column(String(50))
    compatible_browsers = Column(Text)  # JSON string
    responsive = Column(Boolean, default=True)
    
    # Files and Media
    demo_url = Column(String(500))
    video_url = Column(String(500))
    documentation_url = Column(String(500))
    github_url = Column(String(500))
    
    # Statistics
    views = Column(Integer, default=0)
    downloads = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    
    # Status and Moderation
    status = Column(Enum(ProductStatus), default=ProductStatus.PENDING)
    is_featured = Column(Boolean, default=False)
    is_free = Column(Boolean, default=False)
    rejection_reason = Column(Text)
    
    # SEO
    meta_title = Column(String(255))
    meta_description = Column(String(500))
    meta_keywords = Column(Text)
    
    # Version Control
    version = Column(String(20), default="1.0.0")
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    # Requirements
    requirements = Column(Text)  # JSON string
    features = Column(Text)  # JSON string
    tags = Column(Text)  # JSON string
    
    # AI Analysis
    code_quality_score = Column(Float)
    security_score = Column(Float)
    ai_review = Column(Text)
    
    # Foreign Keys
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("product_categories.id"))
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime)
    
    # Relationships
    seller = relationship("User", back_populates="products")
    category = relationship("ProductCategory", back_populates="products")
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    files = relationship("ProductFile", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="product")
    
    def __repr__(self):
        return f"<Product {self.title}>"


class ProductImage(Base):
    """Product image model"""
    __tablename__ = "product_images"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    image_url = Column(String(500), nullable=False)
    thumbnail_url = Column(String(500))
    caption = Column(String(255))
    is_primary = Column(Boolean, default=False)
    order = Column(Integer, default=0)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    product = relationship("Product", back_populates="images")


class ProductFile(Base):
    """Product file model"""
    __tablename__ = "product_files"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_url = Column(String(500), nullable=False)
    file_size = Column(Integer)  # in bytes
    file_type = Column(String(50))
    checksum = Column(String(64))  # SHA256 hash
    is_main = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    product = relationship("Product", back_populates="files")
