from fastapi import HTTPException
from app.services.libro_service import (
    buscar_libros as buscar_libros_service
)

def buscar_libros_controller(author=None, title=None, year=None, genre=None):
    try:
        resultados = buscar_libros_service(author, title, year, genre)
        if not resultados:
            raise HTTPException(status_code=404, detail="No se encontraron libros")
        return resultados
    except HTTPException:
        
        raise
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=str(e))
