import hashlib
import os
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models import Document, User
from app.core.security import get_current_user
from app.schemas import DocumentResponse   # ✅ IMPORTANT

router = APIRouter(tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/documents/upload", response_model=DocumentResponse)
async def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # ✅ Read file
    content = await file.read()

    # ✅ Save file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(content)

    # ✅ Generate hash
    file_hash = hashlib.sha256(content).hexdigest()

    # ✅ Save to DB
    doc = Document(
        filename=file.filename,
        file_hash=file_hash,
        org_name=user.org_name,
        uploaded_by=user.email
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)   # ✅ IMPORTANT

    return doc

@router.get("/documents/verify/{file_hash}")
def verify_document(
    file_hash: str,
    db: Session = Depends(get_db)
):
    doc = db.query(Document).filter(Document.file_hash == file_hash).first()

    if doc:
        return {
            "status": "✅ Document Verified",
            "filename": doc.filename,
            "uploaded_by": doc.uploaded_by,
            "org_name": doc.org_name,
            "created_at": doc.created_at
        }

    return {
        "status": "❌ Document Not Found"
    }