from unittest.mock import MagicMock
import unittest

from src.adapter.spi.db.promoters.repository import StoreRepository
from src.application.usecases.promoters.get_one_store_by_id_usecase import (
    GetOneStoreByIdUseCase
)
from src.domain.api_exception import ApiException
from src.domain.promoters.store import StoreEntity
from src.domain.promoters.user import UserEntity


class GetOneStoreByIdUseCaseTest(unittest.TestCase):
    def test_should_return_generic_message_when_unexpected_repo_exception(self):
        # given the "one store by id" usecase repo with an unexpected exception
        id = 1
        store_repository = StoreRepository(None)
        store_repository.get_store_by_id = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneStoreByIdUseCase = GetOneStoreByIdUseCase(id, store_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_dog_fact_by_id_usecase.execute()
        self.assertEqual(f'Cannot get store {id}', str(context.exception.message))

    def test_should_return_custom_message_when_expected_repo_exception(self):
        # given the "one store by id" usecase repo raising with an expected ApiException
        store_repository = StoreRepository(None)
        store_repository.get_store_by_id = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneStoreByIdUseCase = GetOneStoreByIdUseCase(1, store_repository)

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_dog_fact_by_id_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_one_result(self):
        # given the "one store by id" usecase repo returning one result
        store_repository = StoreRepository(None)
        user = UserEntity(id=1, name='homer', cpf_cnpj='1234567890')
        store_repository.get_store_by_id = MagicMock(
            return_value=StoreEntity(
                id=1, name='xablau', user=user
            )
        )

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneStoreByIdUseCase = GetOneStoreByIdUseCase(1, store_repository)
        data = get_one_dog_fact_by_id_usecase.execute()

        # then assert the result is the expected entity
        self.assertEqual(data.id, 1)
        self.assertEqual(data.name, "xablau")
