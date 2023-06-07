import pytest

from src.adapter.api.promoters.store_presenters import StorePresenter
from tests.integration_tests.request_utils import RequestsUtils
from tests.integration_tests.response_utils import ResponseUtils


class TestStore:

    STORE_URL = 'http://localhost:8080/api/v1/promoters/store'

    @pytest.mark.usefixtures("setup_db")
    def test_should_return_one_result_only(self):
        # given the "single store" route
        id = 2
        url = "{url}/{id}".format(
            url=TestStore.STORE_URL,
            id=id
        )

        # when getting
        response = RequestsUtils.client().get(url)

        # then expect 1 result (id 2 inserted in db)
        data: StorePresenter = ResponseUtils.ok_and_parse(response)
        assert data.name == "xablau"
        assert data.id == id
