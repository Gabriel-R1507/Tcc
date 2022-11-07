from models.Paciente import Paciente
from fastapi import APIRouter, Body
from repository.pacienteRepository import criar_paciente, listar_pacientes

router = APIRouter()

@router.get("/")
def listarPacientes():
    resultado = listar_pacientes()
    return resultado

@router.post("/")
async def criarPacientes(usuario: Paciente = Body(...)):
    return "teste"
    

    
# def Cadastrar():
#     pNome = input("nome: ")
#     pIdade = int(input("idade: "))
#     pPeso = input("peso: ")
#     paltura = input("altura: ")
    
#     testePaciente = Paciente(pNome, pIdade, pPeso, paltura)

#     print(testePaciente.getJson())


# Cadastrar()