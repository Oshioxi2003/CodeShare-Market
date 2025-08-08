"""API endpoint for AI code review."""
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.code_review import review_code

router = APIRouter()


class CodeReviewRequest(BaseModel):
    code: str


@router.post("/", response_model=dict)
async def perform_code_review(payload: CodeReviewRequest):
    feedback = review_code(payload.code)
    return {"feedback": feedback}
