from typing import List, Optional
from pedidos.domain.pedidos import Pedido, PedidoCreate #UserUpdate, UserStatus
from pedidos.application.ports.pedidos_repository import PedidosRepository


class PedidosService:

    def __init__(self, repository: PedidosRepository):
        self.repository = repository

    def register_pedido(self, pedido_data: PedidoCreate) -> Pedido:
        """Caso de uso: Registrar pedido"""
        #Validación de negocio
        if not pedido_data.nombre_pedido:
            raise ValueError("Nombre del pedido is required")
        
        '''existing_pedido = self.repository.find_by_nombre(pedido_data.nombre_pedido)

        if existing_pedido:
            raise ValueError(f"Nombre del pedido {pedido_data.nombre_pedido} is already registered")'''
        
        #Crear Pedido
        return self.repository.save(pedido_data)
    
    def get_pedido(self, pedido_id: str) -> Optional[Pedido]:
        """Caso de uso: Obtener pedido por ID"""
        return self.repository.find_by_id(pedido_id)
    
    def get_all_pedidos(self) -> List[Pedido]:
        """Caso de uso: Listar todos los pedidos"""
        return self.repository.find_all()
    
    '''def update_pedido(self, pedido_id: str, pedido_update: PedidoCreate) -> Optional[Pedido]:
        """Caso de uso: Actualizar pedido"""
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None
        
        #Validar que el nuevo nombre del pedido no esté en uso por otro pedido
        if pedido_update.nombre_pedido and pedido_update.nombre_pedido != pedido.nombre_pedido:
            existing_pedido = self.repository.find_by_nombre(pedido_update.nombre_pedido)
            if existing_pedido:
                raise ValueError(f"Nombre del pedido {pedido_update.nombre_pedido} is already in use")
            
        return self.repository.update(pedido_id, pedido_update)'''
    
    def delete_pedido(self, pedido_id: str) -> bool:
        """Caso de uso: Eliminar pedido"""
        return self.repository.delete(pedido_id)
            
    '''def deactivate_pedido(self, pedido_id: str) -> Optional[Pedido]:
        """Caso de uso: Desactivar pedido"""
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None
        
        pedido.deactivate()
        return self.repository.update(pedido_id, PedidoCreate(nombre_pedido=pedido.nombre_pedido, created_at=pedido.created_at))
    
    def activate_pedido(self, pedido_id: str) -> Optional[Pedido]:
        """Caso de uso: Activar pedido"""
        pedido = self.repository.find_by_id(pedido_id)
        if not pedido:
            return None
        
        pedido.activate()
        return self.repository.update(pedido_id, PedidoCreate(nombre_pedido=pedido.nombre_pedido, created_at=pedido.created_at))'''
    
    def get_pedido_stats(self) -> dict:
        """Caso de uso: Obtener estadísticas de pedidos"""
        pedidos = self.repository.find_all()
        total = len(pedidos)
        active = len([p for p in pedidos if p.is_active()])

        return {
            "total_pedidos": total,
            "active_pedidos": active,
            "inactive_pedidos": total - active
        }
    