## Biblioteca Colectiva

Este proyecto es una biblioteca colectiva, Utilizando el lenguaje Python y FastAPI (servidor) .
Cada usuario se registra con su nombre y datos de contactos(email y Teléfono).
El usuario puede registrar sus libros y además buscar libros que no poseen. 
Al encontrar el libro que busca, el servidor le ofrecerá los datos de la persona que los posee.
De esta forma podrá contactarse con la persona dueña del libro.

## Version

- Python 3.10 
-FastAPi

## Funciones

-Crear usuario
-Lista de libros
-Editar libro
-Eliminar libro
-Buscar libro(autor, titulo, año, genero)

% Cada usuario cuenta con:
-Nombre
-Correo
-Teléfono
-contraseña

% Cada libro cuenta con:
-Título
-Autor
-Año
-Genero

## Estructura de carpetas:

biblioteca-colectiva/
│
├── .env                     # Archivo para variables de entorno
├── README.txt # Documentación del proyecto
├── main.py             # Punto de entrada principal de la aplicación
├── app/
│   ├── __init__.py         # Hace que app sea un paquete Python
│   │
│   ├── data/               # Datos persistentes
│   │
│   ├── routes/             # Rutas/endpoints de la API
│   │
│   ├── services/           # Lógica de negocio
│   │
│   ├── utils/              # Utilidades varias
│   │
│   ├── schemas/            # Validacion de datos


## pasos para ejecutar:

1-Crea y activa un entorno virtual (en terminal bash):

- python -m venv venv
- source venv/Scripts/activate
	
2- Instala las dependencias  (en terminal bash):

- pip install fastapi uvicorn python-dotenv

3- instalar validador de mails

- pip install email-validator
- pip install uvicorn
4- Ejecuta el servidor:

uvicorn main:app --reload

5- Abre la documentación interactiva de tu API:

Swagger UI: http://127.0.0.1:8000/docs

