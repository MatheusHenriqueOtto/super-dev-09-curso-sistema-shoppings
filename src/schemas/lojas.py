from dataclasses import dataclass


@dataclass
class Loja:
    id: int
    nome_fantasia: str
    numero_modulo: str
    id_shopping: int
    registro_ativo: bool


@dataclass
class LojaCadastro:
    nome_fantasia: str
    numero_modulo: str
    id_shopping: int


@dataclass
class LojaEditar:
    nome_fantasia: str
    numero_modulo: str
    id_shopping: int
