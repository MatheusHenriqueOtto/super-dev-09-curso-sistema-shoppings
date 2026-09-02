

from src.repositories import shoppings_repository
from src.schemas.shoppings import Shopping, ShoppingCadastro, ShoppingEditar
from fastapi import APIRouter, HTTPException, status


router = APIRouter()

@router.get("/shoppings")
def listar_shoppings():
    return shoppings_repository.consultar_todos()


@router.post("/shoppings")
def cadastrar_shpping(shopping: ShoppingCadastro):
    return shoppings_repository.cadastrar(shopping)


@router.put("/shoppings/{id}")
def editar_shopping(id: int, shopping: ShoppingEditar):
    shopping_banco = shoppings_repository.consultar_por_id(id)

    if shopping_banco is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon não encontrado")

    shoppings_repository.editar(id, shopping)
    return {
        "status": "ok"
    }