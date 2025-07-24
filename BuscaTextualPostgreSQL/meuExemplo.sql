ALTER TABLE Producoes ADD COLUMN documento_fts tsvector;
UPDATE Producoes pr
SET documento_fts = to_tsvector('portuguese', 
    pr.nomeartigo || ' ' || 
    (SELECT nome FROM Pesquisadores p WHERE p.pesquisadores_id = pr.pesquisadores_id)
);
CREATE INDEX index_fts ON Producoes USING gin(documento_fts);

SELECT
    p.nome,
    pr.nomeartigo
FROM
    Pesquisadores p
JOIN
    Producoes pr ON p.pesquisadores_id = pr.pesquisadores_id
WHERE
    pr.documento_fts @@ to_tsquery('portuguese', 'eduardo');
