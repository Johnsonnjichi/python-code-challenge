from fastapi import FastAPI
import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import session 

# create database
Base.metadata.create_all(engine)

# access database
def get_access():
    session = SessionLocal()
    try:
        yield Session
        print('Database successfully connected')
    finally:
        session.close()

app = FastAPI()

@app.get("/")
def hello():
    return ['data 1','data 2','data 3','data 4']