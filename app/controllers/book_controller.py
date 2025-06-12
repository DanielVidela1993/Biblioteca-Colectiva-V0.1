from fastapi import HTTPException
from typing import Optional, List, Dict
from app.services import libro_service
from app.models.models import Libro

def buscar_libros_controller(author: Optional[str] = None,
                             title: Optional[str] = None,
                             year: Optional[int] = None,
                             genre: Optional[str] = None) -> List[Dict]:
    try:
        resultado = libro_service.buscar_libros(author, title, year, genre)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al buscar libros: {str(e)}")


def agregar_libro_controller(libro: Libro) -> Dict:
    try:
        resultado = libro_service.agregar_libro(libro.dict())
        return resultado
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar libro: {str(e)}")


def eliminar_libro_controller(titulo: str, propietario: str) -> Dict:
    try:
        libro_service.eliminar_libro(titulo, propietario)
        return {"mensaje": "Libro eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar libro: {str(e)}")


def editar_libro_controller(titulo: str, propietario: str, datos_actualizados: dict) -> Dict:
    try:
        libro_actualizado = libro_service.editar_libro(titulo, propietario, datos_actualizados)
        return {"mensaje": "Libro editado correctamente", "libro": libro_actualizado}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al editar libro: {str(e)}")
