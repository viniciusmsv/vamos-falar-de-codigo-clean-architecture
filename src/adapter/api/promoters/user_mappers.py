from typing import Any
from src.adapter.api.promoters.user_presenters import UserPresenter
from src.application.mappers.api_mapper import ApiMapper
from src.domain.promoters.user import UserEntity


class UserPresenterMapper(ApiMapper):

    def to_api(self, entity: UserEntity) -> UserPresenter:
        return UserPresenter(
            cpf_cnpj=entity.cpf_cnpj,
            name=entity.name
        )

    def to_entity(self, payload: Any) -> UserEntity:
        raise Exception("not implemented")
