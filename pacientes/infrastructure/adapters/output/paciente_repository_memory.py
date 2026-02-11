from typing import Dict, List, Optional
from datetime import datetime
from pacientes.application.ports.paciente_repository import PacienteRepository
from pacientes.domain.paciente import Paciente, PacienteCreate, PacienteStatus
import uuid


class InMemoryPacienteRepository(PacienteRepository):

    def __init__(self):
        self.pacientes: Dict[str, Paciente] = {}

    def save(self, paciente_data: PacienteCreate) -> Paciente:
        paciente_id = str(uuid.uuid4())
        paciente = Paciente(
            id=paciente_id,
            username=paciente_data.username,
            email=paciente_data.email,
            status=PacienteStatus.ACTIVE,
            created_at=datetime.utcnow()
        )
        self.pacientes[paciente_id] = paciente
        return paciente

    def find_by_id(self, paciente_id: str) -> Optional[Paciente]:
        return self.pacientes.get(paciente_id)

    def find_all(self) -> List[Paciente]:
        return list(self.pacientes.values())

    def find_by_email(self, email: str) -> Optional[Paciente]:
        return next((p for p in self.pacientes.values() if p.email == email), None)

    '''def update(self, paciente_id: str, paciente_update: PacienteUpdate) -> Optional[Paciente]:
        paciente = self.pacientes.get(paciente_id)
        if not paciente:
            return None

        if paciente_update.username:
            paciente.username = paciente_update.username
        if paciente_update.email:
            paciente.email = paciente_update.email
        if paciente_update.status:
            paciente.status = paciente_update.status

        return paciente'''

    def delete(self, paciente_id: str) -> bool:
        return self.pacientes.pop(paciente_id, None) is not None
