from enum import Enum
from typing import Optional
from pydantic import BaseModel


class PacienteStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Paciente(BaseModel):
    '''Entidad de dominio: Paciente'''
    id: str
    username: str
    email: str
    status: PacienteStatus = PacienteStatus.ACTIVE

    def activate(self):
        """Comportamiento de dominio"""
        self.status = PacienteStatus.ACTIVE

    def deactivate(self):
        """Comportamiento de dominio"""
        self.status = PacienteStatus.INACTIVE

    def is_active(self) -> bool:
        """Comportamiento de dominio"""
        return self.status == PacienteStatus.ACTIVE
    
class PacienteCreate(BaseModel):
    """DTO para crear paciente"""
    username: str
    email: str

'''class PacienteUpdate(BaseModel):
    """DTO para actualizar paciente"""
    username: Optional[str] = None
    email: Optional[str] = None
    status: Optional[PacienteStatus] = None'''

