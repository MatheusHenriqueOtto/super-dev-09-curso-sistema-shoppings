DROP DATABASE IF EXISTS mallverse_db;

CREATE DATABASE mallverse_db;

USE mallverse_db;

CREATE TABLE shoppings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    registro_ativo BIT NOT NULL DEFAULT(1)
);

CREATE TABLE lojas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_fantasia VARCHAR(100) NOT NULL,
    numero_modulo VARCHAR(20) NOT NULL,
    id_shopping INT NOT NULL,
    FOREIGN KEY (id_shopping) REFERENCES shoppings(id),
    registro_ativo BIT NOT NULL DEFAULT(1)
);

CREATE TABLE funcionarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_loja INT NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES lojas(id),
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    registro_ativo BIT NOT NULL DEFAULT(1)
);

CREATE TABLE clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    telefone VARCHAR(20),
    registro_ativo BIT NOT NULL DEFAULT(1)
);



CREATE TABLE estacionamento (
    id INT PRIMARY KEY AUTO_INCREMENT,
    setor VARCHAR(50) NOT NULL,
    capacidade_vagas INT NOT NULL DEFAULT 0,
    id_shopping INT,
    FOREIGN KEY (id_shopping) REFERENCES shoppings(id),
    registro_ativo BIT NOT NULL DEFAULT(1)
);

CREATE TABLE avaliacoes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nota INT NOT NULL,
    comentario TEXT,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    registro_ativo BIT NOT NULL DEFAULT(1)

    CONSTRAINT fk_avaliacao_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(id)
);

CREATE TABLE contratos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_aluguel FLOAT NOT NULL,
    id_loja INT NOT NULL,
    FOREIGN KEY (id_loja) REFERENCES lojas(id),
    id_shopping INT NOT NULL,
    FOREIGN KEY (id_shopping) REFERENCES shoppings(id),
    registro_ativo BIT NOT NULL DEFAULT(1)
);