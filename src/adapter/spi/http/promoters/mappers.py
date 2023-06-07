from typing import Any

from src.adapter.spi.db.promoters.db_models import User
from src.application.mappers.http_mapper import HttpMapper
from src.domain.promoters.user import UserEntity


class UserHttpMapper(HttpMapper):

    def to_http(self, entity: UserEntity) -> Any:
        raise Exception("not implemented")

    def to_entity(self, http_obj: Any) -> UserEntity:
        return UserEntity(
            id=http_obj["id"],
            cpf_cnpj=http_obj["cpf_cnpj"],
            name=http_obj["name"]
        )
