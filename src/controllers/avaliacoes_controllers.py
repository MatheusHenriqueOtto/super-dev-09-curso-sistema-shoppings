from fastapi import APIRouter

from src.repositories import avaliacoes_repository


router = APIRouter()


# =========================
# LISTAR TODOS
# =========================

@router.get("/avaliacoes")
def listar_avaliacoes():
    return avaliacoes_repository.consultar_todos()


# =========================
# BUSCAR POR ID
# =========================

@router.get("/avaliacoes/{id_avaliacao}")
def buscar_avaliacao(id_avaliacao: int):
    return avaliacoes_repository.consultar_por_id(id_avaliacao)


# =========================
# CADASTRAR
# =========================

@router.post("/avaliacoes")
def cadastrar_avaliacao(
    nota: int,
    comentario: str | None = None,
    id_cliente: int = 0
):
    avaliacoes_repository.cadastrar(
        nota,
        comentario,
        id_cliente
    )

    return {
        "mensagem": "Avaliação cadastrada com sucesso!"
    }


# =========================
# ATUALIZAR
# =========================

@router.put("/avaliacoes/{id_avaliacao}")
def atualizar_avaliacao(
    id_avaliacao: int,
    nota: int,
    comentario: str | None = None,
    id_cliente: int = 0
):
    sucesso = avaliacoes_repository.atualizar(
        id_avaliacao,
        nota,
        comentario,
        id_cliente
    )

    if not sucesso:
        return {
            "mensagem": "Avaliação não encontrada!"
        }

    return {
        "mensagem": "Avaliação atualizada com sucesso!"
    }


# =========================
# ALTERAR STATUS
# =========================

@router.patch("/avaliacoes/{id_avaliacao}/status")
def alterar_status(
    id_avaliacao: int,
    registro_ativo: bool
):
    sucesso = avaliacoes_repository.alterar_status(
        id_avaliacao,
        registro_ativo
    )

    if not sucesso:
        return {
            "mensagem": "Avaliação não encontrada!"
        }

    return {
        "mensagem": "Status alterado com sucesso!"
    }


# =========================
# EXCLUIR
# =========================

@router.delete("/avaliacoes/{id_avaliacao}")
def excluir_avaliacao(id_avaliacao: int):

    sucesso = avaliacoes_repository.excluir(id_avaliacao)

    if not sucesso:
        return {
            "mensagem": "Avaliação não encontrada!"
        }

    return {
        "mensagem": "Avaliação excluída com sucesso!"
    }