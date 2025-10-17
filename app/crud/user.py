# app/crud/user.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password  # 👈 Normally should be hashed!
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()
