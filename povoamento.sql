-- Povoamento da tabela 'shoppings'
INSERT INTO shoppings (nome, cnpj, cidade, registro_ativo) VALUES
('Shopping Plaza Sul', '12.345.678/0001-90', 'São Paulo', 1),
('Grand Park Mall', '98.765.432/0001-10', 'Rio de Janeiro', 1),
('Central Park Shopping', '45.678.912/0001-34', 'Belo Horizonte', 1),
('Via Norte Shopping', '55.443.221/0001-88', 'Campinas', 1),
('Shopping Beira Mar', '77.889.900/0001-55', 'Florianópolis', 1),
('Boulevard Express', '33.221.100/0001-66', 'Curitiba', 1);

-- Povoamento da tabela 'lojas'
INSERT INTO lojas (nome_fantasia, numero_modulo, id_shopping, registro_ativo) VALUES
('Livraria Saber', 'L1-101', 1, 1),
('Moda Viva', 'L1-102', 1, 1),
('Burguer Tech', 'F2-205', 1, 1),
('Gamer Zone', 'L2-210', 2, 1),
('Café Central', 'L1-105', 3, 1),
('Tech World', 'L2-201', 1, 1),
('Sabor & Arte Cafe', 'F1-102', 2, 1),
('Óticas Visão', 'L1-108', 2, 1),
('Sapataria Real', 'L1-112', 3, 1),
('Livraria do Conhecimento', 'L3-301', 4, 1);

-- Povoamento da tabela 'funcionarios'
INSERT INTO funcionarios (id_loja, nome, cpf, cargo, registro_ativo) VALUES
(1, 'Carlos Eduardo Silva', '111.222.333-44', 'Gerente', 1),
(1, 'Ana Paula Souza', '222.333.444-55', 'Atendente', 1),
(2, 'Mariana Costa', '333.444.555-66', 'Vendedora', 1),
(3, 'Roberto Lima', '444.555.666-77', 'Cozinheiro', 1),
(4, 'Fernanda Oliveira', '555.666.777-88', 'Atendente', 1),
(2, 'Patricia Mendes', '123.987.456-00', 'Gerente', 1),
(3, 'Felipe Augusto Rossi', '321.654.987-11', 'Caixa', 1),
(4, 'Vanessa Camargo', '789.456.123-22', 'Vendedora', 1),
(5, 'Thiago Alcantara', '654.321.987-33', 'Atendente', 1),
(6, 'Juliana Paes Costa', '987.123.654-44', 'Supervisora', 1);

-- Povoamento da tabela 'clientes'
INSERT INTO clientes (nome, cpf, telefone, registro_ativo) VALUES
('Lucas Martins', '666.777.888-99', '(11) 98765-4321', 1),
('Beatriz Ribeiro', '777.888.999-00', '(21) 99876-5432', 1),
('Camila Rodrigues', '888.999.000-11', '(31) 97654-3210', 1),
('Gabriel Santos', '999.000.111-22', NULL, 1),
('Renata Vasconcelos', '112.223.334-55', '(19) 98111-2233', 1),
('Marcelo Oliveira', '445.556.667-88', '(48) 99222-3344', 1),
('Aline Farias', '778.889.990-11', NULL, 1),
('Diego Guimarães', '223.334.445-66', '(41) 98333-4455', 1);

-- Povoamento da tabela 'estacionamento'
INSERT INTO estacionamento (setor, capacidade_vagas, id_shopping, registro_ativo) VALUES
('Setor A - Coberto', 150, 1, 1),
('Setor B - Subsolo', 200, 1, 1),
('Setor VIP', 50, 2, 1),
('Estacionamento Externo', 100, 3, 1),
('Setor Premium - Valet', 40, 1, 1),
('Setor C - Descoberto', 180, 2, 1),
('Estacionamento Motos', 60, 4, 1),
('Setor A - Subsolo', 220, 5, 1);

-- Povoamento da tabela 'avaliacoes'
INSERT INTO avaliacoes (nota, comentario, id_cliente, registro_ativo) VALUES
(5, 'Excelente estrutura e ótimas lojas!', 1, 1),
(4, 'Bom atendimento, mas o estacionamento é caro.', 2, 1),
(3, 'Falta sinalização nas áreas comuns.', 3, 1),
(5, 'Praça de alimentação muito variada.', 4, 1),
(4, 'Ótima variedade de lojas de vestuário.', 5, 1),
(2, 'O ar condicionado da praça de alimentação estava fraco.', 6, 1),
(5, 'Limpeza impecável dos banheiros e bom atendimento.', 7, 1),
(4, 'Fácil acesso e boas opções de estacionamento.', 8, 1);

-- Povoamento da tabela 'contratos'
INSERT INTO contratos (data_inicio, data_fim, valor_aluguel, id_loja, id_shopping, registro_ativo) VALUES
('2024-01-01', '2026-01-01', 4500.00, 1, 1, 1),
('2024-02-01', '2025-02-01', 3800.50, 2, 1, 1),
('2023-06-15', '2025-06-15', 5200.00, 3, 1, 1),
('2024-03-01', '2027-03-01', 6100.00, 4, 2, 1),
('2023-11-01', '2025-11-01', 2900.00, 5, 3, 1),
('2024-04-01', '2026-04-01', 3200.00, 6, 1, 1),
('2023-08-10', '2025-08-10', 4100.00, 7, 2, 1),
('2024-05-15', '2027-05-15', 5500.00, 8, 2, 1),
('2023-12-01', '2025-12-01', 2800.00, 9, 3, 1),
('2024-01-10', '2026-01-10', 6800.00, 10, 4, 1);