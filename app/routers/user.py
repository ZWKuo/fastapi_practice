from curses.ascii import HT
import email
from platform import node
from unicodedata import name
from fastapi import FastAPI, Query , Depends , Response, responses , status , HTTPException , encoders , APIRouter
from sqlalchemy.orm.session import Session
from app.database import SessionLocal
from app import model , schemas
from app.routers import utils , oauth2


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/User" ,
    tags= ["User"]
)

@router.post('/', response_model = schemas.User_Out )
def create_user(request : schemas.User_In, db : Session =  Depends(get_db)):
    user_email = db.query(model.User_table).filter(model.User_table.email == request.email).first()
    if  user_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , 
                            detail="The email is already used ! ")
    else:
        request.password = utils.hash_password(request.password)
        new = model.User_table(**request.dict())
        db.add(new)
        db.commit()
        db.refresh(new)
        return new

@router.post('/Login' , response_model=schemas.Token)
def Login(request : schemas.user_login, db : Session =  Depends(get_db)):
    user_email = db.query(model.User_table).filter(model.User_table.email == request.email).first()
    if not user_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The email does't exist !")
    hash_password = db.query(model.User_table).filter(model.User_table.email == request.email).first().password
    if not utils.verify(request.password , hash_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="The password doesn't correct ! ")
    else:
        access_token = oauth2.create_access_token({"user":request.email})
        return {"access_token": access_token, "token_type": "bearer"}