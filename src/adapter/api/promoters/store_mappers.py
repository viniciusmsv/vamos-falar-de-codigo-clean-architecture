from typing import Any
from src.adapter.api.promoters.store_presenters import StorePresenter
from src.application.mappers.api_mapper import ApiMapper
from src.domain.promoters.store import StoreEntity


class StorePresenterMapper(ApiMapper):

    def to_api(self, entity: StoreEntity) -> StorePresenter:
        return StorePresenter(
            name=entity.name,
            cpf_cnpj=entity.user.cpf_cnpj,
        )

    def to_entity(self, payload: Any) -> StoreEntity:
        raise Exception("not implemented")
