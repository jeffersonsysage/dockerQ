from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Request, responses, Response, Query
import schemas, database, models
from sqlalchemy.orm import Session
from datetime import datetime

router = APIRouter(tags=['Test'])
get_db = database.get_db

@router.get('/')
async def read_root():
    return {"Hello": "World321"}

@router.get('/user', status_code=status.HTTP_200_OK)
async def getuser(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    users = list(map(lambda user: user.serialize(), all_users))
    return responses.JSONResponse(content={'users': users})

@router.post('/create_user/v2', status_code=status.HTTP_201_CREATED)
async def post_user_v2(request: schemas.JUser, db: Session = Depends(get_db)):
    now = datetime.now()
    new_user = models.User(
        name = request.name,
        email = request.email,
        created_at = now,
        updated_at = now
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "成功建立User資料!"

@router.put('/put_user', status_code=status.HTTP_202_ACCEPTED)
async def put_user(id: str, request: schemas.JUser, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User is not found!")
    else:
        user.update(request.dict())
        db.commit()
    return f"user's id: {id} 資料已修改!"

@router.delete('/delete_user', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user is not found!")
    user.delete()
    db.commit()
    return f"Delete"