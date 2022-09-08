from fastapi import FastAPI
from Controllers.PacineteController import router as PacienteController
from Controllers.RemedioController import router as RemedioController

app = FastAPI()
app.include_router(PacienteController, tags=["Pacientes"], prefix="/api/paciente")
app.include_router(RemedioController, tags=["Remedios"], prefix="/api/remedio")

@app.get("/api/health", tags=["Health"])
def listPacientes():
    return {"status": "OK"}