from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_hash: str
    org_name: str
    uploaded_by: str
    created_at: datetime

    class Config:
        from_attributes = True
        
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str
    org_name: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    org_name: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str