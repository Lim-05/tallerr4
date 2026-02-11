from fastapi import FastAPI
from pacientes.infrastructure.adapters.input.rest.paciente_controller import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}
