from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.controllers.book_controller import (
    buscar_libros_controller,
    agregar_libro_controller,
    eliminar_libro_controller,
    editar_libro_controller
)
from app.models.models import Libro

router = APIRouter(prefix="/books", tags=["Libros"])

@router.get("/buscar/")
async def buscar_libros(
    author: Optional[str] = Query(None, description="Filtrar por autor"),
    title: Optional[str] = Query(None, description="Filtrar por título"),
    year: Optional[int] = Query(None, description="Filtrar por año"),
    genre: Optional[str] = Query(None, description="Filtrar por género")
):
    resultados = buscar_libros_controller(author, title, year, genre)
    return {"resultados": resultados}

@router.post("/agregar/")
async def agregar_libro(libro: Libro):
    resultado = agregar_libro_controller(libro)
    return resultado

@router.delete("/eliminar/")
async def eliminar_libro(titulo: str, propietario: str):
    resultado = eliminar_libro_controller(titulo, propietario)
    return resultado

@router.put("/editar/")
async def editar_libro(titulo: str, propietario: str, datos_actualizados: dict):
    resultado = editar_libro_controller(titulo, propietario, datos_actualizados)
    return resultado
