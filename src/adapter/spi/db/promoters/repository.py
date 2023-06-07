from src.adapter.spi.db.db_connection import DbConnection
from src.adapter.spi.db.promoters.db_models import Store
from src.adapter.spi.db.promoters.mappers import StoreDbMapper
from src.application.repositories.promoters.repository_abstract import (
    StoreRepositoryAbstract
)
from src.domain.api_exception import ApiException
from src.domain.promoters.store import StoreEntity


class StoreRepository(StoreRepositoryAbstract):
    def __init__(self, db_connection: DbConnection) -> None:
        self.mapper = StoreDbMapper()
        self.db_connection = db_connection

    def get_store_by_id(self, id: int) -> StoreEntity:
        res = Store.select().where(Store.id == id).get()

        if not res:
            raise ApiException("couldn't retrieve store from id")

        return self.mapper.to_entity(res)
