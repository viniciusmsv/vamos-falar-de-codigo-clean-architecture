import pytest

from src.adapter.api.promoters.store_presenters import StorePresenter
from tests.integration_tests.request_utils import RequestsUtils
from tests.integration_tests.response_utils import ResponseUtils


class TestUser:

    USER_URL = 'http://localhost:8080/api/v1/promoters/user'

    @pytest.mark.usefixtures("setup_db")
    def test_should_return_one_result_only(self):
        # given the "single store" route
        cpf_cnpj = '1234567890'
        url = "{url}/{cpf_cnpj}".format(
            url=TestUser.USER_URL,
            cpf_cnpj=cpf_cnpj
        )

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect 1 result (id 2 inserted in db)
        data: StorePresenter = ResponseUtils.ok_and_parse(response)
        assert data.name == "Homer"
        assert data.cpf_cnpj == cpf_cnpj
