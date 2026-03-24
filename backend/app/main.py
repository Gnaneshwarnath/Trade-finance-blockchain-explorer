from fastapi import FastAPI
from app.routers import auth, users, documents, ledger
from app.database import Base, engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(ledger.router)