from src.adapter.spi.http.http_connection import HttpConnection
from src.adapter.spi.http.promoters.mappers import UserHttpMapper
from src.application.repositories.promoters.repository_abstract import (
    UserRepositoryAbstract
)
from src.domain.api_exception import ApiException
from src.domain.promoters.user import UserEntity


class UserRepository(UserRepositoryAbstract):
    def __init__(self, http_connection: HttpConnection, source: str) -> None:
        self.mapper = UserHttpMapper()
        self.source = source
        self.http_connection = http_connection

    def get_user_by_cpf_cnpj(self, cpf_cnpj) -> UserEntity:
        """
        Simulando a chamada de em uma api
        """
        # self.http_connection.get("API")
        if cpf_cnpj == '1234567890':
            res_json = {
                'id': 1,
                'name': 'Homer',
                'cpf_cnpj': '1234567890'
            }
        if not res_json:
            raise ApiException("couldn't process json response")

        return self.mapper.to_entity(res_json)
