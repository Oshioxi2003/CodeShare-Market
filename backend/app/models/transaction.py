"""
Transaction Model
"""
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class TransactionStatus(str, enum.Enum):
    """Transaction status enumeration"""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class PaymentMethod(str, enum.Enum):
    """Payment method enumeration"""
    STRIPE = "stripe"
    PAYPAL = "paypal"
    VNPAY = "vnpay"
    WALLET = "wallet"
    FREE = "free"


class Transaction(Base):
    """Transaction model"""
    __tablename__ = "transactions"
    
    # Basic Information
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String(100), unique=True, nullable=False, index=True)
    
    # Transaction Details
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    commission_amount = Column(Float, default=0.0)
    seller_amount = Column(Float, default=0.0)
    
    # Payment Information
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    payment_gateway_id = Column(String(255))  # Stripe/PayPal/VNPay transaction ID
    payment_gateway_response = Column(Text)  # JSON response from payment gateway
    
    # Status
    status = Column(Enum(TransactionStatus), default=TransactionStatus.PENDING)
    
    # Additional Information
    notes = Column(Text)
    invoice_number = Column(String(50))
    download_count = Column(Integer, default=0)
    max_downloads = Column(Integer, default=5)
    download_expiry = Column(DateTime)
    
    # Foreign Keys
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime)
    refunded_at = Column(DateTime)
    
    # Relationships
    product = relationship("Product", back_populates="transactions")
    buyer = relationship("User", foreign_keys=[buyer_id], back_populates="purchases")
    seller = relationship("User", foreign_keys=[seller_id], back_populates="sales")
    
    def __repr__(self):
        return f"<Transaction {self.transaction_id}>"
