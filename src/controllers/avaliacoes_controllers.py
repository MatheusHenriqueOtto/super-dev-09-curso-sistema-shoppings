from fastapi import APIRouter, HTTPException

from src.repositories import avaliacoes_repository
from src.schemas.avaliacoes import AvaliacaoCadastro, AvaliacaoEditar

router = APIRouter()

@router.get("/avaliacoes")
def listar_avaliacoes():
    return avaliacoes_repository.consultar_todos()

@router.get("/avaliacoes/{id}")
def buscar_avaliacao(id: int):
    avaliacao = avaliacoes_repository.consultar_por_id(id)
    if avaliacao is None:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacao

@router.post("/avaliacoes")
def cadastrar_avaliacao(item: AvaliacaoCadastro):
    return avaliacoes_repository.cadastrar(item)

@router.put("/avaliacoes/{id}")
def atualizar_avaliacao(id: int, item: AvaliacaoEditar):
    if avaliacoes_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    avaliacoes_repository.atualizar(id, item)
    return {"mensagem": "Avaliação atualizada com sucesso"}

@router.patch("/avaliacoes/{id}/status")
def alterar_status_avaliacao(id: int, registro_ativo: bool):
    if not avaliacoes_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/avaliacoes/{id}")
def excluir_avaliacao(id: int):
    if avaliacoes_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    avaliacoes_repository.excluir(id)
    return {"mensagem": "Avaliação excluída com sucesso"}
