from pydantic import BaseModel

class UsuarioRegistro(BaseModel):
    nombre: str
    telefono: str
    correo: str
    contrasena: str

class UsuarioOut(BaseModel):
    nombre: str
    telefono: str
    correo: str

class LibroIn(BaseModel):
    titulo: str
    autor: str
    anio: int
    genero: str

class LibroOut(LibroIn):
    id: int
    propietario: UsuarioOut
