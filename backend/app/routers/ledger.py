from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.deps import get_db
from app.models import Ledger, User
from app.core.security import get_current_user

router = APIRouter(prefix="/ledger", tags=["Ledger"])

class LedgerCreate(BaseModel):
    doc_name: str
    doc_hash: str

class LedgerOut(BaseModel):
    id: int
    doc_name: str
    doc_hash: str
    org_name: str

    class Config:
        orm_mode = True  # <-- THIS IS IMPORTANT

@router.post("/", response_model=LedgerOut)
def add_ledger(entry_in: LedgerCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    entry = Ledger(
        doc_name=entry_in.doc_name,
        doc_hash=entry_in.doc_hash,
        org_name=user.org_name
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)  # <-- ensures entry has DB-generated fields like id
    return entry