from unicodedata import name
from fastapi import FastAPI, Query , Depends , Path, Response, responses , status , HTTPException , encoders , APIRouter
from sqlalchemy.orm.session import Session
from app.database import SessionLocal
from app import model , schemas
from passlib.context import CryptContext
import json


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/Create_user" ,
    tags= ["User"]
)

@router.post('/', response_model = schemas.User_Out )
def create_user(request : schemas.User_In, db : Session =  Depends(get_db)):
    
    request.password = pwd_context.hash(request.password)
    new = model.User_table(**request.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new