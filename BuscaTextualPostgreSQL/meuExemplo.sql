-- extensão para remover os acentos
CREATE EXTENSION IF NOT EXISTS unaccent;

-- configura para tirar acentos e fazer stemming
DROP TEXT SEARCH CONFIGURATION IF EXISTS public.portuguese_unaccent;
CREATE TEXT SEARCH CONFIGURATION public.portuguese_unaccent (COPY = pg_catalog.portuguese);

-- aplicar unnacent antes do stemming
ALTER TEXT SEARCH CONFIGURATION public.portuguese_unaccent
  ALTER MAPPING FOR hword, hword_part, word
  WITH unaccent, portuguese_stem;

-- confirmar que a coluna de documento_fts vai ser do tipo tsvector
ALTER TABLE Producoes
  ALTER COLUMN documento_fts TYPE tsvector
  USING documento_fts::tsvector;

-- vai atualizar a coluna com os lexemas de nome de artigo e nome, com peso maior para nome do de artigo
UPDATE Producoes pr
SET documento_fts = 
    setweight(to_tsvector('public.portuguese_unaccent', coalesce(pr.nomeartigo, '')), 'A') ||
    setweight(to_tsvector('public.portuguese_unaccent', coalesce(p.nome, '')), 'D')
FROM Pesquisadores p
WHERE p.pesquisadores_id = pr.pesquisadores_id;

-- criar o índice GIN para documento_fts
CREATE INDEX IF NOT EXISTS idx_producoes_documento_fts
  ON Producoes
  USING GIN (documento_fts);

-- faz a busca e ordena em ordem decrescente
-- websearch_to_tsquery aceita melhor as variações de palavras
SELECT
    p.nome,
    pr.nomeartigo,
    ts_rank_cd(pr.documento_fts, websearch_to_tsquery('public.portuguese_unaccent', 'eduard robótica')) AS rank
FROM
    Pesquisadores p
JOIN
    Producoes pr ON p.pesquisadores_id = pr.pesquisadores_id
WHERE
    pr.documento_fts @@ websearch_to_tsquery('public.portuguese_unaccent', 'eduard robótica')
ORDER BY
    rank DESC;
