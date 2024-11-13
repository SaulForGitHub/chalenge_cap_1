# CHALLENGE: Copilotos

Este challenge tiene como objetivo comprender y afianzar las mejores prácticas en el uso de copilotos para código impulsados por IA y entender cómo pueden mejorar la eficiencia y productividad en el desarrollo de software.

Este homework está diseñado no solo para aquellos familiarizados con el desarrollo de software y el uso de APIs, sino también para quienes pueden ser nuevos en la programación o en el uso específico de Python y FastAPI. Una de las metas principales es demostrar cómo, incluso sin un profundo conocimiento previo del lenguaje o del framework, una persona puede crear una API simple y funcional con la ayuda de un copiloto de código impulsado por IA.

Antes de comenzar, es esencial familiarizarte con algunas herramientas y librerías que se utilizarán:
- **FastAPI**: Un moderno framework web para construir APIs con Python 3.7+ que es rápido (de alta performance), fácil de aprender, y viene con soporte automático para documentación.

## Prompt:

Necesito una descripción de qué es y para que se utiliza FastAPI, cuales son sus ventajas frente a otro framework y un ejemplo de uso. Las explicaciones deben se formuladas para una persona principiante en programación.

## Inferencias:

¡Hola! Te explico sobre FastAPI de manera sencilla.

FastAPI es un framework moderno de Python para crear APIs web de forma rápida y sencilla. Imagina que es como un ayudante que te permite crear aplicaciones web de manera muy eficiente.

Ventajas principales de FastAPI:

Velocidad: Es uno de los frameworks más rápidos disponibles
Fácil de aprender: Su sintaxis es muy intuitiva
Documentación automática: Crea documentación interactiva sin esfuerzo extra
Validación automática de datos: Verifica que la información que recibe sea correcta
Soporte para async/await: Permite manejar muchas peticiones simultáneamente
Para empezar a usar FastAPI, primero necesitas instalarlo. Aquí está el comando:

```
pip install fastapi uvicorn
```

Aquí te muestro un ejemplo básico de una API que saluda:

```
from fastapi import FastAPI

# Crear la aplicación
app = FastAPI()

# Crear una ruta básica
@app.get("/")
def saludar():
    return {"mensaje": "¡Hola, bienvenido a mi primera API!"}

# Crear una ruta con parámetro
@app.get("/saludar/{nombre}")
def saludar_persona(nombre: str):
    return {"mensaje": f"¡Hola {nombre}!"}
```

Para ejecutar esta API, usarías este comando:

```
uvicorn main:app --reload
```

Después de ejecutarlo, puedes:

Visitar http://localhost:8000 para ver el saludo general
Visitar http://localhost:8000/saludar/Ana para ver un saludo personalizado
Ver la documentación automática en http://localhost:8000/docs
Este ejemplo muestra lo fácil que es crear una API con FastAPI. La documentación se genera automáticamente y puedes probar tu API directamente desde el navegador.

FastAPI es especialmente útil cuando:

Necesitas crear servicios web rápidamente
Quieres una API bien documentada
Trabajas con datos que necesitan validación
Necesitas alto rendimiento
Es una excelente opción para principiantes por su simplicidad y para expertos por su potencia.



- **Pydantic**: Utilizado para la validación de datos y la configuración del esquema de tu API utilizando Python type annotations.

## Prompt:

Necesito una descripción de qué es y para que se utiliza Pydantic, cuales son sus caracteristicas y un ejemplo de uso, si es posible. Las explicaciones deben se formuladas para una persona principiante en programación.

## Inferencias:

¡Con gusto te explico sobre Pydantic!

Pydantic es una biblioteca de Python que nos ayuda a validar datos y manejar configuraciones de una manera muy sencilla. Es como tener un asistente que revisa que todos nuestros datos estén correctos y en el formato que necesitamos.

Características principales:

Validación automática de datos
Conversión de tipos de datos
Manejo de errores claro y amigable
Excelente integración con FastAPI
Muy rápido en su funcionamiento
Soporte para datos anidados
Para entenderlo mejor, imagina que tienes un formulario donde alguien debe registrar una persona. Quieres asegurarte que el email sea válido, la edad sea un número y el nombre no esté vacío.

Aquí te muestro un ejemplo sencillo:

```
from pydantic import BaseModel, EmailStr
from typing import Optional

class Persona(BaseModel):
    nombre: str
    edad: int
    email: EmailStr
    telefono: Optional[str] = None

# Ejemplo de uso
try:
    # Esto funcionará correctamente
    persona1 = Persona(
        nombre="María García",
        edad=25,
        email="maria@ejemplo.com",
        telefono="555-1234"
    )
    print(persona1)
    
    # Esto generará un error porque la edad no es un número
    persona2 = Persona(
        nombre="Juan Pérez",
        edad="veinte",  # ¡Error! Debe ser un número
        email="juan@ejemplo.com"
    )
except Exception as e:
    print(f"Hubo un error: {e}")
```

En este ejemplo:

Creamos una clase Persona que hereda de BaseModel de Pydantic
Definimos los campos con sus tipos de datos
Optional[str] significa que el teléfono es opcional
Pydantic automáticamente validará que:
El nombre sea un texto
La edad sea un número entero
El email tenga un formato válido
El teléfono sea opcional
Si alguien intenta crear una persona con datos incorrectos (como una edad en texto), Pydantic automáticamente mostrará un error explicando qué está mal.

Pydantic es muy útil cuando trabajas con APIs, archivos de configuración o cualquier situación donde necesites asegurarte que los datos cumplan con cierto formato. ¡Es como tener un guardia de seguridad que revisa que todo esté en orden!

- **Passlib**: Para el cifrado de contraseñas.

## Prompt:

Necesito una descripción de qué es y para que se utiliza Passlib, cuales son sus caracteristicas y un ejemplo de uso, si es posible. Las explicaciones deben se formuladas para una persona principiante en programación.

## Inferencias:

¡Con gusto te explico sobre Passlib!

Passlib es una biblioteca de Python muy útil y completa que se especializa en el manejo seguro de contraseñas. Es como una caja de herramientas que nos ayuda a proteger las contraseñas de nuestros usuarios.

Características principales:

Fácil de usar para principiantes
Tiene muchos métodos de encriptación diferentes
Es muy segura y está actualizada con los estándares modernos
Funciona en diferentes versiones de Python
Permite verificar contraseñas de forma segura
Se utiliza principalmente para:

Crear contraseñas seguras
Verificar contraseñas
Encriptar información sensible
Gestionar el almacenamiento seguro de contraseñas en bases de datos
Aquí te muestro un ejemplo sencillo de cómo usar Passlib:

Primero, necesitas instalar Passlib:

```
pip install passlib
```

Y aquí un ejemplo básico de código:

```python:/auth/password_manager.py
from passlib.hash import sha256_crypt

# Crear una contraseña encriptada
password = "micontraseña123"
password_encriptada = sha256_crypt.hash(password)

print("Contraseña encriptada:", password_encriptada)

# Verificar si una contraseña es correcta
es_correcta = sha256_crypt.verify("micontraseña123", password_encriptada)
print("¿La contraseña es correcta?:", es_correcta)

# Intentar con una contraseña incorrecta
es_incorrecta = sha256_crypt.verify("contraseñaincorrecta", password_encriptada)
print("¿La contraseña incorrecta coincide?:", es_incorrecta)
```

En este ejemplo:

Importamos el método de encriptación sha256_crypt de Passlib
Creamos una contraseña y la encriptamos
Verificamos si la contraseña original coincide con la encriptada
Probamos con una contraseña incorrecta para ver la diferencia
Cada vez que ejecutes este código, la contraseña encriptada será diferente, ¡pero seguirá funcionando! Esto es una característica de seguridad que hace que cada hash sea único.

Este es solo un ejemplo básico, pero Passlib tiene muchas más funcionalidades que puedes explorar según tus necesidades.

- **PyJWT**: Para generar y verificar tokens JWT en el proceso de autenticación.

## Prompt:

Necesito una descripción de qué es y para que se utiliza PyJWT, cuales son sus caracteristicas y un ejemplo de uso, si es posible. Las explicaciones deben se formuladas para una persona principiante en programación.

## Inferencias:

¡Con gusto te explico sobre PyJWT!

PyJWT es una biblioteca de Python que nos permite trabajar con JSON Web Tokens (JWT). Los JWT son una forma segura de transmitir información entre diferentes partes de una aplicación o entre sistemas distintos.

Características principales:

Fácil de usar y entender
Permite crear y verificar tokens de forma segura
Soporta diferentes algoritmos de cifrado
Ideal para autenticación y autorización en aplicaciones web
Permite transmitir datos de forma segura
Los JWT se componen de 3 partes:

Header (Cabecera): Contiene el tipo de token y algoritmo
Payload (Carga útil): Contiene los datos que queremos transmitir
Signature (Firma): Garantiza que el token no ha sido modificado
Aquí te muestro un ejemplo sencillo de cómo usar PyJWT:

```
import jwt

# Crear un token
secret_key = "mi_clave_secreta"
datos = {
    "usuario_id": 123,
    "nombre": "Juan",
    "rol": "usuario"
}

# Generar el token
token = jwt.encode(datos, secret_key, algorithm="HS256")
print("Token generado:", token)

# Decodificar el token
try:
    datos_decodificados = jwt.decode(token, secret_key, algorithms=["HS256"])
    print("Datos decodificados:", datos_decodificados)
except jwt.InvalidTokenError:
    print("Token inválido")
```

Para instalar PyJWT, simplemente ejecuta:
```
pip install PyJWT
```
En el ejemplo anterior:

Primero importamos la biblioteca
Definimos una clave secreta (que debe mantenerse segura)
Creamos un diccionario con los datos que queremos guardar
Generamos el token usando encode()
Luego podemos decodificar el token para recuperar los datos usando decode()
PyJWT es muy útil cuando necesitas:

Crear sistemas de login
Proteger rutas en APIs
Compartir información de forma segura entre servicios
Mantener sesiones de usuario
Verificar la identidad de usuarios
Es una herramienta fundamental en el desarrollo web moderno y es especialmente popular en aplicaciones que usan arquitecturas REST o microservicios.




## Configuración del ambiente
Es recomendable crear un ambiente virtual para manejar las dependencias de manera aislada. Una vez localizado dentro de la carpeta `CAP01_CHALLENGE` Puedes hacerlo ejecutando:
```
python3 -m venv venv
```
Para activar el ambiente virtual, usa el siguiente comando:

En Windows:
```
.\venv\Scripts\activate
```

En Unix o MacOS:
```
source venv/bin/activate
```

## Instalacion de dependencias
Una vez activado el ambiente virtual, instala las dependencias necesarias ejecutando:
```
pip install -r requirements.txt
```

## Ejecutar tu aplicación
Para iniciar tu API FastAPI, ejecuta:
```
uvicorn main:app --reload
```

## Endpoints básicos de la API
Recuerda trabajar sobre el archivo `main.py`
1. ### Bubble Sort
- Ruta: `/bubble-sort`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve la lista ordenada utilizando el algoritmo de Bubble Sort.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"numbers": [lista de números ordenada]}`
2. ### Filtro de Pares
- Ruta: `/filter-even`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve únicamente aquellos que son pares.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"even_numbers": [lista de números pares]}`
3. ### Suma de Elementos
- Ruta: `/sum-elements`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve la suma de sus elementos.
- Entrada: `{"numbers": [lista de números]}`
- Salida: `{"sum": suma de los números}`
4. ### Máximo Valor
- Ruta: `/max-value`
- Método: `POST`
- Descripción: Recibe una lista de números y devuelve el valor máximo.
- Entrada: `{"numbers": [lista de números]}`
- Salida:  `{"max": número máximo}`
5. ### Búsqueda Binaria
- Ruta: `/binary-search`
- Método: `POST`
- Descripción: Recibe un número y una lista de números ordenados. Devuelve true y el índice si el número está en la lista, de lo contrario false y -1 como index.
- Entrada: `{"numbers": [lista de números], "target": int}`
- Salida:  `{"found": booleano, "index": int}`

### Nota
El payload debe estar definido por:

```python 
class Payload(BaseModel):
    numbers: List[int]
```
o
```python 
class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int
```

### 1. Implementación de Autenticación
- **Objetivo**: Añadir un sistema de autenticación básico utilizando tokens.
- **Descripción**: Implementa un endpoint para la creación de usuarios y otro para el inicio de sesión. Los usuarios deben autenticarse para poder acceder a los endpoints existentes.
- **Ruta Registro**: `/register`
  - **Método**: `POST`
  - **Entrada (Body)**: `{"username": "user1", "password": "pass1"}`
  - **Salida**: `{"message": "User registered successfully"}`
  - **Status Code**:
    - 200: Registro exitoso
    - 400: El usuario ya existe
- **Ruta Login**: `/login`
  - **Método**: `POST`
  - **Entrada (Body)**: `{"username": "user1", "password": "pass1"}`
  - **Salida**: `{"access_token": <token_de_acceso>}`
  - **Status Code**:
    - 200: Login Exitoso
    - 401: Credenciales Inválidas

### 2. Cifrado de Contraseñas
- **Objetivo**: Mejorar la seguridad almacenando las contraseñas de manera segura.
- **Descripción**: Utiliza `CryptContext` de `passlib` para cifrar las contraseñas antes de guardarlas en tu base de datos simulada (`fake_db`).

### Nota Sobre Autenticación con Tokens JWT

Recuerda que, una vez registrado e iniciado sesión, se debe generar un token JWT con algoritmo HS256. Este token debe incluirse como un parámetro de consulta (`query parameter`) llamado `token` en cada solicitud a los endpoints protegidos. El token sirve como tu credencial de autenticación, permitiendo que el sistema verifique tu identidad y autorice tu acceso a los recursos solicitados.



Por ejemplo, si deseas acceder a un endpoint protegido después de haber iniciado sesión, tu solicitud podría verse así:

```
POST /some-protected-endpoint?token=<tu_token_jwt_aquí>
```

Asegúrate de reemplazar `<tu_token_jwt_aquí>` con el token JWT real que recibiste como respuesta del endpoint de login. La ausencia de este token o el uso de un token inválido resultará en una respuesta de error, indicando que no estás autorizado para acceder al recurso solicitado.

Este mecanismo de autenticación es crucial para la seguridad de la aplicación, asegurando que solo los usuarios autenticados puedan acceder a ciertos endpoints y realizar acciones específicas.


- **Status Code**:
  - 200: Operacion Exitosa
  - 401: Credenciales Inválidas / Autorización fállida.

##### Nota: ```Por simplicidad, este proyecto utiliza parámetros de consulta para pasar el token JWT. En aplicaciones de producción, se recomienda usar headers de autorización para tokens y el cuerpo de la solicitud para credenciales de usuario, adheriéndose a las mejores prácticas de seguridad para proteger la información sensible.```

Recuerda hacer uso del comando `/doc` en el copiloto para documentar tus funciones.

## Ejemplo de Uso
```
Entrada: {"numbers": [5, 3, 8, 6, 1, 9]}
```
- Salida Bubble Sort:  `{"numbers": [1, 3, 5, 6, 8, 9]}`
- Salida Filtro de Pares: `{"even_numbers": [8, 6]}`
- Salida Suma de Elementos: `{"sum": 32}`
- Salida Máximo Valor: `{"max": 9}`

#### Registro de Usuario
```bash
curl -X 'POST' \
  'http://localhost:8000/register' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user1",
  "password": "pass1"
}'
```

#### Inicio de Sesión
```bash
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "user1",
  "password": "pass1"
}'
```
Este comando devolverá un token que deberás usar en las siguientes solicitudes como parte del parámetro \`token\`.

#### Bubble Sort (Autorizado)
Asegúrate de reemplazar `<TOKEN>` con el token obtenido durante el inicio de sesión.
```bash
curl -X 'POST' \
  'http://localhost:8000/bubble-sort?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [3, 2, 1]
}'
```

#### Filtro de Pares (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/filter-even?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Suma de Elementos (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/sum-elements?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Máximo Valor (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/max-value?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [5, 3, 8, 6, 1, 9]
}'
```

#### Búsqueda Binaria (Autorizado)
```bash
curl -X 'POST' \
  'http://localhost:8000/binary-search?token=<TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
  "numbers": [1, 2, 3, 4, 5],
  "target": 3
}'
```


## Correr Pruebas
Para validar la funcionalidad de tu API, utiliza pytest para ejecutar el módulo de pruebas automatizadas. Asegúrate de estar en el directorio raíz del proyecto y ejecuta:
```
pytest tests.py
```
Esto correrá todas las pruebas definidas en tests.py y te mostrará los resultados.