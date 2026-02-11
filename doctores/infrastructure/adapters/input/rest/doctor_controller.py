from fastapi import APIRouter, Depends
from doctores.application.services.doctor_service import DoctorService
from doctores.infrastructure.adapters.output.doctor_repository_memory import InMemoryDoctorRepository
from doctores.domain.doctor import DoctorCreate

router = APIRouter(prefix="/doctores", tags=["Doctores"])

repository = InMemoryDoctorRepository()
service = DoctorService(repository)


@router.post("/")
def create_user(user: DoctorCreate):
    return service.register_doctor(user)


@router.get("/")
def list_users():
    return service.get_all_doctors()


@router.get("/{doctor_id}")
def get_doctor(doctor_id: str):
    return service.get_doctor(doctor_id)


'''@router.put("/{doctor_id}")
def update_doctor(doctor_id: str, doctor: DoctorUpdate):
    return service.update_doctor(doctor_id, doctor)'''


@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: str):
    return service.delete_doctor(doctor_id)
