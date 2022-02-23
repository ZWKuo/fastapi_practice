from sqlite3 import Timestamp
from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String , Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    opt = Column(String , default= True)

class User_2(Base):
    __tablename__ = "users_2"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    cup = Column(String)
    rank = Column(String)
    
class User_table(Base):
    __tablename__ = "User_Table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    create_time = Column(TIMESTAMP(timezone = True) , nullable= False , server_default= text('now()'))

