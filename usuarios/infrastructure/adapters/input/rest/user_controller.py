from fastapi import APIRouter, Depends
from usuarios.application.services.user_service import UserService
from usuarios.infrastructure.adapters.output.user_repository_memory import InMemoryUserRepository
from usuarios.domain.user import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

repository = InMemoryUserRepository()
service = UserService(repository)


@router.post("/")
def create_user(user: UserCreate):
    return service.register_user(user)


@router.get("/")
def list_users():
    return service.get_all_users()


@router.get("/{user_id}")
def get_user(user_id: str):
    return service.get_user(user_id)


@router.put("/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    return service.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: str):
    return service.delete_user(user_id)
