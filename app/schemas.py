from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str

class AccountCreate(BaseModel):
    user_id: int
    outstanding_balance: float

class TransactionCreate(BaseModel):
    account_id: int
    amount: float