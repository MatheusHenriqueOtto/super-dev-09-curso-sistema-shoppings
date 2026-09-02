from fastapi import APIRouter, HTTPException

from src.repositories import contratos_repository
from src.schemas.contratos import ContratoCadastro, ContratoEditar

router = APIRouter()

@router.get("/contratos")
def listar_contratos():
    return contratos_repository.consultar_todos()

@router.get("/contratos/{id}")
def buscar_contrato(id: int):
    contrato = contratos_repository.consultar_por_id(id)
    if contrato is None:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return contrato

@router.post("/contratos")
def cadastrar_contrato(item: ContratoCadastro):
    return contratos_repository.cadastrar(item)

@router.put("/contratos/{id}")
def atualizar_contrato(id: int, item: ContratoEditar):
    if contratos_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    contratos_repository.atualizar(id, item)
    return {"mensagem": "Contrato atualizado com sucesso"}

@router.patch("/contratos/{id}/status")
def alterar_status_contrato(id: int, registro_ativo: bool):
    if not contratos_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/contratos/{id}")
def excluir_contrato(id: int):
    if contratos_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    contratos_repository.excluir(id)
    return {"mensagem": "Contrato excluído com sucesso"}
