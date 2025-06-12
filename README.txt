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

Biblioteca-Colectiva-V0.1/
│
├── app/                             # Lógica principal del proyecto
│   ├── controllers/                 # Controladores que manejan la lógica HTTP
│   │   ├── libros_controller.py     # Endpoints relacionados con libros
│   │   └── usuarios_controller.py   # Endpoints relacionados con usuarios
│   │
│   ├── models/                      # Modelos de datos y validaciones con Pydantic
│   │   ├── libro_model.py           # Modelos para libros 
│   │   └── usuario_model.py         # Modelos para usuarios 
│   │
│   ├── repositories/               # Acceso a datos 
│   │   ├── libro_repository.py      # Funciones para CRUD de libros
│   │   └── usuario_repository.py    # Funciones para CRUD de usuarios
│   │
│   ├── routes/                      # Rutas de la API
│   │   ├── libros.py                # Ruta de libros
│   │   └── usuarios.py              # Ruta de usuarios
│   │
│   ├── services/                    # Lógica de negocio del proyecto
│   │   ├── libro_service.py         # Reglas y validaciones para libros
│   │   └── usuario_service.py       # Reglas y validaciones para usuarios
│   │
│   ├── utils/                       # Utilidades generales
│   │   └── json_handler.py          # Funciones para leer/escribir archivos JSON
│   │
│   └── data/                        # Archivos de persistencia (base de datos JSON)
│       ├── libros.json              # Base de datos simulada de libros
│       └── usuarios.json            # Base de datos simulada de usuarios
│
├── .env                             # Variables de entorno 
├── main.py                          # Punto de entrada del proyecto (inicia FastAPI)
├── requirements.txt                 # Lista de dependencias del proyecto
├── README.md                        # Documentación general del proyecto
└── .gitignore                       # Archivos y carpetas que git debe ignorar

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

python -m uvicorn main:app --reload

5- Abre la documentación interactiva de tu API:

Swagger UI: http://127.0.0.1:8000/docs


#################### Autor: Daniel Videla ####################