from fastapi import APIRouter, Depends, Request, Response, HTTPException
from sqlalchemy.orm import Session
import cruds
from db.database import get_db
from schemas.user import UserModel, UserCreate, UserUpdate, User
from typing import List


router_user = APIRouter(prefix='/api/v1', tags=["User"])

@router_user.get('/user/{user_id}', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = cruds.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router_user.get('/users', response_model=List[User])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, limit=limit)
    return users


@router_user.post('/users', response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return cruds.create_user(db=db, user=user)


@router_user.put('/users/{user_id}', response_model=UserUpdate)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return cruds.update_user(db=db, user_id=user_id, user=user)


@router_user.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    cruds.delete_user(db=db, user_id=user_id)

# @router_user.get("/", response_model=List[UserModel], summary="UserModelの一覧を取得します")
# async def get_users():
#     return conn.execute(users.select()).fetchall()
# # async def get_tests(request: Request):
# #     res = await db_get_tests()
# #     return res


# @router_user.get("/{id}", response_model=UserModel, summary="UserModelを1件取得します")
# async def get_user(id: int):
#     res = conn.execute(users.select().where(users.c.id == id)).fetchone()
#     if res:
#         return res
#     raise HTTPException(
#         status_code=404, detail=f"User of ID:{id} doesn't exist")

# @router_user.post("/", response_model=UserModel, summary="UserModelを1件新規作成します")
# async def write_user(user: UserModel):
#     conn.execute(users.insert().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ))
#     return conn.execute(users.select()).fetchall()

# @router_user.put("/{id}", response_model=UserModel, summary="UserModelを1件取得します")
# async def update_user(id: int, user: UserModel):
#     conn.execute(users.update().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ).where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()

# @router_user.delete("/{id}", response_model=UserModel, summary="UserModelを1件削除します")
# async def update_user(id: int, user: UserModel):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()