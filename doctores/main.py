from fastapi import FastAPI
from doctores.infrastructure.adapters.input.rest.doctor_controller import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return {"Bienvenido": "UNACH"}
