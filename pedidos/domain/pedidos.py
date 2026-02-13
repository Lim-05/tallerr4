from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Pedido(BaseModel):
    '''Entidad de dominio: Pedido'''
    id_pedido: str
    nombre_pedido: str
    descripcion: str
    created_at: datetime

    '''def activate(self):
        """Comportamiento de dominio"""
        self.status = PedidoStatus.ACTIVE

    def deactivate(self):
        """Comportamiento de dominio"""
        self.status = PedidoStatus.INACTIVE

    def is_active(self) -> bool:
        """Comportamiento de dominio"""
        return self.status == PedidoStatus.ACTIVE'''
    
class PedidoCreate(BaseModel):
    """DTO para crear pedido"""
    nombre_pedido: str
    descripcion: str
    created_at: datetime

'''class PedidoUpdate(BaseModel):
    """DTO para actualizar pedido"""
    nombre_pedido: Optional[str] = None
    descripcion: Optional[str] = None
    created_at: Optional[datetime] = None
    status: Optional[PedidoStatus] = None'''

