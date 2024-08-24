from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.depends import get_db_session, token_verifier
from app.useCases import UserUseCases
from app.schemas import User, UserLogin

user_router = APIRouter(prefix='/user')
test_router = APIRouter(prefix='/test ', dependencies=[Depends(token_verifier)])


@user_router.post('/register', summary="Register a new user",    description="Register a new user with a username, password, and email. This endpoint will hash the password and store the user in the database.", tags=["User Operations"])
def user_register(
    user: User = Body(example={"username": "john_doe", "email": "john@example.com", "password": "strongpassword123"}),
    db_session: Session = Depends(get_db_session),
):
    uc = UserUseCases(db_session=db_session)
    uc.user_register(user=user)
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )


@user_router.post('/login', summary="User login",
    description="Authenticate a user by providing username and password. Returns a JWT token if authentication is successful.", tags=["User Operations"])
def user_login(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session),
):
    uc = UserUseCases(db_session=db_session)
    user_login = UserLogin(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = uc.user_login(user_login=user_login)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )


@user_router.get('/{user_id}', summary="Get user details", tags=["User Operations"])
def get_user(user_id: int, db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)
    user = uc.get_user(user_id)
    return JSONResponse(content=user, status_code=status.HTTP_200_OK)

@user_router.put('/{user_id}', summary="Update user details", tags=["User Operations"])
def update_user(user_id: int, user: User, db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)
    uc.update_user(user_id, user)
    return JSONResponse(content={'msg': 'User updated successfully'}, status_code=status.HTTP_200_OK)

@user_router.delete('/{user_id}', summary="Delete a user", tags=["User Operations"])
def delete_user(user_id: int, db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)
    uc.delete_user(user_id)
    return JSONResponse(content={'msg': 'User deleted successfully'}, status_code=status.HTTP_200_OK)



@test_router.get('/test')
def test_user_verify():
    return 'It works'