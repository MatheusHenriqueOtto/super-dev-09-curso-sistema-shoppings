from dataclasses import dataclass

@dataclass
class Shopping:
    id: int
    nome: str
    cnpj: str
    cidade: str
    registro_ativo: bool


