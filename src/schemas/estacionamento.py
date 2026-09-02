from dataclasses import dataclass


@dataclass
class Estacionamento:
    id: int
    setor: str
    capacidade_vagas: int
    id_shopping: int | None
    registro_ativo: bool


@dataclass
class EstacionamentoCadastro:
    setor: str
    capacidade_vagas: int
    id_shopping: int | None = None


@dataclass
class EstacionamentoEditar:
    setor: str
    capacidade_vagas: int
    id_shopping: int | None = None
