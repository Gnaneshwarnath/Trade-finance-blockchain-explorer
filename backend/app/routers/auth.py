from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import models, schemas
from app.deps import get_db
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email exists")

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role,
        org_name=user.org_name
    )
    db.add(new_user)
    db.commit()

    return {"msg": "User created"}

@router.post("/login", response_model=schemas.Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form.username).first()

    if not user or not verify_password(form.password, user.password):
        raise HTTPException(status_code=401)

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}