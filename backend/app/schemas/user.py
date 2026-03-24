from pydantic import BaseModel

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