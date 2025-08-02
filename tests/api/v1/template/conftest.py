import pytest

from app.core.database import models
from tests.helpers.preload import utils
from tests.utils import common


@pytest.fixture
async def create_template(test_database):
    return await utils.insert_into(
        test_database=test_database, record=models.Template(name="new test template")
    )


@pytest.fixture
def mock_request_create_template_success():
    return common.load_json("api/v1/template/base/mocks/request_create_template.json")


@pytest.fixture
def mock_response_create_template_success():
    return common.load_json("api/v1/template/base/mocks/response_create_template.json")


@pytest.fixture
def mock_response_get_template_by_id_success():
    return common.load_json("api/v1/template/base/mocks//response_get_template_by_id.json")


@pytest.fixture
def mock_response_get_templates_list_success():
    return common.load_json("api/v1/template/base/mocks/response_get_templates_list.json")
