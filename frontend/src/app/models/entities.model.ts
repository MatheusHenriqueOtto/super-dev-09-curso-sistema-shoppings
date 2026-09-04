export interface Entity { id: number; registro_ativo: boolean; [key: string]: string | number | boolean | null | undefined; }
export interface Shopping extends Entity { nome: string; cnpj: string; cidade: string; }
export interface Loja extends Entity { nome_fantasia: string; numero_modulo: string; id_shopping: number; }
export interface Funcionario extends Entity { id_loja: number; nome: string; cpf: string; cargo: string; }
export interface Cliente extends Entity { nome: string; cpf: string; telefone?: string | null; }
export interface Estacionamento extends Entity { setor: string; capacidade_vagas: number; id_shopping?: number | null; }
export interface Avaliacao extends Entity { nota: number; comentario?: string | null; id_cliente: number; }
export interface Contrato extends Entity { data_inicio: string; data_fim: string; valor_aluguel: number; id_loja: number; id_shopping: number; }
