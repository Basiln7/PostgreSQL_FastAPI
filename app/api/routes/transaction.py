# api/routes/transaction.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate, TransactionOut

router = APIRouter()


@router.post("/transactions", response_model=TransactionOut)
def add_transaction(txn: TransactionCreate, db: Session = Depends(get_db)):
    # check if user exists
    user = db.query(User).filter(User.id == txn.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_txn = Transaction(amount=txn.amount, user_id=txn.user_id)
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return new_txn


@router.get("/transactions", response_model=list[TransactionOut])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()
