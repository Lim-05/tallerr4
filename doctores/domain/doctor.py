from enum import Enum
from typing import Optional
from pydantic import BaseModel


class DoctorStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Doctor(BaseModel):
    '''Entidad de dominio: Doctor'''
    id: str
    username: str
    especialidad: str
    status: DoctorStatus = DoctorStatus.ACTIVE

    def activate(self):
        """Comportamiento de dominio"""
        self.status = DoctorStatus.ACTIVE

    def deactivate(self):
        """Comportamiento de dominio"""
        self.status = DoctorStatus.INACTIVE

    def is_active(self) -> bool:
        """Comportamiento de dominio"""
        return self.status == DoctorStatus.ACTIVE
    
class DoctorCreate(BaseModel):
    """DTO para crear doctor"""
    username: str
    especialidad: str

'''class DoctorUpdate(BaseModel):
    """DTO para actualizar doctor"""
    username: Optional[str] = None
    especialidad: Optional[str] = None
    status: Optional[DoctorStatus] = None'''

