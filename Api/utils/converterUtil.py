def paciente_converter(paciente):
    return {
        "id": str(paciente["_id"]) if "_id" in paciente else "",
        "nome": paciente["nome"] if "nome" in paciente else "" 
    }

def usuario_converter(usuario):
    return {
        "id": str(usuario["_id"]) if "_id" in usuario else "",
        "login": usuario["login"] if "login" in usuario else "",
        "isAdmin": usuario["isAdmin"] if "isAdmin" in usuario else "",
        "idPaciente": usuario["idPaciente"] if "idPaciente" in usuario else "" 
    }

def remedio_converter(remedio):
    return {
        "id": str(remedio["_id"]) if "_id" in remedio else "",
        "nome": remedio["nome"] if "nome" in remedio else "" 
    }