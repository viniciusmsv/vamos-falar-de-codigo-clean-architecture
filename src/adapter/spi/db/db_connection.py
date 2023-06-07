from peewee import SqliteDatabase, Database

from src.adapter.spi.db.dog_facts.db_models import DogFact
from src.adapter.spi.db.promoters.db_models import User, Store
from src.application.spi.db_interface import DbInterface
from src.domain.api_exception import ApiException
from src.domain.configuration_entity import ConfigurationEntity


class DbConnection(DbInterface):
    def __init__(self, config: ConfigurationEntity) -> None:
        try:
            self.connection(config)
            self.connection_mvc(config)

            if config.env != "test":
                self.migration()
                self.migration_mvc()
        except Exception as error:
            raise ApiException(
                "error initializing connection to DB: {}".format(str(error))) from error

    def connection(self, config: ConfigurationEntity) -> None:
        self.database = SqliteDatabase(config.dogs_source)
        self.database.bind([DogFact])
        self.database.connect()

    def connection_mvc(self, config: ConfigurationEntity) -> None:
        self.database = SqliteDatabase(config.mvc_source)
        self.database.bind([User, Store])
        self.database.connect()

    def migration(self):
        try:
            self.database.create_tables([DogFact])
            DogFact.truncate_table()
            DogFact.create(id=1, fact="a first fact")
            DogFact.create(id=2, fact="a second fact")
            DogFact.create(id=3, fact="a third fact")
            DogFact.create(id=4, fact="a four fact")
        except Exception as error:
            raise ApiException("error running migration to DB: {}".format(str(error))) from error

    def migration_mvc(self):
        try:
            self.database.create_tables([User, Store])
            User.truncate_table()
            Store.truncate_table()
            user = User.create(id=1, name='Hommer', cpf_cnpj='1234567890')
            Store.create(id=1, name='xablau', user=user)
        except Exception as error:
            raise ApiException("error running migration to DB: {}".format(str(error))) from error

    def get_db(self) -> Database:
        return self.database
