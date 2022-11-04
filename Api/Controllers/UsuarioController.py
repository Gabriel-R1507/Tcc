from models.Usuario import Usuario
from DTO.UsuarioLoginDto import UsuarioLoginDto
from fastapi import APIRouter, Body, HTTPException
from repository.UsuarioRepository import login
from Services.AuthService import criptografar_senha, verificar_senha
router = APIRouter()


@router.post("/")
async def criarPacientes(usuario: UsuarioLoginDto = Body(...)):
    resultado = await login(usuario)
    if resultado:
        return resultado
    else:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")