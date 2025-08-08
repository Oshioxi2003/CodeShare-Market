"""
API Router Configuration
"""
from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    users,
    products,
    transactions,
    reviews,
    admin,
    categories,
    upload,
    support,
    code_review,
)

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

api_router.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)

api_router.include_router(
    categories.router,
    prefix="/categories",
    tags=["Categories"]
)

api_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["Transactions"]
)

api_router.include_router(
    reviews.router,
    prefix="/reviews",
    tags=["Reviews"]
)

api_router.include_router(
    upload.router,
    prefix="/upload",
    tags=["File Upload"]
)

api_router.include_router(
    admin.router,
    prefix="/admin",
    tags=["Admin"]
)

api_router.include_router(
    support.router,
    prefix="/support",
    tags=["Support"]
)

api_router.include_router(
    code_review.router,
    prefix="/code-review",
    tags=["Code Review"]
)
