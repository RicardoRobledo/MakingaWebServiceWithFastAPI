import requests


# ------------------------------------------
#                    GET
# ------------------------------------------
'''
URL = 'http://localhost:8000/api/v1/reviews'
HEADERS = {'accept':'application/json'}
QUERYSET = {'page': 1, 'limit':1}

response = requests.get(URL, headers=HEADERS, params=QUERYSET)

if response.status_code==200:
    
    print('Peticion exitosa')
    
    if response.headers.get('content-type')=='application/json':
        reviews = response.json()
        
        for review in reviews:
            print(f"score: {review['score']} - {review['review']}")

    #print(response.content)
    #print(response.headers)
'''


# ------------------------------------------
#                   POST
# ------------------------------------------
'''
URL = 'http://localhost:8000/api/v1/reviews'
HEADERS = {'accept':'application/json'}
REVIEW = {'user_id': 1, 'movie_id': 1, 'review': 'Review creada con requests', 'score': 5}


response = requests.post(URL, headers=HEADERS, json=REVIEW)

if response.status_code==200:
    print('Reseña creada exitosamente')
    print(response.json()['id'])
else:
    print(response.content)
'''


# ------------------------------------------
#                    PUT
# ------------------------------------------
'''
REVIEW_ID = 3
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'
REVIEW = {'review': 'Review actualizada', 'score': 5}


response = requests.put(URL, json=REVIEW)

if response.status_code==200:
    print('Reseña actualizada exitosamente')
    print(response.json())
'''


# ------------------------------------------
#                   DELETE
# ------------------------------------------
'''
REVIEW_ID = 3
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'


response = requests.delete(URL)

if response.status_code==200:
    print('Reseña eliminada exitosamente')
    print(response.json())
'''


# ------------------------------------------
#                   LOGIN
# ------------------------------------------
URL = 'http://localhost:8000/api/v1/users/'

USER = {'username': 'Zero', 'password': 1234}

response = requests.post(f'{URL}login', json=USER)

if response.status_code==200:
    print('Inicio de sesion exitoso')
    print(response.json())
    
    #cookies
    print(response.cookies) # RequestCookieJar
    print(response.cookies.get_dict())# Cookie diccionario
    
    user_id = response.cookies.get_dict().get('user_id')
    print(user_id)
    
    cookies = {'user_id': user_id}
    response = requests.get(f'{URL}reviews', cookies=cookies)
    
    if response.status_code==200:
        
        for review in response.json():
            print(f"{review['review']} - {review['score']}")
