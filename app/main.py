from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session=Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/accounts/")
def create_account(account: schemas.AccountCreate, db: Session=Depends(database.get_db)):
    return crud.create_account(db=db, account=account)

@app.post("/transactions/")
def create_transaction(transaction: schemas.TransactionCreate, db: Session=Depends(database.get_db)):
    return crud.create_transaction(db=db, transaction=transaction)