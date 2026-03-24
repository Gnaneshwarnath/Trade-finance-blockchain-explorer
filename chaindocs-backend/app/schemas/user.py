from pydantic import BaseModel, EmailStr

from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    bank = "bank"
    corporate = "corporate"
    auditor = "auditor"
    admin = "admin"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole
    org_name: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ✅ ADD THIS (VERY IMPORTANT)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    org_name: str
    created_at: datetime

    class Config:
        orm_mode = True