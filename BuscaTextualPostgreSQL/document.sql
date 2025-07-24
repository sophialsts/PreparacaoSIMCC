-- crio um arquivo que junta as informações do nome do artigo, nome do autor, issn dele e ano de publicação
SELECT 
    pr.nomeartigo || ' ' || 
    p.nome || ' ' || 
    COALESCE(pr.issn, '') || ' ' || 
    pr.anoartigo::TEXT AS document
FROM 
    Producoes pr
    JOIN Pesquisadores p ON p.pesquisadores_id = pr.pesquisadores_id;
