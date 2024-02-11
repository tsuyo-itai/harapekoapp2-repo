from fastapi import APIRouter, Depends, Request, Response, HTTPException
from sqlalchemy.orm import Session
import cruds
from db.database import get_db
from schemas.user import UserCreate, UserUpdate, User, UserWithProfile
from schemas.user_profile import UserProfileUpdate, UserProfile
from typing import List


user_router = APIRouter(prefix='/api/v1', tags=["User"])

# TODO prefix微妙なので再考
@user_router.get('/user_with_profile/{user_id}', response_model=UserWithProfile)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = cruds.get_user_with_profile(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@user_router.get('/user/{user_id}', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = cruds.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@user_router.get('/users', response_model=List[User])
def read_users(limit: int = 100, db: Session = Depends(get_db)):
    users = cruds.get_users(db, limit=limit)
    return users


@user_router.post('/users', response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return cruds.create_user(db=db, user=user)


@user_router.put('/users/{user_id}', response_model=UserUpdate)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return cruds.update_user(db=db, user_id=user_id, user=user)


@user_router.delete('/users/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    cruds.delete_user(db=db, user_id=user_id)

@user_router.get('/userprofile/{userprofile_id}', response_model=UserProfile)
def read_userprofile(userprofile_id: int, db: Session = Depends(get_db)):
    db_userprofile = cruds.get_userprofile(db, userprofile_id=userprofile_id)
    if not db_userprofile:
        raise HTTPException(status_code=404, detail='UserProfile not found')
    return db_userprofile

@user_router.put('/userprofile/{userprofile_id}', response_model=UserProfileUpdate)
def update_userprofile(userprofile_id: int, userprofile: UserProfileUpdate, db: Session = Depends(get_db)):
    return cruds.update_userprofile(db=db, userprofile_id=userprofile_id, userprofile=userprofile)

# @user_router.get("/", response_model=List[UserModel], summary="UserModelの一覧を取得します")
# async def get_users():
#     return conn.execute(users.select()).fetchall()
# # async def get_tests(request: Request):
# #     res = await db_get_tests()
# #     return res


# @user_router.get("/{id}", response_model=UserModel, summary="UserModelを1件取得します")
# async def get_user(id: int):
#     res = conn.execute(users.select().where(users.c.id == id)).fetchone()
#     if res:
#         return res
#     raise HTTPException(
#         status_code=404, detail=f"User of ID:{id} doesn't exist")

# @user_router.post("/", response_model=UserModel, summary="UserModelを1件新規作成します")
# async def write_user(user: UserModel):
#     conn.execute(users.insert().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ))
#     return conn.execute(users.select()).fetchall()

# @user_router.put("/{id}", response_model=UserModel, summary="UserModelを1件取得します")
# async def update_user(id: int, user: UserModel):
#     conn.execute(users.update().values(
#         name=user.name,
#         email=user.email,
#         password=user.password
#     ).where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()

# @user_router.delete("/{id}", response_model=UserModel, summary="UserModelを1件削除します")
# async def update_user(id: int, user: UserModel):
#     conn.execute(users.delete().where(users.c.id == id))
#     return conn.execute(users.select()).fetchall()