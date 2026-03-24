from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True, index=True)
    doc_name = Column(String)
    doc_hash = Column(String, unique=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    org_name = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())