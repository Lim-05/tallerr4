from fastapi import APIRouter, Depends
from pedidos.application.services.pedidos_service import PedidosService
from pedidos.infrastructure.adapters.output.pedidos_repository_memory import InMemoryPedidosRepository
from pedidos.domain.pedidos import PedidoCreate #UserUpdate

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

repository = InMemoryPedidosRepository()
service = PedidosService(repository)


@router.post("/")
def create_pedido(pedido: PedidoCreate):
    return service.register_pedido(pedido)


@router.get("/")
def list_pedidos():
    return service.get_all_pedidos()


@router.get("/{pedido_id}")
def get_pedido(pedido_id: str):
    return service.get_pedido(pedido_id)


'''@router.put("/{pedido_id}")
def update_pedido(pedido_id: str, pedido: PedidoCreate):
    return service.update_pedido(pedido_id, pedido)'''


@router.delete("/{pedido_id}")
def delete_pedido(pedido_id: str):
    return service.delete_pedido(pedido_id)
