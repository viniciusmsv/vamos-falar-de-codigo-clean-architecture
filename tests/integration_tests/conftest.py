from peewee import Database
import pytest

from src.adapter.spi.db.promoters.db_models import User, Store
from src.infrastructure.config_mapper import ConfigurationMapper
from src.adapter.spi.db.db_connection import DbConnection
from src.adapter.spi.db.dog_facts.db_models import DogFact
from src.domain.configuration_entity import ConfigurationEntity


@pytest.fixture
def session() -> Database:
    config: ConfigurationEntity = ConfigurationMapper("test").get_config()
    db_connection: DbConnection = DbConnection(config)
    yield db_connection.get_db()
    db_connection.database.close()


@pytest.fixture
# pylint: disable=redefined-outer-name
def setup_db(session: Database):
    session.create_tables([DogFact])
    DogFact.truncate_table()
    DogFact.create(id=1, fact="Forty-five percent of U.S. dogs sleep in their owner's bed")
    DogFact.create(id=2, fact="Seventy percent of people sign their dog's name on their holiday cards")
    DogFact.create(id=3, fact="Dogs have about 1,700 taste buds. We humans have between 2,000-10,000")

    session.create_tables([User, Store])
    User.truncate_table()
    Store.truncate_table()
    user = User.create(id=2, name='Hommer', cpf_cnpj='1234567890')
    Store.create(id=2, name='xablau', user=user)