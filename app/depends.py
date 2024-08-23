from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.useCases import UserUseCases
from app.database import Session as SessionDB

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

def get_db_session():
    try:
        session = SessionDB()
        yield session
    finally:
        session.close()

def token_verifier(
        db_session: Session = Depends(get_db_session),
        token = Depends(oauth_scheme)
):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(access_token=token)