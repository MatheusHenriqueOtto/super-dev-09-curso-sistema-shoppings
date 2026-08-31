from fastapi import APIRouter

from src.repositories import clientes_repository


router = APIRouter()


# =========================
# LISTAR TODOS
# =========================

@router.get("/clientes")
def listar_clientes():
    return clientes_repository.consultar_todos()


# =========================
# BUSCAR POR ID
# =========================

@router.get("/clientes/{id_cliente}")
def buscar_cliente(id_cliente: int):
    return clientes_repository.consultar_por_id(id_cliente)


# =========================
# CADASTRAR
# =========================

@router.post("/clientes")
def cadastrar_cliente(
    nome: str,
    cpf: str,
    telefone: str | None = None
):
    clientes_repository.cadastrar(
        nome,
        cpf,
        telefone
    )

    return {
        "mensagem": "Cliente cadastrado com sucesso!"
    }


# =========================
# ATUALIZAR
# =========================

@router.put("/clientes/{id_cliente}")
def atualizar_cliente(
    id_cliente: int,
    nome: str,
    cpf: str,
    telefone: str | None = None
):
    sucesso = clientes_repository.atualizar(
        id_cliente,
        nome,
        cpf,
        telefone
    )

    if not sucesso:
        return {
            "mensagem": "Cliente não encontrado!"
        }

    return {
        "mensagem": "Cliente atualizado com sucesso!"
    }


# =========================
# ALTERAR STATUS
# =========================

@router.patch("/clientes/{id_cliente}/status")
def alterar_status(
    id_cliente: int,
    registro_ativo: bool
):
    sucesso = clientes_repository.alterar_status(
        id_cliente,
        registro_ativo
    )

    if not sucesso:
        return {
            "mensagem": "Cliente não encontrado!"
        }

    return {
        "mensagem": "Status alterado com sucesso!"
    }


# =========================
# EXCLUIR
# =========================

@router.delete("/clientes/{id_cliente}")
def excluir_cliente(id_cliente: int):

    sucesso = clientes_repository.excluir(id_cliente)

    if not sucesso:
        return {
            "mensagem": "Cliente não encontrado!"
        }

    return {
        "mensagem": "Cliente excluído com sucesso!"
    }
