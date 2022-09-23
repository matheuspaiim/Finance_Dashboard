CREATE DATABASE finance_dashboard;

USE finance_dashboard;

CREATE TABLE registro (
	id INT NOT NULL AUTO_INCREMENT,
    descricao VARCHAR(255),
    escolha VARCHAR(30),
    data_entrada DATE NOT NULL,
    quantia FLOAT(10,2) NOT NULL,
    PRIMARY KEY(id)
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
CREATE TABLE usuario (
	id INT NOT NULL AUTO_INCREMENT,
    primeiro_nome VARCHAR(30),
    ultimo_nome VARCHAR(30),
	email VARCHAR(100),
	senha VARCHAR(100),
	PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE investimentos (
	id INT NOT NULL AUTO_INCREMENT,
    investimento VARCHAR(40),
    codigo_negociacao VARCHAR(40),
    nome_fundo VARCHAR(50),
    titulo_privado VARCHAR(50),
    tipo_taxa VARCHAR(30),
    taxa FLOAT(5,2) NOT NULL,
    taxa_adicional FLOAT(5,2) NOT NULL,
    data_compra DATE NOT NULL,
    data_vencimento DATE NOT NULL,
    banco VARCHAR(30),
    corretora VARCHAR(30),
    quantidade FLOAT(10,2) NOT NULL,
    taxa_corretagem FLOAT(10,2),
    outras_taxas FLOAT(10,2),
    titulo_tesouro VARCHAR(50),
    codigo_cetip VARCHAR(20),
    codigo_debenture VARCHAR(20),
    codigo_ativo_objeto VARCHAR(20),
    codigo_coe VARCHAR(50),
    moeda VARCHAR(30),
    PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;