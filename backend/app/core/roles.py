from fastapi import Depends, HTTPException
from app.core.security import get_current_user

def require_role(role: str):
    def role_checker(user=Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="Not allowed")
        return user
    return role_checker