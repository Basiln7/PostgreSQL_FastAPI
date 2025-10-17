from pydantic import BaseModel

class TransactionBase(BaseModel):
    amount: float

class TransactionCreate(TransactionBase):
    user_id: int

class TransactionOut(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
