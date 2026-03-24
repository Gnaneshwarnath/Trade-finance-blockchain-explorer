from pydantic import BaseModel

class LedgerCreate(BaseModel):
    doc_name: str
    doc_hash: str

class LedgerOut(BaseModel):
    id: int
    doc_name: str
    doc_hash: str
    org_name: str

    class Config:
        from_attributes = True