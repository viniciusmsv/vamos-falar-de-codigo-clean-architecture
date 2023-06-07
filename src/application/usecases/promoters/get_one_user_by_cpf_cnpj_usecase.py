from src.application.repositories.promoters.repository_abstract import (
    UserRepositoryAbstract
)
from src.application.usecases.interfaces import UseCaseOneEntity
from src.application.utils.error_handling_utils import ErrorHandlingUtils
from src.domain.promoters.user import UserEntity


class GetOneUserByCpfCnpjUseCase(UseCaseOneEntity):
    def __init__(
        self, cpf_cnpj: int, repository: UserRepositoryAbstract
    ) -> None:
        self.repository = repository
        self.cpf_cnpj = cpf_cnpj

    def execute(self) -> UserEntity:
        try:
            return self.repository.get_user_by_cpf_cnpj(self.cpf_cnpj)
        except Exception as exception:
            raise ErrorHandlingUtils.application_error(
                f"Cannot get user {self.cpf_cnpj}", exception
            )
