import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, status

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '..', '..', 'uploads')
UPLOAD_DIR = os.path.abspath(UPLOAD_DIR)

os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()


@router.post("/file")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file")
    ext = os.path.splitext(file.filename)[1]
    target_name = f"{uuid.uuid4().hex}{ext}"
    target_path = os.path.join(UPLOAD_DIR, target_name)
    with open(target_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "stored_as": target_name, "size": os.path.getsize(target_path)}
