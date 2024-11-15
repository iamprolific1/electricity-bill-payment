from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    outstanding_balance = Column(Float, default=0.0)
    user = relationship("User", back_populates="accounts")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    amount = Column(Float)
    status = Column(String) #e.g. 'pending', 'completed'
    account = relationship("Account", back_populates="transactions")

User.accounts = relationship("Account", back_populates="user")
Account.transactions = relationship("Transaction", back_populates="account")