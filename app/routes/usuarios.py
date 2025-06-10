from fastapi import APIRouter, HTTPException
from app.schemas.schemas import UsuarioRegistro, UsuarioOut
from app.models.models import Usuario
from app.services.usuario_service import registrar_usuario, obtener_usuario_por_correo_y_contrasena

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/registro", response_model=UsuarioOut)
def registro(usuario: UsuarioRegistro):
    try:
        nuevo = registrar_usuario(Usuario(**usuario.dict()))
        return UsuarioOut(**nuevo.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=UsuarioOut)
def login(correo: str, contrasena: str):
    try:
        usuario = obtener_usuario_por_correo_y_contrasena(correo, contrasena)
        return UsuarioOut(**usuario.dict())
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
