from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.core.config import settings
from app.schemas.support import ContactForm
from app.services.email import EmailService

router = APIRouter()


@router.post("/contact")
async def submit_contact(form: ContactForm, db: Session = Depends(get_db)):
    try:
        email_service = EmailService()
        subject = f"[Contact] {form.subject}"
        html = f"""
        <h3>New Contact Message</h3>
        <p><strong>Name:</strong> {form.name}</p>
        <p><strong>Email:</strong> {form.email}</p>
        <p><strong>Subject:</strong> {form.subject}</p>
        <p><strong>Message:</strong><br/>{form.message}</p>
        """
        await email_service.send_email(
            email_to=[settings.ADMIN_EMAIL],
            subject=subject,
            body=form.message,
            html=html,
        )
        return {"message": "Message sent"}
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to send message now")
