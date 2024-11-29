


CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    marca VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);


DELIMITER $$

CREATE PROCEDURE InsertProduto (
    IN nomeProduto VARCHAR(255),
    IN marcaProduto VARCHAR(255),
    IN valorProduto DECIMAL(10,2)
)
BEGIN
    INSERT INTO produtos (nome, marca, valor)
    VALUES (nomeProduto, marcaProduto, valorProduto);
END $$

DELIMITER ;