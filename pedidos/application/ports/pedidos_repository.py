from abc import ABC, abstractmethod
from typing import List, Optional
from pedidos.domain.pedidos import Pedido, PedidoCreate #PedidoUpdate

class PedidosRepository(ABC):

    @abstractmethod
    def save(self, pedido: PedidoCreate) -> Pedido:
        pass

    @abstractmethod
    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        pass

    @abstractmethod
    def find_all(self) -> List[Pedido]:
        pass

    '''@abstractmethod
    def update(self, pedido_id: str, pedido_update: PedidoCreate) -> Optional[Pedido]:
        pass'''

    @abstractmethod
    def delete(self, pedido_id: str) -> bool:
        pass
