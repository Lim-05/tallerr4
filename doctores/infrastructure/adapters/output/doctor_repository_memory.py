from typing import Dict, List, Optional
from datetime import datetime
from doctores.application.ports.doctor_repository import DoctorRepository
from doctores.domain.doctor import Doctor, DoctorCreate, DoctorStatus
import uuid


class InMemoryDoctorRepository(DoctorRepository):

    def __init__(self):
        self.doctores: Dict[str, Doctor] = {}

    def save(self, doctor_data: DoctorCreate) -> Doctor:
        doctor_id = str(uuid.uuid4())
        doctor = Doctor(
            id=doctor_id,
            username=doctor_data.username,
            especialidad=doctor_data.especialidad,
            status=DoctorStatus.ACTIVE,
            created_at=datetime.utcnow()
        )
        self.doctores[doctor_id] = doctor
        return doctor

    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        return self.doctores.get(doctor_id)

    def find_all(self) -> List[Doctor]:
        return list(self.doctores.values())

    def find_by_especialidad(self, especialidad: str) -> List[Doctor]:
        return [d for d in self.doctores.values() if d.especialidad == especialidad]

    '''def update(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        doctor = self.doctores.get(doctor_id)
        if not doctor:
            return None

        if doctor_update.username:
            doctor.username = doctor_update.username
        if doctor_update.email:
            doctor.email = doctor_update.email
        if doctor_update.status:
            doctor.status = doctor_update.status

        return doctor'''

    def delete(self, doctor_id: str) -> bool:
        return self.doctores.pop(doctor_id, None) is not None
