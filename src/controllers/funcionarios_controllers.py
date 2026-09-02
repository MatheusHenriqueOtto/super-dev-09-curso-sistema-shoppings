from fastapi import APIRouter, HTTPException

from src.repositories import funcionarios_repository
from src.schemas.funcionarios import FuncionarioCadastro, FuncionarioEditar

router = APIRouter()

@router.get("/funcionarios")
def listar_funcionarios():
    return funcionarios_repository.consultar_todos()

@router.get("/funcionarios/{id}")
def buscar_funcionario(id: int):
    funcionario = funcionarios_repository.consultar_por_id(id)
    if funcionario is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

@router.post("/funcionarios")
def cadastrar_funcionario(funcionario: FuncionarioCadastro):
    return funcionarios_repository.cadastrar(funcionario)

@router.put("/funcionarios/{id}")
def atualizar_funcionario(id: int, funcionario: FuncionarioEditar):
    if funcionarios_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    funcionarios_repository.atualizar(id, funcionario)
    return {"mensagem": "Funcionário atualizado com sucesso"}

@router.patch("/funcionarios/{id}/status")
def alterar_status_funcionario(id: int, registro_ativo: bool):
    if not funcionarios_repository.alterar_status(id, registro_ativo):
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return {"mensagem": "Status alterado com sucesso"}

@router.delete("/funcionarios/{id}")
def excluir_funcionario(id: int):
    if funcionarios_repository.consultar_por_id(id) is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    funcionarios_repository.excluir(id)
    return {"mensagem": "Funcionário excluído com sucesso"}
