from sqlalchemy import Column, Integer, String
from app.database import Base

class Ledger(Base):
    __tablename__ = "ledger"

    id = Column(Integer, primary_key=True)
    doc_name = Column(String)
    doc_hash = Column(String)
    org_name = Column(String)