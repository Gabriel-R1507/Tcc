def paciente_converter(self, paciente):
    return {
        "id": str(paciente["_id"]) if "_id" in paciente else "",
        "nome": paciente["nome"] if "nome" in paciente else "" 
    }