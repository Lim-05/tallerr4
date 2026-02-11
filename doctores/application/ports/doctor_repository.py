from abc import ABC, abstractmethod
from typing import List, Optional
from doctores.domain.doctor import Doctor, DoctorCreate

class DoctorRepository(ABC):

    @abstractmethod
    def save(self, doctor: DoctorCreate) -> Doctor:
        pass

    @abstractmethod
    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        pass

    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass

    @abstractmethod
    def find_by_especialidad(self, especialidad: str) -> Optional[Doctor]:
        pass

    '''@abstractmethod
    def update(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        pass'''

    @abstractmethod
    def delete(self, doctor_id: str) -> bool:
        pass
