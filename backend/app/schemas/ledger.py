from pydantic import BaseModel
from datetime import datetime 

class LedgerCreate(BaseModel):
    doc_name: str
    doc_hash: str

class LedgerOut(BaseModel):
    id: int
    doc_name: str
    doc_hash: str
    org_name: str

class LedgerResponse(BaseModel):
    id: int
    action: str
    document_hash: str
    performed_by: str
    timestamp: datetime

    class Config:
        from_attributes = True

   