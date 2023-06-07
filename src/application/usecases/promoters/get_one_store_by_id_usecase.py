from src.application.repositories.promoters.repository_abstract import (
    StoreRepositoryAbstract
)
from src.application.usecases.interfaces import UseCaseOneEntity
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.promoters.store import StoreEntity


class GetOneStoreByIdUseCase(UseCaseOneEntity):
    def __init__(
        self, id: int, repository: StoreRepositoryAbstract
    ) -> None:
        self.repository = repository
        self.id = id

    def execute(self) -> StoreEntity:
        try:
            return self.repository.get_store_by_id(self.id)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error(
                f"Cannot get store {self.id}", exception
            )
