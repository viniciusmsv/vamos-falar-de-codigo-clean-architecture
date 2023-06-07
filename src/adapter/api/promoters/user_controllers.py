from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.promoters.user_mappers import UserPresenterMapper
from src.adapter.api.shared.api_error_handling import ApiErrorHandling
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.application.repositories.promoters.repository_abstract import (
    UserRepositoryAbstract
)
from src.application.usecases.promoters.get_one_user_by_cpf_cnpj_usecase import (
    GetOneUserByCpfCnpjUseCase
)

router = APIRouter()


@router.get("/{cpf_cnpj}")
async def get_user_by_cpf_cnpj(
    cpf_cnpj: str, factory: RepositoriesFactory = Injected(RepositoriesFactory)
):
    try:
        user_repository: UserRepositoryAbstract = factory.get_repository(
            "user_repository"
        )
        user_presenter_mapper: UserPresenterMapper = UserPresenterMapper()

        get_one_user_by_cpf_cnpj_usecase: GetOneUserByCpfCnpjUseCase = GetOneUserByCpfCnpjUseCase( # noqa
            cpf_cnpj, user_repository
        )
        user = get_one_user_by_cpf_cnpj_usecase.execute()

        return user_presenter_mapper.to_api(user)
    except Exception as exception:
        raise ApiErrorHandling.http_error("Unexpected error getting one user by cpf cnpj", exception)
