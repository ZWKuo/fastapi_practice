import email
from unicodedata import name
from xmlrpc.client import boolean
from fastapi.param_functions import Body
from pydantic import BaseModel , EmailStr
from sqlalchemy import Integer
import datetime

class Item(BaseModel):
    title: str
    body: str
    opt: str
    
    class Config:
        orm_mode = True

class Item2(BaseModel):
    title: str
    cup: str
    rank : str
    
    class Config:
        orm_mode = True
        
class User_Out(BaseModel):
    id : int
    name: str
    email: EmailStr
    create_time : datetime.datetime
    class Config:
        orm_mode = True
        
class User_In(BaseModel):
    name: str
    email: EmailStr
    password : str
    
    class Config:
        orm_mode = True