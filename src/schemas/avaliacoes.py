from pydantic import BaseModel


class Avaliacao(BaseModel):
    id: int
    nota: int
    comentario: str | None
    id_cliente: int
    registro_ativo: bool