from fastapi import APIRouter, HTTPException
from app.schemas.schemas import LibroIn, LibroOut, UsuarioOut
from app.models.models import Libro
from app.services import libro_service

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/", response_model=list[Libro])
def listar_libros(correo: str):
    return libro_service.obtener_libros_por_usuario(correo)

@router.post("/", response_model=Libro)
def agregar(libro: LibroIn, correo: str):
    nuevo = Libro(id=0, propietario=correo, **libro.dict())
    return libro_service.agregar_libro(nuevo)

@router.delete("/{libro_id}")
def eliminar(libro_id: int, correo: str):
    libro_service.eliminar_libro(libro_id, correo)
    return {"mensaje": "Libro eliminado"}

@router.put("/{libro_id}", response_model=Libro)
def editar(libro_id: int, libro: LibroIn, correo: str):
    editado = libro_service.editar_libro(libro_id, libro.dict(), correo)
    if not editado:
        raise HTTPException(status_code=404, detail="Libro no encontrado o no autorizado")
    return editado

@router.get("/buscar/", response_model=list)
def buscar(filtro: str, valor: str):
    libros = libro_service.buscar_libros(filtro, valor)
    resultados = []
    for libro in libros:
        resultados.append({
            "libro": libro,
            "usuario": libro.propietario  # Solo se muestra el correo, por simplicidad
        })
    return resultados
