from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .database import database as connection
from .database import User, Movie, UserReview

from .routers import user_router, review_router

from .common import create_access_token


app = FastAPI(
    title='Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='1'
)

# levantar servidor con uvicorn:
# uvicorn 'modulo':'nombre de la aplicacion' --reload
# ejemplo: uvicorn main:app --reload


api_v1 = APIRouter(prefix='/api/v1')

# agregar rutas sobre otras
api_v1.include_router(user_router)
api_v1.include_router(review_router)

@api_v1.post('/auth')
async def auth(data:OAuth2PasswordRequestForm=Depends()):
    
    user = User.authenticate(data.username, data.password)
    
    if user:
        
        return {
            'access_token': create_access_token(user),
            'token_type': 'Bearer'
        }
    
    else:
    
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username o password incorrectos",
            headers={'WWW-Authenticate':'Bearer'}
        )


app.include_router(api_v1)


# ---------------------------------------------
#                    eventos
# ---------------------------------------------

@app.on_event('startup')
def startup():
    
    print('El servidor se encuentra iniciando')
    
    if connection.is_closed():
        connection.connect()
        
        print('Connecting...')
    
    connection.create_tables([User, Movie, UserReview])


@app.on_event('shutdown')
def shutdown():
    print('El servidor se encuentra finalizando')
    
    if not connection.is_closed():
        connection.close()
        
        print('Closing...')


# ---------------------------------------------
#                     rutas
# ---------------------------------------------

@app.get('/')
async def index():
    return 'Hola mundo, desde un servidor en FastAPI'


@app.get('/about')
async def about():
    return 'About'


# si ingresamos a '/docs' podremos ver la documentacion que se genera
