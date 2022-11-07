from Api.models.Paciente import Paciente
from fastapi import APIRouter, Body, HTTPException

from models.Usuario import Usuario
from DTO.UsuarioLoginDto import UsuarioLoginDto
from DTO.UsuarioCreateDto import UsuarioCreateDto
from repository.UsuarioRepository import login, criar_usuario
from repository.pacienteRepository import criar_paciente

router = APIRouter()


@router.post("/login")
async def login(usuario: UsuarioLoginDto = Body(...)):
    resultado = await login(usuario)
    if resultado:
        #retorno nao traz o nome do paciente
        return resultado
    else:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

@router.post("/")
async def criarUsuario(usuario: UsuarioCreateDto = Body(...)):
    paciente = Paciente(usuario.nome, usuario.idade, usuario.peso, usuario.altura)
    print(paciente)

    pacienteCriado = await criar_paciente(usuario)
    newUser = Usuario(usuario.login, usuario.senha, pacienteCriado._id)
    
    return await criar_usuario(newUser)