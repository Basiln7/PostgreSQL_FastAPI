# app/db/base.py
from app.db.session import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 👇 import all models here
from app.models.user import User
