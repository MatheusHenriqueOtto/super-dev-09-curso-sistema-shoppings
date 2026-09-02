from dataclasses import dataclass


@dataclass
class Funcionario:
    id: int
    id_loja: int
    nome: str
    cpf: str
    cargo: str
    registro_ativo: bool


@dataclass
class FuncionarioCadastro:
    id_loja: int
    nome: str
    cpf: str
    cargo: str


@dataclass
class FuncionarioEditar:
    id_loja: int
    nome: str
    cpf: str
    cargo: str
