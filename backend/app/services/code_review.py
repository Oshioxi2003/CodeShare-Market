"""Service for AI-powered code review using OpenAI."""
from openai import OpenAI

from app.core.config import settings


def review_code(code: str) -> str:
    """Send code to OpenAI API and return review feedback."""
    if not settings.OPENAI_API_KEY:
        return "OpenAI API key is not configured."

    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    prompt = (
        "Please review the following code and provide suggestions for improvement:\n\n"
        + code
    )
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content.strip()
    except Exception as exc:  # pragma: no cover - network
        return f"Error during code review: {exc}"
