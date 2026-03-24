from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_hash = Column(String, unique=True)
    org_name = Column(String)
    uploaded_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)   # ✅ ADD THIS