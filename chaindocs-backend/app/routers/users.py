from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas import UserResponse

from app.deps import get_db
from app.models import User
from app.core.security import get_current_user
from app.core.roles import require_role
from app.schemas import UserResponse   # ✅ IMPORT THIS

router = APIRouter(tags=["Users"])


@router.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/admin/users", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin"))
):
    return db.query(User).all()


@router.get("/org/users", response_model=List[UserResponse])
def get_org_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(User).filter(
        User.org_name == current_user.org_name
    ).all()
