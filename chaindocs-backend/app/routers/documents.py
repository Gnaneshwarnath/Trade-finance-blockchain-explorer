import os
import hashlib
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.deps import get_db
from app.models import Document, User
from app.core.security import get_current_user
from app.schemas import DocumentResponse

router = APIRouter(tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/documents/upload", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    # Generate SHA256 hash
    file_hash = hashlib.sha256(content).hexdigest()

    # Save in DB
    document = Document(
        filename=file.filename,
        file_hash=file_hash,
        org_name=current_user.org_name,
        uploaded_by=current_user.email
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


@router.get("/documents", response_model=list[DocumentResponse])
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Document).filter(
        Document.org_name == current_user.org_name
    ).all()

@router.get("/documents/verify/{file_hash}")
def verify_document(
    file_hash: str,
    db: Session = Depends(get_db)
):
    document = db.query(Document).filter(
        Document.file_hash == file_hash
    ).first()

    if document:
        return {
            "status": "Document Verified ✅",
            "filename": document.filename,
            "uploaded_by": document.uploaded_by,
            "org_name": document.org_name,
            "created_at": document.created_at
        }

    return {"status": "Document Not Found ❌"}
