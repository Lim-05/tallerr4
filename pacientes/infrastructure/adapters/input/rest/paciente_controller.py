from fastapi import APIRouter, Depends
from pacientes.application.services.paciente_service import PacienteService
from pacientes.infrastructure.adapters.output.paciente_repository_memory import InMemoryPacienteRepository
from pacientes.domain.paciente import PacienteCreate

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

repository = InMemoryPacienteRepository()
service = PacienteService(repository)


@router.post("/")
def create_user(user: PacienteCreate):
    return service.register_paciente(user)


@router.get("/")
def list_users():
    return service.get_all_pacientes()


@router.get("/{paciente_id}")
def get_paciente(paciente_id: str):
    return service.get_paciente(paciente_id)


'''@router.put("/{paciente_id}")
def update_paciente(paciente_id: str, paciente: PacienteUpdate):
    return service.update_paciente(paciente_id, paciente)'''


@router.delete("/{paciente_id}")
def delete_paciente(paciente_id: str):
    return service.delete_paciente(paciente_id)
