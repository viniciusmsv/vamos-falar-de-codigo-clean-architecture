from unittest.mock import MagicMock
import unittest

from src.adapter.spi.http.promoters.user_repository import UserRepository
from src.application.usecases.promoters.get_one_user_by_cpf_cnpj_usecase import (
    GetOneUserByCpfCnpjUseCase
)
from src.domain.api_exception import ApiException
from src.domain.promoters.store import StoreEntity
from src.domain.promoters.user import UserEntity


class GetOneUserByCpfCnpjUseCaseTest(unittest.TestCase):
    def test_should_return_generic_message_when_unexpected_repo_exception(self):
        # given the "one user by cpf_cnpj" usecase repo with an unexpected exception
        cpf_cnpj = '1234567890'
        user_repository = UserRepository(None, "")
        user_repository.get_user_by_cpf_cnpj = MagicMock(side_effect=Exception("random exception"))

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneUserByCpfCnpjUseCase = GetOneUserByCpfCnpjUseCase(
            cpf_cnpj, user_repository
        )

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_dog_fact_by_id_usecase.execute()
        self.assertEqual(f'Cannot get user {cpf_cnpj}', str(context.exception.message))

    def test_should_return_custom_message_when_expected_repo_exception(self):
        # given the "one user by cpf_cnpj" usecase repo raising with an expected ApiException
        user_repository = UserRepository(None, "")
        user_repository.get_user_by_cpf_cnpj = MagicMock(side_effect=ApiException("exception in repo"))

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneUserByCpfCnpjUseCase = GetOneUserByCpfCnpjUseCase(
            1, user_repository
        )

        # then exception
        with self.assertRaises(ApiException) as context:
            get_one_dog_fact_by_id_usecase.execute()
        self.assertEqual('exception in repo', str(context.exception.message))

    def test_should_return_one_result(self):
        # given the "one user by cpf_cnpj" usecase repo returning one result
        user_repository = UserRepository(None, "")
        user = UserEntity(id=1, name='homer', cpf_cnpj='1234567890')
        user_repository.get_user_by_cpf_cnpj = MagicMock(
            return_value=StoreEntity(
                id=1, name='xablau', user=user
            )
        )

        # when calling usecase
        get_one_dog_fact_by_id_usecase: GetOneUserByCpfCnpjUseCase = GetOneUserByCpfCnpjUseCase(
            1, user_repository
        )
        data = get_one_dog_fact_by_id_usecase.execute()

        # then assert the result is the expected entity
        self.assertEqual(data.id, 1)
        self.assertEqual(data.name, "xablau")
