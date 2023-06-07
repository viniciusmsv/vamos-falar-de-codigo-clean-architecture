from fastapi import APIRouter
from fastapi_injector import Injected

from src.adapter.api.promoters.store_mappers import StorePresenterMapper
from src.adapter.api.shared.api_error_handling import ApiErrorHandling
from src.adapter.spi.repositories_factory import RepositoriesFactory
from src.application.repositories.promoters.repository_abstract import (
    StoreRepositoryAbstract
)
from src.application.usecases.promoters.get_one_store_by_id_usecase import (
    GetOneStoreByIdUseCase
)

router = APIRouter()


@router.get("/{id}")
async def get_one_store_by_id(
    id: int, factory: RepositoriesFactory = Injected(RepositoriesFactory)
):
    try:
        store_repository: StoreRepositoryAbstract = factory.get_repository(
            "store_repository"
        )
        store_presenter_mapper: StorePresenterMapper = StorePresenterMapper()

        get_one_store_by_id_usecase: GetOneStoreByIdUseCase = GetOneStoreByIdUseCase( # noqa
            id, store_repository
        )
        store = get_one_store_by_id_usecase.execute()

        return store_presenter_mapper.to_api(store)
    except Exception as exception:
        raise ApiErrorHandling.http_error("Unexpected error getting on store by id", exception)
