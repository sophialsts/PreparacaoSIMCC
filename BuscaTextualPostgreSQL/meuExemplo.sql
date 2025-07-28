CREATE EXTENSION IF NOT EXISTS unaccent;

CREATE TEXT SEARCH CONFIGURATION public.multi_unaccent (COPY = simple);

ALTER TEXT SEARCH CONFIGURATION public.multi_unaccent
    ALTER MAPPING FOR hword, hword_part, word
    WITH unaccent;

ALTER TABLE Producoes ADD COLUMN IF NOT EXISTS documento_fts tsvector;

UPDATE Producoes pr
SET documento_fts =
    setweight(to_tsvector('public.multi_unaccent', coalesce(pr.nomeartigo, '')), 'A') ||
    setweight(to_tsvector('public.multi_unaccent', coalesce((SELECT p.nome FROM Pesquisadores p WHERE p.pesquisadores_id = pr.pesquisadores_id), '')), 'D');

DROP INDEX IF EXISTS index_fts;
CREATE INDEX index_fts ON Producoes USING gin(documento_fts);

SELECT
    p.nome,
    pr.nomeartigo,
    ts_rank_cd(pr.documento_fts, to_tsquery('public.multi_unaccent', 'eduardo & system')) AS rank
FROM
    Pesquisadores p
JOIN
    Producoes pr ON p.pesquisadores_id = pr.pesquisadores_id
WHERE
    pr.documento_fts @@ to_tsquery('public.multi_unaccent', 'eduardo & system')
ORDER BY
    rank DESC;
