from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import hashlib

from app.deps import get_db
from app.models import Ledger, User
from app.schemas.ledger import LedgerCreate, LedgerOut
from app.core.security import get_current_user

router = APIRouter(prefix="/ledger", tags=["Ledger"])


# ✅ Add document to ledger (with chaining)
@router.post("/", response_model=LedgerOut)
def add_ledger(
    data: LedgerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 🔗 Get last entry
    last_entry = db.query(Ledger).order_by(Ledger.id.desc()).first()
    prev_hash = last_entry.doc_hash if last_entry else None

    # 🔐 Create new hash (chain)
    combined = (data.doc_hash + str(prev_hash)).encode()
    new_hash = hashlib.sha256(combined).hexdigest()

    entry = Ledger(
        doc_name=data.doc_name,
        doc_hash=new_hash,
        previous_hash=prev_hash,
        owner_id=current_user.id,
        org_name=current_user.org_name
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry


# 🔍 Get all ledger entries (org-based)
@router.get("/", response_model=list[LedgerOut])
def get_ledger(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Ledger).filter(
        Ledger.org_name == current_user.org_name
    ).all()


# ✅ Verify document (strong verification)
@router.get("/verify/{doc_hash}")
def verify_doc(doc_hash: str, db: Session = Depends(get_db)):
    entry = db.query(Ledger).filter(Ledger.doc_hash == doc_hash).first()

    if not entry:
        return {"status": "Not Found ❌"}

    return {
        "status": "Verified ✅",
        "doc_name": entry.doc_name,
        "previous_hash": entry.previous_hash,
        "timestamp": entry.created_at
    }