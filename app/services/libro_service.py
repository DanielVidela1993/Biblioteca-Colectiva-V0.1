from app.utils.json_handler import leer_json
from app.models.models import Libro
from typing import Optional, List, Dict

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
        
        # Buscar usuario propietario
        usuario_propietario = next((u for u in usuarios if u["correo"] == libro["propietario"]), None)

        resultados.append({
            "libro": libro,
            "usuario": usuario_propietario
        })

    return resultados