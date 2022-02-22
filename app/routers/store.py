
from typing import  List
from fastapi import Body, FastAPI, Query , Depends , Path, responses , status , HTTPException , encoders , APIRouter
from matplotlib.pyplot import title
from pyparsing import Opt
from sqlalchemy.orm.session import Session
from app.database import SessionLocal
from app import model , schemas
import json

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/store" ,
    tags= ["store"]
)

@router.get('/' , status_code = status.HTTP_201_CREATED)
def get_user(title, db : Session =  Depends(get_db)):
    tmp = db.query(model.User).filter(model.User.title == title).first()
    if not tmp:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= f"Id {id} is not in the DB !")
    return tmp

@router.post('/')
def post_user(request : schemas.Item, db : Session =  Depends(get_db)):
    new = model.User(**request.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.delete('/{id}')
def delete_user(id , db : Session =  Depends(get_db)):
    tmp = db.query(model.User).filter(model.User.id == id)
    if not tmp :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= f"Id {id} is not in the DB !")
    tmp.delete()
    db.commit()
    return f"Id {id} was been deleted"

@router.get('/' , response_model= List[schemas.Item] ) 
def db_user( db : Session =  Depends(get_db)):
    tmp = db.query(model.User).all()
    return tmp