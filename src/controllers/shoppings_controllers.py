from fastapi import APIRouter, HTTPException

from src.repositories import shoppings_repository
from src.schemas.shoppings import ShoppingCadastro, ShoppingEditar

router = APIRouter()

@router.get("/shoppings")
def listar_shoppings():
    return shoppings_repository.consultar_todos()

@router.get("/shoppings/{id}")
def buscar_shopping(id: int):
    shopping = shoppings_repository.consultar_por_id(id)
    if shopping is None:
        raise HTTPException(status_code=404, detail="Shopping não encontrado")
    return shopping

@router.post("/shoppings")
def cadastrar_shopping(shopping: ShoppingCadastro):
    return shoppings_repository.cadastrar(shopping)

@router.put("/shoppings/{id}")
def atualizar_shopping(id: int, shopping: ShoppingEditar):
    if shoppings_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Shopping não encontrado")
    shoppings_repository.atualizar(id, shopping)
    return {"mensagem": "Shopping atualizado com sucesso"}

@router.patch("/shoppings/{id}/status")
def alterar_status_shopping(id: int, registro_ativo: bool):
    if not shoppings_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Shopping não encontrado")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/shoppings/{id}")
def excluir_shopping(id: int):
    if shoppings_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Shopping não encontrado")
    shoppings_repository.excluir(id)
    return {"mensagem": "Shopping excluído com sucesso"}
