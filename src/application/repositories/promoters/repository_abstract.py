from abc import ABC, abstractmethod

from src.domain.promoters.store import StoreEntity
from src.domain.promoters.user import UserEntity


class UserRepositoryAbstract(ABC):
    @abstractmethod
    def get_user_by_cpf_cnpj(self, cpf_cnpj: int) -> UserEntity:
        """Get user by id"""


class StoreRepositoryAbstract(ABC):
    @abstractmethod
    def get_store_by_id(self, id: int) -> StoreEntity:
        """Get store by id"""
