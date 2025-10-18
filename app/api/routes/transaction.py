# app/routers/transaction.py (snippet)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionOut
from app.models.transaction import Transaction
from app.core.deps import get_current_user

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionOut)
def create_transaction(txn_in: TransactionCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # Ensure current_user.id == txn_in.user_id or enforce only own account
    if current_user.id != txn_in.user_id:
        raise HTTPException(status_code=403, detail="Not authorized to create transaction for this user")
    new_txn = Transaction(amount=txn_in.amount, user_id=txn_in.user_id)
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)
    return new_txn

@router.get("/", response_model=list[TransactionOut])
def list_transactions(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return db.query(Transaction).filter(Transaction.user_id == current_user.id).all()
