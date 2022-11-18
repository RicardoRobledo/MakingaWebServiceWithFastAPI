# Variables
# Funciones
# Clases
# Colecciones

from typing import List, Tuple, Union, Dict

a: str = 'Hello I am a variable'
b: int = 30
c: float = 3.14
d: bool = True

print(a)
print(b)
print(c)
print(d)


def suma(numero1: int, numero2: int) -> int:
    return numero1 + numero2

valor1: int = 10
valor2: int = 20
valor3: int # definir variable sin asignar su valor inicial

resultado: int = suma(valor1, valor2)
print(resultado)


class User:
    
    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password
    
    def saluda(self) -> str:
        return f'Hola {self.username}'


cody = User('Cody', '1234')
print(cody.saluda())


calificaciones: List[int] = [10, 9, 7, 4, 4, 8, 9]

def promedio(calificaciones: List[int]) -> float:
    return sum(calificaciones) / len(calificaciones)

print(promedio(calificaciones=calificaciones))


#configuraciones: Tuple[str] = ('localhost', 3306, 'root')
configuraciones: Tuple[Union[str, str, bool, int]] = ('localhost', 'root', 3306, True)
print(configuraciones)


usuarios: Dict[str, int] = {
    'Ricardo': 10,
    'Cody': 10 
}
print(usuarios)
