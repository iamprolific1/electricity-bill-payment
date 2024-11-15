from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(user_id=account.user_id, outstanding_balance=account.outstanding_balance)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(account_id=transaction.account_id, amount=transaction.amount, status="pending")
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
