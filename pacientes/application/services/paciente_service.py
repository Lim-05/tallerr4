from typing import List, Optional
from pacientes.domain.paciente import Paciente, PacienteCreate, PacienteStatus
from pacientes.application.ports.paciente_repository import PacienteRepository


class PacienteService:


    def __init__(self, repository: PacienteRepository):
        self.repository = repository

    def register_paciente(self, paciente_data: PacienteCreate) -> Paciente:
        """Caso de uso: Registrar paciente"""
        #Validación de negocio
        if not paciente_data.username or not paciente_data.email:
            raise ValueError("Username and email are required")
        
        #Verificar unicidad del email
        existing_paciente = self.repository.find_by_email(paciente_data.email)
        if existing_paciente:
            raise ValueError(f"Email {paciente_data.email} is already registered")
        
        #Crear Paciente
        return self.repository.save(paciente_data)
    
    def get_paciente(self, paciente_id: str) -> Optional[Paciente]:
        """Caso de uso: Obtener paciente por ID"""
        return self.repository.find_by_id(paciente_id)
    
    def get_all_pacientes(self) -> List[Paciente]:
        """Caso de uso: Listar todos los pacientes"""
        return self.repository.find_all()
    
    '''def update_paciente(self, paciente_id: str, paciente_update: PacienteUpdate) -> Optional[Paciente]:
        """Caso de uso: Actualizar paciente"""
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        
        #Validar que el nuevo email no esté en uso por otro paciente
        if paciente_update.email and paciente_update.email != paciente.email:
            existing_paciente = self.repository.find_by_email(paciente_update.email)
            if existing_paciente:
                raise ValueError(f"Email {paciente_update.email} is already in use")
            
        return self.repository.update(paciente_id, paciente_update)'''
    
    def delete_paciente(self, paciente_id: str) -> bool:
        """Caso de uso: Eliminar paciente"""
        return self.repository.delete(paciente_id)
            
    '''def deactivate_paciente(self, paciente_id: str) -> Optional[Paciente]:
        """Caso de uso: Desactivar paciente"""
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        
        paciente.deactivate()
        return self.repository.update(paciente_id, PacienteUpdate(status=PacienteStatus.INACTIVE))
    
    def activate_paciente(self, paciente_id: str) -> Optional[Paciente]:
        """Caso de uso: Activar paciente"""
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        
        paciente.activate()
        return self.repository.update(paciente_id, PacienteUpdate(status=PacienteStatus.ACTIVE))'''
    
    def get_paciente_stats(self) -> dict:
        """Caso de uso: Obtener estadísticas de pacientes"""
        pacientes = self.repository.find_all()
        total = len(pacientes)
        active = len([p for p in pacientes if p.is_active()])

        return {
            "total_pacientes": total,
            "active_pacientes": active,
            "inactive_pacientes": total - active
        }
    