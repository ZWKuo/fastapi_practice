from http.client import responses
from operator import mod
from typing import Optional , List
from urllib import response
from fastapi import FastAPI, Query , Depends , Path, responses , status , HTTPException , encoders
from fastapi.param_functions import Body, Path
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import table
from  app.database import SessionLocal, engine
from app import model , schemas
from app.routers import store , store2 , user
from fastapi.middleware.cors import CORSMiddleware
import json



app = FastAPI()

model.Base.metadata.create_all(bind = engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return 'Hello my Friend '


app.include_router(store.router)
app.include_router(store2.router)
app.include_router(user.router)

