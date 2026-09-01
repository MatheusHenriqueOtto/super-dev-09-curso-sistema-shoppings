from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    telefone: str | None
    registro_ativo: bool

