from array import array
from DTO.UsuarioLoginDto import UsuarioLoginDto
from utils.converterUtil import usuario_converter
from repository.database import get_database

db = get_database()

async def login(usuario: UsuarioLoginDto) -> dict:
    usuariofound = await db["usuario"].find_one({"login": usuario.login, "senha": usuario.senha })
    
    if usuariofound:
        return usuario_converter(usuariofound)
