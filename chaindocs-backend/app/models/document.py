from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_hash = Column(String, unique=True, index=True)
    org_name = Column(String)
    uploaded_by = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())