from fastapi import FastAPI

from app.routers import auth, users, documents, ledger
from app.database import Base, engine
from app import models   # IMPORTANT (loads all models)

app = FastAPI(title="ChainDocs Backend")

# ✅ CREATE TABLES (VERY IMPORTANT)
Base.metadata.create_all(bind=engine)

# ✅ INCLUDE ROUTERS
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(documents.router)

# ✅ ROOT
@app.get("/")
def root():
    return {"message": "ChainDocs Backend Running"}