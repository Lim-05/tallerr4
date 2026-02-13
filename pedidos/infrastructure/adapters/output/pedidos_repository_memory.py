from typing import Dict, List, Optional
from datetime import datetime
from pedidos.application.ports.pedidos_repository import PedidosRepository
from pedidos.domain.pedidos import Pedido, PedidoCreate #PedidosUpdate, PedidosStatus
import uuid


class InMemoryPedidosRepository(PedidosRepository):

    def __init__(self):
        self.pedidos: Dict[str, Pedido] = {}

    def save(self, pedido_data: PedidoCreate) -> Pedido:
        pedido_id = str(uuid.uuid4())
        pedido = Pedido(
            id_pedido=pedido_id,
            nombre_pedido=pedido_data.nombre_pedido,
            descripcion=pedido_data.descripcion,
            created_at=datetime.utcnow()
        )
        self.pedidos[pedido_id] = pedido
        return pedido

    def find_by_id(self, pedido_id: str) -> Optional[Pedido]:
        return self.pedidos.get(pedido_id)

    def find_all(self) -> List[Pedido]:
        return list(self.pedidos.values())

    '''def update(self, id_pedido: str, pedido_update: PedidoUpdate) -> Optional[Pedido]:
        pedido = self.pedidos.get(id_pedido)
        if not pedido:
            return None

        if pedido_update.nombre:
            pedido.nombre = pedido_update.nombre
        if pedido_update.descripcion:
            pedido.descripcion = pedido_update.descripcion
        if pedido_update.status:
            pedido.status = pedido_update.status

        return pedido'''

    def delete(self, pedido_id: str) -> bool:
        return self.pedidos.pop(pedido_id, None) is not None
