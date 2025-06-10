from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    telefono: str
    correo: str
    contrasena: str

class Libro(BaseModel):
    id: int
    autor: str
    titulo: str
    anio: int
    genero: str
    propietario: str
