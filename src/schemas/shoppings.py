from dataclasses import dataclass


@dataclass
class Shopping:
    id: int
    nome: str
    cnpj: str
    cidade: str
    registro_ativo: bool


@dataclass
class ShoppingCadastro:
    nome: str
    cnpj: str
    cidade: str


@dataclass
class ShoppingEditar:
    nome: str
    cnpj: str
    cidade: str
