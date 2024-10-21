Comandos SQL Comuns
SELECT: Usado para selecionar dados de uma tabela.


SELECT coluna1, coluna2 FROM tabela;

INSERT: Usado para inserir novos dados em uma tabela. 

INSERT INTO
    tabela (coluna1, coluna2)
VALUES (valor1, valor2);

UPDATE: Usado para modificar dados existentes em uma tabela. 

UPDATE tabela
SET
    coluna1 = novo_valor
WHERE
    condição;

DELETE: Usado para excluir dados de uma tabela. 

DELETE FROM tabela WHERE condição;

CREATE TABLE: Usado para criar uma nova tabela. 

CREATE TABLE tabela (
    coluna1 tipo_dado,
    coluna2 tipo_dado
);

ALTER TABLE: Usado para modificar a estrutura de uma tabela existente (como adicionar ou remover colunas).


ALTER TABLE tabela ADD coluna tipo_dado;

DROP TABLE: Usado para excluir uma tabela do banco de dados. 

DROP TABLE tabela;

Consultas Avançadas
JOIN: Usado para combinar registros de duas ou mais tabelas com base em uma condição relacionada.


SELECT coluna1, coluna2
FROM tabela1
    JOIN tabela2 ON tabela1.coluna_comum = tabela2.coluna_comum;

WHERE: Usado para filtrar registros com base em condições específicas.


SELECT * FROM tabela WHERE coluna = valor;

GROUP BY: Usado para agrupar registros com valores iguais em colunas específicas.


SELECT coluna, COUNT(*)
FROM tabela
GROUP BY
    coluna;

ORDER BY: Usado para ordenar os resultados de uma consulta. 

SELECT * FROM tabela ORDER BY coluna ASC | DESC;