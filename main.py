from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List, Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

fake_db = {"users": {}}

app = FastAPI()

class Payload(BaseModel):
    numbers: List[int]


class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int


# necesito construir un sistema de registro y autenticacion en python utilizando FastAPI.
# el primer endpoint se debe llamar /register y recibirá llamados vía POST con el formato {"username": "user1", "password": "pass1"}
# cuando el registro del usuario sea correcto, el endpoint debe responder con un código de estado 200 y un mensaje de éxito {"message": "User registered successfully"}.
# en caso contrario, el endpoint debe responder con un código de estado 400 y un mensaje de error.
# al almcenar los datos en la BD se debe realizar en fake_db respestando la sigueinte estructura: fake_db = {"users": {}}
# considera además que el nombre del usuario será la clave del diccionario y el valor de la clave será la contraseña hasheada.

# Configuración de Passlib para el hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Modelo de datos para el registro
class UserRegister(BaseModel):
    username: str
    password: str


@app.post("/register")
async def register_user(user: UserRegister):
    # Verificar si el usuario ya existe
    if user.username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Hashear la contraseña
    hashed_password = pwd_context.hash(user.password)

    # fake_db["users"][user.username] = {"password": user.password}
    # return {"message": "Usuario registrado exitosamente", "database": fake_db["users"]}    

    # Guardar usuario en la base de datos
    fake_db["users"][user.username] = {"password": hashed_password}
    return {"message": "Registro exitoso"}


# código 405: { "detail": "Method Not Allowed" } # GET en lugar de POST


# ahora necesito crear el endpoint /login, que recibirá llamados vía POST con el formato: {"username": "user1", "password": "pass1"}
# el username y password deben ser validados como existentes en fake_db.
# se debe responder status code 401 y el mensaje "Credenciales inválidas" cuando:
# el username que llegó no existe en fake_db o cuando la password que llegó, después de haber sido hasheada, no corresponda a la que tiene el usuario en fake_db.
# si el proceso de login es correcto, se encuentra un username y su password con los datos del POST, se debe generar un nuevo token de acceso.
# este nuevo token de acceso generado con algoritmo HS256 debe ser enviado en la respuesta con el status code 200 y el mensaje "Login exitoso".
@app.post("/login")
async def login_user(payload: UserRegister):

    username = payload.username
    password = payload.password

    # Verificar si el usuario existe
    if username not in fake_db["users"]:
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    
    # Verificar la contraseña
    stored_password = fake_db["users"][username]["password"]
    if not pwd_context.verify(password, stored_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas..")
    
    # Generar token JWT
    token_data = {"sub": username}
    token = jwt.encode(token_data, "secret_key", algorithm="HS256")
    
    # Convención común usar "access_token" como nombre de la clave para tokens JWT
    return {
        "access_token": token
    }



# necesito una función para verificar el JWT que provee el endoint /login que pueda ser utilizada desde cualquier endpoint de negocio.
# en cualquier petición a los endpoints de negocio protegidos, que aún no han sido definidos, debe ser validado el token de acceso.
# el token de acceso se proporcionará en los parámetros de consulta.
# en ausencia del token o en una petición a un endpoint protegido con un token inválido se responderá con status code 401 y el mensaje credenciales inválidas / autorización fállida.
async def verify_token(token: Optional[str] = Query(None)):
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Token de acceso no proporcionado"
        )
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        return payload
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Token de acceso inválido"
        )


# Ejemplo de uso en endpoint protegido
@app.get("/protected")
async def protected_route(current_user: dict = Depends(verify_token)):
    return {
        "message": "Acceso permitido",
        "user": current_user["sub"]
    }



# registrar un usuario: 
#    curl -X POST "http://localhost:8000/register" -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'

# login:
#    curl -X POST "http://localhost:8000/login" -H "Content-Type: application/json" -d '{"username": "user1", "password": "pass1"}'

# verificar token:
#    curl "http://localhost:8000/protected?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8"








################################# END POINT DE NEGOCIO #################################


# necesito una función de tipo POST que implemente Bubble Sort. Será endpoint /bubble-sort
# recibirá com parámetro de entrada una lista de números desordenados y la función deberá retornar o devolver la misma lista, pero ordenada de menor a mayor
# no olvides implementar la validacion del token de acceso que también viene como parámetro.
@app.post("/bubble-sort")
async def bubble_sort(payload: Payload, current_user: dict = Depends(verify_token)):
    numbers = payload.numbers.copy()
    n = len(numbers)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    return {
        "numbers": numbers
    }

# pruebas
#   curl -X POST "http://localhost:8000/bubble-sort?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8" -H "Content-Type: application/json" -d '{"numbers": [64, 34, 25, 12, 22, 11, 90]}'



# necesito una función de tipo POST que realice un filtro. Será endpoint /filter-even
# recibirá com parámetro de entrada una lista de números y la función deberá retornar sólo aquellos números de la lista que sean pares
# no olvides implementar la validacion del token de acceso que también viene como parámetro.
@app.post("/filter-even")
async def filter_even(payload: Payload, current_user: dict = Depends(verify_token)):
    # Filtrar números pares usando list comprehension
    even_numbers = [num for num in payload.numbers if num % 2 == 0]
    
    return {
        "even_numbers": even_numbers
    }

# pruebas:
#   curl -X POST "http://localhost:8000/filter-even?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8" -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}'


# necesito una función de tipo POST que realice una suma de elementos. Será endpoint /sum-elements
# recibirá com parámetro de entrada una lista de números y la función deberá retornar un número correspondiente a la suma de todos los elementos de la lista
# no olvides implementar la validacion del token de acceso que también viene como parámetro.
@app.post("/sum-elements")
async def sum_elements(payload: Payload, current_user: dict = Depends(verify_token)):
    # Calcular la suma de todos los elementos
    total_sum = sum(payload.numbers)
    
    return {
        "sum": total_sum
    }


# pruebas:
#   curl -X POST "http://localhost:8000/sum-elements?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8" -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}'



# necesito una función de tipo POST que obtenga el valor máximo desde una lista de números. Será endpoint /max-value
# recibirá com parámetro de entrada una lista de números y la función deberá retornar el valor máximo de todos los elementos de la lista
# no olvides implementar la validacion del token de acceso que también viene como parámetro.
@app.post("/max-value")
async def max_value(payload: Payload, current_user: dict = Depends(verify_token)):
    # Obtener el valor máximo de la lista
    max_number = max(payload.numbers)
    
    return {
        "max": max_number
    }


# pruebas:
#   curl -X POST "http://localhost:8000/max-value?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8" -H "Content-Type: application/json" -d '{"numbers": [64, 34, 25, 12, 22, 11, 90]}'


# necesito una función de tipo POST que realice una búsqueda binaria. Será endpoint /binary-search
# recibirá como primer parámetro de entrada una lista de números ordenados que recibirá por nombre 'numbers'
# el segundo parámetro será el número que se debe buscar dentro de la lista. Debe ser llamado 'target'
# la función retornará true y el índice si el número está en la lista, de lo contrario false y -1 como índice
# no olvides implementar la validacion del token de acceso que también viene como parámetro.
# en el inicio de este arhivo encontrarás una clase llamada BinarySearchPayload que te servirá para recibir los parámetros de entrada
@app.post("/binary-search")
async def binary_search(payload: BinarySearchPayload, current_user: dict = Depends(verify_token)):
    numbers = payload.numbers
    target = payload.target
    
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if numbers[mid] == target:
            return {
                "found": True,
                "index": mid
            }
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return {
        "found": False,
        "index": -1
    }


# pruebas:
#   curl -X POST "http://localhost:8000/binary-search?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSJ9.tivC9Alqeiwa4XdEGqFPiU60LYtImIoZWud6J5h2Cs8" -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "target": 5}'








# tests.py CAP01_CHALLENGE_saul_ponce creo que no estaba en el directorio correcto antes, ahora me cambié a /Users/sponce/Documents/curso henry/CAP1/CAP01_CHALLENGE_saul_ponce y  ejecuté:

# python3 -m pytest tests.py  

# igualmente me arroja un error:

# ImportError while importing test module '/Users/sponce/Documents/curso henry/CAP1/CAP01_CHALLENGE_saul_ponce/tests.py'.
# Hint: make sure your test modules/packages have valid Python names.
# Traceback:
# /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/importlib/__init__.py:127: in import_module
#     return _bootstrap._gcd_import(name[level:], package, level)
# tests.py:1: in <module>
#     from fastapi.testclient import TestClient
# E   ModuleNotFoundError: No module named 'fastapi'

# puedes indicarme por qué se genera el error y cómo corregirlo?


# ¡Por supuesto! El error ocurre porque no tienes instalada la librería FastAPI en tu entorno Python. Para resolver esto, necesitas instalar las dependencias necesarias para ejecutar las pruebas.

# Ejecuta los siguientes comandos en tu terminal:

# pip install fastapi

# pip install pytest

# pip install httpx

# Estos comandos instalarán:

# FastAPI: el framework web que se está utilizando
# pytest: el framework de pruebas
# httpx: requerido por TestClient de FastAPI
# Después de instalar estas dependencias, podrás ejecutar las pruebas correctamente con:

# python3 -m pytest tests.py

# python3 -m pytest tests.py -vv



# Si estás usando un entorno virtual (lo cual es recomendado), asegúrate de activarlo antes de ejecutar estos comandos de instalación.

