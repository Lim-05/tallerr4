from typing import List, Optional
from doctores.domain.doctor import Doctor, DoctorCreate, DoctorStatus
from doctores.application.ports.doctor_repository import DoctorRepository


class DoctorService:


    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def register_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        """Caso de uso: Registrar doctor"""
        #Validación de negocio
        if not doctor_data.username or not doctor_data.especialidad:
            raise ValueError("Username and especialidad are required")
        
        #Verificar unicidad del email
        '''existing_doctor = self.repository.find_by_especialidad(doctor_data.especialidad)
        if existing_doctor:
            raise ValueError(f"Doctor with especialidad {doctor_data.especialidad} is already registered")'''

        #Crear Doctor
        return self.repository.save(doctor_data)
    
    def get_doctor(self, doctor_id: str) -> Optional[Doctor]:
        """Caso de uso: Obtener doctor por ID"""
        return self.repository.find_by_id(doctor_id)
    
    def get_all_doctors(self) -> List[Doctor]:
        """Caso de uso: Listar todos los doctores"""
        return self.repository.find_all()
    
    '''def update_doctor(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        """Caso de uso: Actualizar doctor"""
        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None
        
        #Validar que la nueva especialidad no esté en uso por otro doctor
        if doctor_update.especialidad and doctor_update.especialidad != doctor.especialidad:
            existing_doctor = self.repository.find_by_especialidad(doctor_update.especialidad)
            if existing_doctor:
                raise ValueError(f"Doctor with especialidad {doctor_update.especialidad} is already registered")
            
        return self.repository.update(doctor_id, doctor_update)'''
    
    def delete_doctor(self, doctor_id: str) -> bool:
        """Caso de uso: Eliminar doctor"""
        return self.repository.delete(doctor_id)
            
    '''def deactivate_doctor(self, doctor_id: str) -> Optional[Doctor]:
        """Caso de uso: Desactivar doctor"""
        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None
        
        doctor.deactivate()
        return self.repository.update(doctor_id, DoctorUpdate(status=DoctorStatus.INACTIVE))
    
    def activate_doctor(self, doctor_id: str) -> Optional[Doctor]:
        """Caso de uso: Activar doctor"""
        doctor = self.repository.find_by_id(doctor_id)
        if not doctor:
            return None
        
        doctor.activate()
        return self.repository.update(doctor_id, DoctorUpdate(status=DoctorStatus.ACTIVE))'''
    
    def get_doctor_stats(self) -> dict:
        """Caso de uso: Obtener estadísticas de doctores"""
        doctores = self.repository.find_all()
        total = len(doctores)
        active = len([d for d in doctores if d.is_active()])

        return {
            "total_doctores": total,
            "active_doctores": active,
            "inactive_doctores": total - active
        }
    