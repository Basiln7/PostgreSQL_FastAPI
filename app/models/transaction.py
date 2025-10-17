from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Optional — for future joining of user & transaction
    user = relationship("User")
