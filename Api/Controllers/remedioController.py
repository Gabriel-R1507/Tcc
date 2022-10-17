from fastapi import APIRouter, Body

router = APIRouter()

@router.get("/")
def listarRemedios():
    return[{},{}]

@router.post("/")
def criarRemedios(remedio = Body(...)):
    return {"teste": remedio}