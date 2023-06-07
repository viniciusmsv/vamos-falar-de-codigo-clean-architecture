from peewee import CharField, IntegerField, Model, ForeignKeyField


class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    cpf_cnpj = CharField(max_length=255)


class Store(Model):
    id = IntegerField(primary_key=True)
    user = ForeignKeyField(User, backref='stores')
    name = CharField(max_length=255)
