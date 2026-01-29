from fastapi import FastAPI, Depends
from app.core.database import engine, Base
from app.models.test import TestTable
from app.models.user import User
from app.routes.auth import router as auth_router
from app.auth.dependencies import get_current_user


app = FastAPI(title="My API", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/protected")
def protected_route(current_user = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}! You are authenticated."}



