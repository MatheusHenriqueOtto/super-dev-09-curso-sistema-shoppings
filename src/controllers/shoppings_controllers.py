

from src.repositories import shoppings_repository
from src.schemas.shoppings import Shopping, ShoppingCadastro
from fastapi import APIRouter 


router = APIRouter()

@router.get("/shoppings")
def listar_shoppings():
    return shoppings_repository.consultar_todos()


@router.post("/shoppings")
def cadastrar_shpping(shopping: ShoppingCadastro):
    return shoppings_repository.cadastrar(shopping)
