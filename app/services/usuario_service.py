from app.utils.json_handler import leer_json, guardar_json
from app.models.models import Usuario
from typing import List

RUTA = "app/data/usuarios.json"

def registrar_usuario(usuario: Usuario) -> Usuario:
    usuarios = leer_json(RUTA)
    if any(u["correo"] == usuario.correo for u in usuarios):
        raise ValueError("Correo ya registrado")
    usuarios.append(usuario.dict())
    escribir_json(RUTA, usuarios)
    return usuario

def obtener_usuario_por_correo_y_contrasena(correo: str, contrasena: str) -> Usuario:
    usuarios = leer_json(RUTA)
    for u in usuarios:
        if u["correo"] == correo and u["contrasena"] == contrasena:
            return Usuario(**u)
    raise ValueError("Credenciales inválidas")
