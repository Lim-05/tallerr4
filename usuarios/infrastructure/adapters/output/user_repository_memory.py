from typing import Dict, List, Optional
from datetime import datetime
from usuarios.application.ports.user_repository import UserRepository
from usuarios.domain.user import User, UserCreate, UserUpdate, UserStatus
import uuid


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users: Dict[str, User] = {}

    def save(self, user_data: UserCreate) -> User:
        user_id = str(uuid.uuid4())
        user = User(
            id=user_id,
            username=user_data.username,
            email=user_data.email,
            status=UserStatus.ACTIVE,
            created_at=datetime.utcnow()
        )
        self.users[user_id] = user
        return user

    def find_by_id(self, user_id: str) -> Optional[User]:
        return self.users.get(user_id)

    def find_all(self) -> List[User]:
        return list(self.users.values())

    def find_by_email(self, email: str) -> Optional[User]:
        return next((u for u in self.users.values() if u.email == email), None)

    def update(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        user = self.users.get(user_id)
        if not user:
            return None

        if user_update.username:
            user.username = user_update.username
        if user_update.email:
            user.email = user_update.email
        if user_update.status:
            user.status = user_update.status

        return user

    def delete(self, user_id: str) -> bool:
        return self.users.pop(user_id, None) is not None
