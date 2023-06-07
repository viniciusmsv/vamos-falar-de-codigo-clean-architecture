from src.domain.base_entity import BaseEntity
from src.domain.promoters.user import UserEntity


class StoreEntity(BaseEntity):

    def __init__(self, id: int, name: str, user: UserEntity) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.user = user
