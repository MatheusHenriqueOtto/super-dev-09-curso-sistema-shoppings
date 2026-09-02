from dataclasses import dataclass


@dataclass
class Avaliacao:
    id: int
    nota: int
    comentario: str | None
    id_cliente: int
    registro_ativo: bool


@dataclass
class AvaliacaoCadastro:
    nota: int
    id_cliente: int
    comentario: str | None = None


@dataclass
class AvaliacaoEditar:
    nota: int
    id_cliente: int
    comentario: str | None = None
