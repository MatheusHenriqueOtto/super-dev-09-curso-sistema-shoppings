from dataclasses import dataclass
from datetime import date


@dataclass
class Contrato:
    id: int
    data_inicio: date
    data_fim: date
    valor_aluguel: float
    id_loja: int
    id_shopping: int
    registro_ativo: bool


@dataclass
class ContratoCadastro:
    data_inicio: date
    data_fim: date
    valor_aluguel: float
    id_loja: int
    id_shopping: int


@dataclass
class ContratoEditar:
    data_inicio: date
    data_fim: date
    valor_aluguel: float
    id_loja: int
    id_shopping: int
