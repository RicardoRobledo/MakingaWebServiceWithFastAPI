from pydantic import BaseModel, validator, ValidationError
from typing import Optional 


class User(BaseModel):
    username: str # Requerido
    password: Optional[int] = None # Opcional
    repeat_password: str
    email: str
    age: int


    @validator('username')
    def username_validation_length(cls, username):
        
        if len(username)<4:
            raise ValueError('Error de longitud minima')
        elif len(username)>40:
            raise ValueError('Error de longitud maxima')
        
        return username


    @validator('repeat_password')
    def repeat_password_validation(cls, repeat_password, values): #con values podemos verificar los demas valores que tenemos en nuestro modelo

        if 'password' in values and repeat_password!=values['password']:
            raise ValueError('Contraseñas diferentes')

        return repeat_password
        

try:
    user1 = User(
        username='Ricardo',
        password='1234',
        repeat_password='4321',
        email='info@gmail.com',
        age=20
    )
except ValueError as e:
    print(e.json())


try:
    user1 = User(
        username=15,
        password='1234',
        repeat_password='1234',
        email=123,
        age=True
    )
except ValidationError as e:
    print(e.json())
