from sqlalchemy.orm import Session, joinedload

from models import User, UserProfile
from schemas.user import UserCreate, UserUpdate
from schemas.user_profile import UserProfileUpdate


def get_user_with_profile(db: Session, user_id: int):
    # TODO クエリで1発で取れないか調べる。
    user = db.query(User).filter(User.id == user_id).first()
    user_profile = db.query(UserProfile).filter(UserProfile.user_id == user_id).first()

    user.first_name = user_profile.first_name
    user.last_name = user_profile.last_name
    user.phone_number = user_profile.phone_number
    user.postal_code = user_profile.postal_code
    user.prefecture = user_profile.prefecture
    user.city = user_profile.city
    user.address = user_profile.address
    user.date_of_birth = user_profile.date_of_birth
    user.icon_image = user_profile.icon_image

    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, limit: int = 100):
    return db.query(User).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # 同時にユーザー詳細情報も初期値で作成
    user_profile_data = {
        "first_name": "",
        "last_name": "",
        "phone_number": "",
        "postal_code": "",
        "prefecture": "",
        "city": "",
        "address": "",
        "date_of_birth": None,
        "icon_image": "",
        "user_id": db_user.id  # 新しいユーザーの ID を指定
    }

    db_user_profile = UserProfile(**user_profile_data)
    db.add(db_user_profile)
    db.commit()
    db.refresh(db_user_profile)

    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()

def get_userprofile(db: Session, userprofile_id: int):
    return db.query(UserProfile).filter(UserProfile.id == userprofile_id).first()

def update_userprofile(db: Session, userprofile_id: int, userprofile: UserProfileUpdate):
    db_userprofile = db.query(UserProfile).filter(UserProfile.id == userprofile_id).first()
    db_userprofile.first_name = userprofile.first_name
    db_userprofile.last_name = userprofile.last_name
    db_userprofile.phone_number = userprofile.phone_number
    db_userprofile.postal_code = userprofile.postal_code
    db_userprofile.prefecture = userprofile.prefecture
    db_userprofile.city = userprofile.city
    db_userprofile.address = userprofile.address
    db_userprofile.date_of_birth = userprofile.date_of_birth
    db_userprofile.icon_image = userprofile.icon_image
    db.commit()
    return db_userprofile