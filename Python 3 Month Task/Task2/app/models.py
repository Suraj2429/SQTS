from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String

Base=declarative_base()

class Lead(Base):
    __tablename__="leads"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    education=Column(String)
    skills=Column(String)
    interest=Column(String)

class FAQ(Base):
    __tablename__="faqs"

    id=Column(Integer,primary_key=True,index=True)
    question=Column(String)
    answer=Column(String)
    category=Column(String)

class ChatLog(Base):
    __tablename__="chat_logs"

    id=Column(Integer,primary_key=True,index=True)
    question=Column(String)
    response=Column(String)