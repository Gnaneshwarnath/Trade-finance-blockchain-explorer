from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.deps import get_db
from app.models import User
from app.core.security import get_current_user

router = APIRouter(tags=["Users"])

@router.get("/users/me")
def me(user: User = Depends(get_current_user)):
    return user