from src.domain.base_entity import BaseEntity


class UserEntity(BaseEntity):

    def __init__(self, id: int, name: str, cpf_cnpj: str) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.cpf_cnpj = cpf_cnpj
