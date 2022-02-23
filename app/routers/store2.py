from http.client import responses
from typing import  List
from fastapi import FastAPI, Query , Depends , Path, responses , status , HTTPException , encoders , APIRouter
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
    prefix="/store2" ,
    tags= ["store2"]
)


@router.get('/{id}' , status_code = status.HTTP_200_OK , response_class =  responses.ORJSONResponse)
def get_user2(id, db : Session =  Depends(get_db)):
    tmp = db.query(model.User_2).filter(model.User_2.id == id).first()
    if not tmp:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail= f"Id {id} is not in the DB !")
    tmp = encoders.jsonable_encoder(tmp)
    return responses.JSONResponse(content=tmp)

@router.post('/') 
def post_user2(request : schemas.Item2, db : Session =  Depends(get_db) ):
    new = model.User_2(**request.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new 

@router.delete('/{id}')
def delete_user2(id , db : Session =  Depends(get_db)):
    tmp = db.query(model.User_2).filter(model.User_2.id == id)
    if not tmp :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail= f"Id {id} is not in the DB !")
    tmp.delete()
    db.commit()
    return f"Id {id} was been deleted"

