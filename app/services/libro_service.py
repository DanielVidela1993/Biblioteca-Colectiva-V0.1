from typing import List, Dict, Optional
from app.utils.json_handler import leer_json, escribir_json
from app.models.models import Libro

RUTA_LIBROS = "app/data/libros.json"
RUTA_USUARIOS = "app/data/usuarios.json"

def buscar_libros(author: Optional[str] = None,
                  title: Optional[str] = None,
                  year: Optional[int] = None,
                  genre: Optional[str] = None) -> List[Dict]:
    libros = leer_json(RUTA_LIBROS)
    usuarios = leer_json(RUTA_USUARIOS)

    resultados = []
    for libro in libros:
        if author and author.lower() not in libro.get("autor", "").lower():
            continue
        if title and title.lower() not in libro.get("titulo", "").lower():
            continue
        if year and int(libro.get("anio", 0)) != year:
            continue
        if genre and genre.lower() not in libro.get("genero", "").lower():
            continue

        usuario_propietario = next((u for u in usuarios if u["correo"] == libro["propietario"]), None)

        resultados.append({
            "libro": libro,
            "usuario": {
                "nombre": usuario_propietario.get("nombre") if usuario_propietario else None,
                "correo": usuario_propietario.get("correo") if usuario_propietario else None,
                "telefono": usuario_propietario.get("telefono") if usuario_propietario else None,
            }
        })

    return resultados

def agregar_libro(libro: dict) -> dict:
    libros = leer_json(RUTA_LIBROS)
    usuarios = leer_json(RUTA_USUARIOS)

    # Verificar si el propietario (correo) existe
    propietario = libro.get("propietario")
    if not propietario or not any(u["correo"] == propietario for u in usuarios):
        raise ValueError("El propietario especificado no existe.")

    # Validaciones básicas
    if not libro.get("titulo") or not libro.get("autor") or not libro.get("anio") or not libro.get("genero"):
        raise ValueError("Faltan campos obligatorios del libro.")

    libros.append(libro)
    escribir_json(RUTA_LIBROS, libros)
    return libro


def eliminar_libro(titulo: str, propietario: str) -> bool:
    libros = leer_json(RUTA_LIBROS)
    libros_filtrados = [libro for libro in libros if not (libro["titulo"].lower() == titulo.lower() and libro["propietario"] == propietario)]

    if len(libros) == len(libros_filtrados):
        raise ValueError("No se encontró un libro con ese título para el propietario.")

    escribir_json(RUTA_LIBROS, libros_filtrados)
    return True


def editar_libro(titulo: str, propietario: str, datos_actualizados: dict) -> dict:
    libros = leer_json(RUTA_LIBROS)
    libro_encontrado = False

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower() and libro["propietario"] == propietario:
            libro_encontrado = True
            libro["titulo"] = datos_actualizados.get("titulo", libro["titulo"])
            libro["autor"] = datos_actualizados.get("autor", libro["autor"])
            libro["anio"] = datos_actualizados.get("anio", libro["anio"])
            libro["genero"] = datos_actualizados.get("genero", libro["genero"])
            break

    if not libro_encontrado:
        raise ValueError("No se encontró un libro con ese título para el propietario.")

    escribir_json(RUTA_LIBROS, libros)
    return libro
