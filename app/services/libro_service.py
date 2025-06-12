from typing import Optional, List, Dict
from app.repositories import libro_repository


def buscar_libros(author: Optional[str] = None,
                  title: Optional[str] = None,
                  year: Optional[int] = None,
                  genre: Optional[str] = None) -> List[Dict]:
    # Reutilizamos la función del repositorio que filtra los libros
    libros = libro_repository.buscar_libros(author, title, year, genre)
    usuarios = libro_repository.obtener_usuarios()

    resultados = []
    for libro in libros:
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


def agregar_libro(libro_data: dict) -> Dict:
    return libro_repository.agregar_libro(libro_data)


def eliminar_libro(titulo: str, propietario: str) -> None:
    libro_repository.eliminar_libro(titulo, propietario)


def editar_libro(titulo: str, propietario: str, datos_actualizados: dict) -> Dict:
    return libro_repository.editar_libro(titulo, propietario, datos_actualizados)
