from fastapi import APIRouter, HTTPException

from src.repositories import lojas_repository
from src.schemas.lojas import LojaCadastro, LojaEditar

router = APIRouter()

@router.get("/lojas")
def listar_lojas():
    return lojas_repository.consultar_todos()

@router.get("/lojas/{id}")
def buscar_loja(id: int):
    loja = lojas_repository.consultar_por_id(id)
    if loja is None:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return loja

@router.post("/lojas")
def cadastrar_loja(loja: LojaCadastro):
    return lojas_repository.cadastrar(loja)

@router.put("/lojas/{id}")
def atualizar_loja(id: int, loja: LojaEditar):
    if lojas_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    lojas_repository.atualizar(id, loja)
    return {"mensagem": "Loja atualizada com sucesso"}

@router.patch("/lojas/{id}/status")
def alterar_status_loja(id: int, registro_ativo: bool):
    if not lojas_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/lojas/{id}")
def excluir_loja(id: int):
    if lojas_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Loja não encontrada")
    lojas_repository.excluir(id)
    return {"mensagem": "Loja excluída com sucesso"}
