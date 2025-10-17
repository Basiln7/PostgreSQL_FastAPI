from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine

from app.api.routes import user, transaction


Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI PostgreSQL Project",
              description="A FastAPI project",
              version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# include routers
app.include_router(user.router, prefix="/api", tags=["User"])
app.include_router(transaction.router, prefix="/api", tags=["Transaction"])
app.include_router(user.router)
@app.get("/")
def root():
    return {"message": "Welcome to FastAPI + PostgreSQL CRM Demo"}


