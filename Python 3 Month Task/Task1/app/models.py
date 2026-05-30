from sqlalchemy import Column, Integer, String
from .database import Base

class Lead(Base):

    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    interest = Column(String)

class FAQ(Base):

    __tablename__ = "faqs"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)