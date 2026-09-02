from fastapi import APIRouter, HTTPException

from src.repositories import estacionamento_repository
from src.schemas.estacionamento import EstacionamentoCadastro, EstacionamentoEditar

router = APIRouter()

@router.get("/estacionamento")
def listar_estacionamentos():
    return estacionamento_repository.consultar_todos()

@router.get("/estacionamento/{id}")
def buscar_estacionamento(id: int):
    item = estacionamento_repository.consultar_por_id(id)
    if item is None:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    return item

@router.post("/estacionamento")
def cadastrar_estacionamento(item: EstacionamentoCadastro):
    return estacionamento_repository.cadastrar(item)

@router.put("/estacionamento/{id}")
def atualizar_estacionamento(id: int, item: EstacionamentoEditar):
    if estacionamento_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    estacionamento_repository.atualizar(id, item)
    return {"mensagem": "Estacionamento atualizado com sucesso"}

@router.patch("/estacionamento/{id}/status")
def alterar_status_estacionamento(id: int, registro_ativo: bool):
    if not estacionamento_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/estacionamento/{id}")
def excluir_estacionamento(id: int):
    if estacionamento_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Estacionamento não encontrado")
    estacionamento_repository.excluir(id)
    return {"mensagem": "Estacionamento excluído com sucesso"}
