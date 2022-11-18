from fastapi import APIRouter, HTTPException, Depends, Response, Cookie
from fastapi.security import HTTPBasicCredentials

from ..database import User

from ..schemas import UserRequestModel, UserResponseModel, ReviewResponseModel

from ..common import oauth2_schema, get_current_user

from typing import List


router = APIRouter(prefix='/users')


# ---------------------------------------------
#                    responses
# --------------------------------------------
@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username==user.username).exists():
        raise HTTPException(409, 'El username ya se encuentra en uso')
    
    hash_password = User.create_password(user.password)
    
    user = User.create(
        username=user.username,
        password=hash_password
    )
    
    #return UserResponseModel(id=user.id, username=user.username)
    
    # ---------------------------------------------
    #              serializar objetos           
    # --------------------------------------------
    return user


@router.post('/login', response_model=UserResponseModel)
async def login(credentials:HTTPBasicCredentials, response:Response):
    
    user = User.select().where(User.username==credentials.username).first()
    
    if user is None:
        raise HTTPException(404, 'User not found')
    
    if not user.password==User.create_password(credentials.password):
        raise HTTPException(404, 'Password error')
    
    response.set_cookie(key='user_id', value=user.id) # TOKEN
    response.set_cookie(key='icon', value='example.png')
    response.set_cookie(key='description', value='example')
    return user


'''
@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user_id:int=Cookie(None)):
    
    user = User.select().where(User.id==user_id).first()
    
    if user is None:
        raise HTTPException(404, 'User not found')
    
    return [ user_review for user_review in user.reviews ]
'''


'''
@router.get('/reviews')
async def get_reviews(token:str=Depends(oauth2_schema)):
    
    return {
        'token': token
    }
'''


@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user:User=Depends(get_current_user)):
    
    return [ user_review for user_review in user.reviews ]
