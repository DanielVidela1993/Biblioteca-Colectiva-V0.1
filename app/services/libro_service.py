from app.utils.json_handler import leer_json, escribir_json
from app.models.models import Libro
from typing import List, Optional

RUTA = "app/data/libros.json"

def obtener_libros_por_usuario(correo: str) -> List[Libro]:
    return [Libro(**l) for l in leer_json(RUTA) if l["propietario"] == correo]

def agregar_libro(libro: Libro) -> Libro:
    libros = leer_json(RUTA)
    libro.id = max([l["id"] for l in libros], default=0) + 1
    libros.append(libro.dict())
    escribir_json(RUTA, libros)
    return libro

def eliminar_libro(libro_id: int, correo: str) -> None:
    libros = leer_json(RUTA)
    libros_filtrados = [l for l in libros if not (l["id"] == libro_id and l["propietario"] == correo)]
    escribir_json(RUTA, libros_filtrados)

def editar_libro(libro_id: int, datos: dict, correo: str) -> Optional[Libro]:
    libros = leer_json(RUTA)
    for l in libros:
        if l["id"] == libro_id and l["propietario"] == correo:
            l.update(datos)
            escribir_json(RUTA, libros)
            return Libro(**l)
    return None

def buscar_libros(filtro: str, valor: str) -> List[Libro]:
    libros = leer_json(RUTA)
    return [Libro(**l) for l in libros if valor.lower() in str(l.get(filtro, "")).lower()]
