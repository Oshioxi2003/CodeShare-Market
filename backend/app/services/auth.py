"""
Authentication Service
"""
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.core.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    decode_token,
    generate_password_reset_token,
    verify_password_reset_token,
    generate_verification_token,
    verify_email_token
)
from app.core.config import settings
from app.services.email import EmailService


class AuthService:
    """Authentication service"""
    
    def __init__(self, db: Session):
        self.db = db
        self.email_service = EmailService()
    
    async def authenticate_user(
        self,
        username: str,
        password: str
    ) -> Optional[User]:
        """
        Authenticate user with username/email and password
        """
        user = self.db.query(User).filter(
            (User.email == username) | (User.username == username)
        ).first()
        
        if not user:
            return None
            
        if not verify_password(password, user.hashed_password):
            return None
            
        return user
    
    async def refresh_access_token(self, refresh_token: str) -> dict:
        """
        Refresh access token using refresh token
        """
        try:
            payload = decode_token(refresh_token)
            
            if payload.get("type") != "refresh":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token type"
                )
            
            user_id = payload.get("sub")
            user = self.db.query(User).filter(User.id == int(user_id)).first()
            
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            
            if not user.is_active:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Inactive user"
                )
            
            # Create new access token
            access_token = create_access_token(
                subject=str(user.id),
                expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
            
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
    
    async def send_password_reset_email(self, user: User) -> None:
        """
        Send password reset email
        """
        token = generate_password_reset_token(user.email)
        reset_url = f"{settings.FRONTEND_URL}/reset-password?token={token}"
        
        await self.email_service.send_password_reset_email(
            user.email,
            user.username,
            reset_url
        )
        
        # Store token in database
        user.password_reset_token = token
        user.password_reset_expires = datetime.utcnow() + timedelta(hours=1)
        self.db.commit()
    
    async def reset_password(self, token: str, new_password: str) -> None:
        """
        Reset user password with token
        """
        email = verify_password_reset_token(token)
        
        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired token"
            )
        
        user = self.db.query(User).filter(User.email == email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        # Check if token matches and not expired
        if user.password_reset_token != token:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid token"
            )
        
        if user.password_reset_expires < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Token has expired"
            )
        
        # Update password
        user.hashed_password = get_password_hash(new_password)
        user.password_reset_token = None
        user.password_reset_expires = None
        self.db.commit()
    
    async def verify_email(self, token: str) -> None:
        """
        Verify user email with token
        """
        email = verify_email_token(token)
        
        if not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired token"
            )
        
        user = self.db.query(User).filter(User.email == email).first()
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        if user.is_verified:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already verified"
            )
        
        user.is_verified = True
        user.email_verified_at = datetime.utcnow()
        self.db.commit()
