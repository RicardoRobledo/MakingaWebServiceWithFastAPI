from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from peewee import ModelSelect
from typing import Any


# ---------------------------------------------
#             modelo serializador
# ---------------------------------------------

class PeeweeGetterDict(GetterDict):

    def get(self, key:Any, default:Any=None):
        
        res = getattr(self._obj, key, default)
        
        if isinstance(res, ModelSelect):
            return list(res)
    
        return res


# ---------------------------------------------
#             modelos validadores
# ---------------------------------------------

class ReviewValidator():
    
    @validator('score')
    def score_validator(cls, score):
        
        if score<1 or score>5:
            raise ValueError('score esta fuera de rango, debe de ser de 1 a 5')
        
        return score
    

class UserRequestModel(BaseModel):
    username: str
    password: str
    
    @validator('username')
    def username_validator(cls, username):
        
        if len(username)<4 or len(username)>40:
            raise ValueError('Longitud erronea en el nombre de usuario')

        return username


class ReviewRequestModel(BaseModel, ReviewValidator):
    movie_id: int
    review: str
    score: int


# ---------------------------------------------
#             modelos responses
# ---------------------------------------------

class ResponseModel(BaseModel):
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class MovieResponseModel(ResponseModel):
    id: int
    title: str


class UserResponseModel(ResponseModel):
    id: int
    username: str


class ReviewResponseModel(ResponseModel):
    id: int
    movie: MovieResponseModel
    review: str
    score: int


class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review: str
    score: int
