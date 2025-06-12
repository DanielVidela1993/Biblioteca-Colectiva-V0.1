from typing import List, Dict, Optional
from app.utils.json_handler import leer_json, escribir_json

RUTA_LIBROS = "app/data/libros.json"
RUTA_USUARIOS = "app/data/usuarios.json"

def obtener_libros() -> List[Dict]:
    return leer_json(RUTA_LIBROS)

def obtener_usuarios() -> List[Dict]:
    return leer_json(RUTA_USUARIOS)

def buscar_libros(author: Optional[str] = None,
                  title: Optional[str] = None,
                  year: Optional[int] = None,
                  genre: Optional[str] = None) -> List[Dict]:
    libros = leer_json(RUTA_LIBROS)
    resultado = []

    for libro in libros:
        if author and author.lower() not in libro.get("autor", "").lower():
            continue
        if title and title.lower() not in libro.get("titulo", "").lower():
            continue
        if year and int(libro.get("anio", 0)) != year:
            continue
        if genre and genre.lower() != libro.get("genero", "").lower():
            continue
        resultado.append(libro)

    return resultado

def agregar_libro(nuevo_libro: Dict) -> Dict:
    libros = leer_json(RUTA_LIBROS)
    for libro in libros:
        if libro.get("titulo", "").lower() == nuevo_libro.get("titulo", "").lower() and \
           libro.get("propietario") == nuevo_libro.get("propietario"):
            raise ValueError("El libro ya existe para este propietario.")
    libros.append(nuevo_libro)
    guardar_json(RUTA_LIBROS, libros)
    return nuevo_libro

def eliminar_libro(titulo: str, propietario: str) -> None:
    libros = leer_json(RUTA_LIBROS)
    libros_filtrados = [libro for libro in libros if not (
        libro.get("titulo", "").lower() == titulo.lower() and libro.get("propietario") == propietario)]
    
    if len(libros_filtrados) == len(libros):
        raise ValueError("No se encontró el libro para eliminar.")
    
    guardar_json(RUTA_LIBROS, libros_filtrados)

def editar_libro(titulo: str, propietario: str, datos_actualizados: Dict) -> Dict:
    libros = leer_json(RUTA_LIBROS)
    libro_encontrado = None

    for libro in libros:
        if libro.get("titulo", "").lower() == titulo.lower() and libro.get("propietario") == propietario:
            libro_encontrado = libro
            break

    if libro_encontrado is None:
        raise ValueError("Libro no encontrado para editar.")
    
    for clave, valor in datos_actualizados.items():
        if valor is not None:
            libro_encontrado[clave] = valor
    
    guardar_json(RUTA_LIBROS, libros)
    return libro_encontrado
