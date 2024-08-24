from datetime import datetime, timedelta, timezone
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from jose import jwt, JWTError
from app.models import UserModel
from app.schemas import User, UserLogin
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

crypt_context = CryptContext(schemes=['sha256_crypt'])


class UserUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def user_register(self, user: User):
        existing_user = self.db_session.query(UserModel).filter_by(username=user.username).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
        )
        user_model = UserModel(
            username=user.username,
            email=user.email,
            password=crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(user_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='An error occurred while registering the user'
            )

    def user_login(self, user_login: UserLogin, expires_in: int = 30):
        user_on_db = self.db_session.query(UserModel).filter_by(username=user_login.username).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )

        if not crypt_context.verify(user_login.password, user_on_db.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )

        exp = datetime.now(timezone.utc) + timedelta(minutes=expires_in)
        payload = {
            'sub': user_login.username,
            'exp': exp
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'exp': exp.isoformat()
        }

    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )

        user_on_db = self.db_session.query(UserModel).filter_by(username=data['sub']).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid access token'
            )
        
    def get_user(self, user_id: int):
        user = self.db_session.query(UserModel).filter_by(id=user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {
            'username': user.username,
            'email': user.email
        }
    
    def update_user(self, user_id: int, user: User):
        user_on_db = self.db_session.query(UserModel).filter_by(id=user_id).first()
        if not user_on_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
        )
        user_on_db.username = user.username
        user_on_db.email = user.email
        if user.password:
            user_on_db.password = crypt_context.hash(user.password)
        self.db_session.commit()

    def delete_user(self, user_id: int):
        user_on_db = self.db_session.query(UserModel).filter_by(id=user_id).first()
        if not user_on_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        self.db_session.delete(user_on_db)
        self.db_session.commit()