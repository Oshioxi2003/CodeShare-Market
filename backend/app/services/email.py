"""
Email Service
"""
from typing import List, Optional
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr

from app.core.config import settings


class EmailService:
    """Email service for sending emails"""
    
    def __init__(self):
        self.conf = ConnectionConfig(
            MAIL_USERNAME=settings.MAIL_USERNAME,
            MAIL_PASSWORD=settings.MAIL_PASSWORD,
            MAIL_FROM=settings.MAIL_FROM,
            MAIL_PORT=settings.MAIL_PORT,
            MAIL_SERVER=settings.MAIL_SERVER,
            MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
            MAIL_STARTTLS=settings.MAIL_STARTTLS,
            MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
            USE_CREDENTIALS=settings.USE_CREDENTIALS,
            VALIDATE_CERTS=settings.VALIDATE_CERTS,
            TEMPLATE_FOLDER='app/templates/email'
        )
        self.fm = FastMail(self.conf)
    
    async def send_email(
        self,
        email_to: List[EmailStr],
        subject: str,
        body: str,
        html: Optional[str] = None
    ) -> None:
        """
        Send email to recipients
        """
        message = MessageSchema(
            subject=subject,
            recipients=email_to,
            body=body,
            html=html,
            subtype=MessageType.html if html else MessageType.plain
        )
        
        await self.fm.send_message(message)
    
    async def send_verification_email(
        self,
        email_to: str,
        username: str
    ) -> None:
        """
        Send email verification email
        """
        subject = f"Welcome to {settings.APP_NAME} - Verify Your Email"
        
        html = f"""
        <html>
            <body>
                <h2>Welcome to {settings.APP_NAME}, {username}!</h2>
                <p>Thank you for registering. Please verify your email address to activate your account.</p>
                <p>Click the link below to verify your email:</p>
                <a href="{settings.FRONTEND_URL}/verify-email" 
                   style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Verify Email
                </a>
                <p>If you didn't create an account, please ignore this email.</p>
                <br>
                <p>Best regards,<br>{settings.APP_NAME} Team</p>
            </body>
        </html>
        """
        
        await self.send_email(
            email_to=[email_to],
            subject=subject,
            body=f"Welcome to {settings.APP_NAME}!",
            html=html
        )
    
    async def send_password_reset_email(
        self,
        email_to: str,
        username: str,
        reset_url: str
    ) -> None:
        """
        Send password reset email
        """
        subject = f"{settings.APP_NAME} - Password Reset Request"
        
        html = f"""
        <html>
            <body>
                <h2>Password Reset Request</h2>
                <p>Hi {username},</p>
                <p>We received a request to reset your password. Click the link below to reset it:</p>
                <a href="{reset_url}" 
                   style="background-color: #FF9800; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Reset Password
                </a>
                <p>This link will expire in 1 hour.</p>
                <p>If you didn't request a password reset, please ignore this email.</p>
                <br>
                <p>Best regards,<br>{settings.APP_NAME} Team</p>
            </body>
        </html>
        """
        
        await self.send_email(
            email_to=[email_to],
            subject=subject,
            body="Password reset requested",
            html=html
        )
    
    async def send_purchase_confirmation(
        self,
        email_to: str,
        username: str,
        product_name: str,
        transaction_id: str,
        amount: float
    ) -> None:
        """
        Send purchase confirmation email
        """
        subject = f"{settings.APP_NAME} - Purchase Confirmation"
        
        html = f"""
        <html>
            <body>
                <h2>Purchase Confirmation</h2>
                <p>Hi {username},</p>
                <p>Thank you for your purchase!</p>
                <h3>Order Details:</h3>
                <ul>
                    <li><strong>Product:</strong> {product_name}</li>
                    <li><strong>Transaction ID:</strong> {transaction_id}</li>
                    <li><strong>Amount:</strong> ${amount:.2f}</li>
                </ul>
                <p>You can download your purchase from your dashboard.</p>
                <a href="{settings.FRONTEND_URL}/dashboard/purchases" 
                   style="background-color: #2196F3; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    Go to Dashboard
                </a>
                <br><br>
                <p>Best regards,<br>{settings.APP_NAME} Team</p>
            </body>
        </html>
        """
        
        await self.send_email(
            email_to=[email_to],
            subject=subject,
            body=f"Purchase confirmation for {product_name}",
            html=html
        )
    
    async def send_sale_notification(
        self,
        email_to: str,
        seller_name: str,
        product_name: str,
        buyer_name: str,
        amount: float,
        seller_amount: float
    ) -> None:
        """
        Send sale notification to seller
        """
        subject = f"{settings.APP_NAME} - New Sale!"
        
        html = f"""
        <html>
            <body>
                <h2>Congratulations on Your Sale!</h2>
                <p>Hi {seller_name},</p>
                <p>Great news! You just made a sale.</p>
                <h3>Sale Details:</h3>
                <ul>
                    <li><strong>Product:</strong> {product_name}</li>
                    <li><strong>Buyer:</strong> {buyer_name}</li>
                    <li><strong>Sale Amount:</strong> ${amount:.2f}</li>
                    <li><strong>Your Earnings:</strong> ${seller_amount:.2f}</li>
                </ul>
                <p>The earnings will be available in your wallet after the standard processing period.</p>
                <a href="{settings.FRONTEND_URL}/dashboard/sales" 
                   style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                    View Sales Dashboard
                </a>
                <br><br>
                <p>Keep up the great work!<br>{settings.APP_NAME} Team</p>
            </body>
        </html>
        """
        
        await self.send_email(
            email_to=[email_to],
            subject=subject,
            body=f"New sale of {product_name}",
            html=html
        )
