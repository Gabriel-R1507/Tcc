from fastapi import FastAPI
from Controllers.PacienteController import router as PacienteController
from Controllers.RemedioController import router as RemedioController
from Controllers.UsuarioController import router as UsuarioController

app = FastAPI()
app.include_router(PacienteController, tags=["Pacientes"], prefix="/api/paciente")
app.include_router(RemedioController, tags=["Remedios"], prefix="/api/remedio")
app.include_router(UsuarioController, tags=["Usuario"], prefix="/api/login")

@app.get("/api/health", tags=["Health"])
def listPacientes():
    return {"status": "OK"}


