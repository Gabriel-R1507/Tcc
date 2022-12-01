from models.Usuario import Usuario
from DTO.UsuarioLoginDto import UsuarioLoginDto
from utils.converterUtil import usuario_converter
from repository.database import get_database

db = get_database()

async def loginuser(usuario: UsuarioLoginDto) -> dict:
    usuariofound = db["usuario"].find_one({"login": usuario.login, "senha": usuario.senha })
    if usuariofound:
        return usuario_converter(usuariofound)


def criar_usuario(usuario: Usuario) -> dict:
    created = db["usuario"].insert_one({
            "login" : usuario.login,
            "senha" : usuario.senha,
            "idPaciente" : usuario.idPaciente,
            "isAdmin" : usuario.isAdmin,
        })
    novo = db["usuario"].find_one({"_id": created.inserted_id })
    return usuario_converter(novo)
