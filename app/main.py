from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = crud.get_user_by_email(db, email=user.email)
  if db_user:
     raise HTTPException(status_code=400, detail='Email already exists')
  return crud.create_user(db=db, user=user)

def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = crud.get_users(db, skip=skip, limit=limit)
  return users

def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = crud.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail='User not found')
  return db_user

def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
  return crud.create_user_item(db=db, item=item, user_id=user_id)

def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return crud.get_items(db, skip=skip, limit=limit)

app.post('/users/', response_model=schemas.User)(create_user)
app.get('/users/', response_model=List[schemas.User])(read_users)
app.get('/users/{user_id}', response_model=schemas.User)(read_user)

app.post('/users/{user_id}/items/', response_model=schemas.Item)(create_item_for_user)
app.get('/items/', response_model=List[schemas.Item])(read_items)
