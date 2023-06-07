from src.adapter.spi.db.promoters.db_models import Store, User
from src.application.mappers.db_mapper import DbMapper, DbModel
from src.domain.promoters.store import StoreEntity
from src.domain.promoters.user import UserEntity


class UserDbMapper(DbMapper):

    def to_db(self, entity: UserEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, model: User) -> UserEntity:
        return UserEntity(
            model.id, model.name, model.cpf_cnpj
        )


class StoreDbMapper(DbMapper):

    def to_db(self, entity: StoreEntity) -> DbModel:
        raise Exception("not implemented")

    def to_entity(self, model: Store) -> StoreEntity:
        return StoreEntity(
            model.id, model.name, UserDbMapper().to_entity(model.user)
        )
