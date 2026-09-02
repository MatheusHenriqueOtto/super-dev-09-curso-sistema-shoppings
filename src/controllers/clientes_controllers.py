from fastapi import APIRouter, HTTPException

from src.repositories import clientes_repository
from src.schemas.clientes import ClienteCadastro, ClienteEditar

router = APIRouter()

@router.get("/clientes")
def listar_clientes():
    return clientes_repository.consultar_todos()

@router.get("/clientes/{id}")
def buscar_cliente(id: int):
    cliente = clientes_repository.consultar_por_id(id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.post("/clientes")
def cadastrar_cliente(cliente: ClienteCadastro):
    return clientes_repository.cadastrar(cliente)

@router.put("/clientes/{id}")
def atualizar_cliente(id: int, cliente: ClienteEditar):
    if clientes_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    clientes_repository.atualizar(id, cliente)
    return {"mensagem": "Cliente atualizado com sucesso"}

@router.patch("/clientes/{id}/status")
def alterar_status_cliente(id: int, registro_ativo: bool):
    if not clientes_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/clientes/{id}")
def excluir_cliente(id: int):
    if clientes_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    clientes_repository.excluir(id)
    return {"mensagem": "Cliente excluído com sucesso"}
