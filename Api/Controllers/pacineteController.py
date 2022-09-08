# from Paciente import Paciente
from fastapi import APIRouter, Body

router = APIRouter()

@router.get("/")
def listarPacientes():
    return[{},{}]

@router.post("/")
def criarPacientes(usuario = Body(...)):
    return {"teste": usuario}

@router.get("/")
def listarPacientes():
    return[{},{}]




    
# def Cadastrar():
#     pNome = input("nome: ")
#     pIdade = int(input("idade: "))
#     pPeso = input("peso: ")
#     paltura = input("altura: ")
    
#     testePaciente = Paciente(pNome, pIdade, pPeso, paltura)

#     print(testePaciente.getJson())


# Cadastrar()