"""Payment service handling VNPay and PayPal integrations."""
from datetime import datetime
from urllib.parse import urlencode
import hmac
import hashlib
from typing import Dict

from app.core.config import settings


def create_vnpay_payment(transaction_id: str, amount: float, return_url: str) -> str:
    """Generate VNPay payment URL."""
    params = {
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": settings.VNPAY_TMN_CODE,
        "vnp_Amount": int(amount * 100),
        "vnp_CreateDate": datetime.utcnow().strftime("%Y%m%d%H%M%S"),
        "vnp_CurrCode": "VND",
        "vnp_TxnRef": transaction_id,
        "vnp_OrderInfo": f"Payment for transaction {transaction_id}",
        "vnp_ReturnUrl": return_url,
    }
    query = urlencode(sorted(params.items()))
    secure_hash = hmac.new(
        settings.VNPAY_HASH_SECRET.encode(), query.encode(), hashlib.sha512
    ).hexdigest()
    return f"{settings.VNPAY_URL}?{query}&vnp_SecureHash={secure_hash}"


def create_paypal_payment(transaction_id: str, amount: float, return_url: str, cancel_url: str) -> Dict[str, str]:
    """Create a PayPal payment.

    Note: This is a placeholder implementation. In production, integrate the official
    PayPal SDK and return the approval URL from the created payment.
    """
    return {
        "approval_url": f"https://www.sandbox.paypal.com/checkoutnow?token={transaction_id}",
        "transaction_id": transaction_id,
    }
