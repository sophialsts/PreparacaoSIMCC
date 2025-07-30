import conexao_singleton as cs  # Importa a conexão Singleton do banco de dados

banco = cs.Conexao().get_conexao()

# Script para criar as tabelas e extensões
script_sql_criacao = """
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    CREATE TABLE IF NOT EXISTS pesquisadores (
        pesquisadores_id UUID NOT NULL DEFAULT uuid_generate_v4(),
        lattes_id VARCHAR(16) NOT NULL,
        nome VARCHAR(200) NOT NULL,
        PRIMARY KEY (pesquisadores_id)
    );

    CREATE TABLE IF NOT EXISTS producoes (
        producoes_id UUID NOT NULL DEFAULT uuid_generate_v4(),
        pesquisadores_id UUID NOT NULL,
        issn VARCHAR(16) NOT NULL,
        nomeArtigo VARCHAR(400) NOT NULL,
        anoArtigo INTEGER NOT NULL,
        PRIMARY KEY (producoes_id),
        CONSTRAINT fkey FOREIGN KEY (pesquisadores_id) 
        REFERENCES pesquisadores (pesquisadores_id) ON DELETE CASCADE
       
    );
"""

try:
    with banco.cursor() as cursor:
        print("Criando tabelas...")
        cursor.execute(script_sql_criacao)
        banco.commit()  # Confirma a criação das tabelas
        print("Tabelas criadas com sucesso!")
except Exception as e:
    banco.rollback()  # Reverte a transação em caso de erro
    print(f"Erro ao criar tabelas: {e}")
    banco.close()
    exit(1)
    
sql_inserir_pesquisador = """
    INSERT INTO pesquisadores (pesquisadores_id, lattes_id, nome)
    VALUES
    ('1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9','1966167015825708','Hugo Saba Pereira Cardoso'),
    ('8583e3d4-59e0-4361-956e-f0261641a013','6716225567627323','Eduardo Manuel de Freitas Jorge');
"""

sql_inserir_producao = """
    INSERT INTO producoes (producoes_id, pesquisadores_id, issn, nomeArtigo, anoArtigo) 
    VALUES
    ('69096072-fe59-4bab-8f09-8effaa6cc5e7', '8583e3d4-59e0-4361-956e-f0261641a013', '25956825', 'Dinâmica de ensino baseada em fabricação digital e PBL para apoiar os professores de psicologia na apresentação do Teste de Pirâmide Colorida Pfister / Teaching dynamics based on digital fabrication and PBL to support psychology teachers in presenting the Pfister Color Pyramid Test', 2021),
    ('1a920088-ec6e-4cb7-8287-819acfea87e5', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25956825', 'Dinâmica de ensino baseada em fabricação digital e PBL para apoiar os professores de psicologia na apresentação do Teste de Pirâmide Colorida Pfister / Teaching dynamics based on digital fabrication and PBL to support psychology teachers in presenting the Pfister Color Pyramid Test', 2021),
    ('f09320ac-77a3-4955-b440-e6a1b7294f95', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '01672789', 'Scaling effect in COVID-19 spreading: The role of heterogeneity in a hybrid ODE-network model with restrictions on the inter-cities flow', 2021),
    ('af817e68-e5d9-4cb4-92e5-58a935d90675', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '03784371', 'Self-affinity and self-organized criticality applied to the relationship between the economic arrangements and the dengue fever spread in Bahia', 2018),
    ('5a3bbd75-a071-447a-902a-5390ca3a6da7', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '2076393X', 'Retrospective Cohort Study of COVID-19 in Patients of the Brazilian Public Health System with SARS-CoV-2 Omicron Variant Infection', 2022),
    ('35361d0e-f756-4062-a9a0-9f6ad347f995', '8583e3d4-59e0-4361-956e-f0261641a013', '00489697', 'Relevance of transportation to correlations among criticality, physical means of propagation, and distribution of dengue fever cases in the state of Bahia', 2018),
    ('525568d0-0e5d-400b-a2c5-cf0baa827a3c', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00489697', 'Relevance of transportation to correlations among criticality, physical means of propagation, and distribution of dengue fever cases in the state of Bahia', 2018),
    ('4fad23cd-808e-4c8c-acc9-1b038d6d82fc', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '17466148', 'Humoral and cellular immune responses in mice against secreted and somatic antigens from a Corynebacterium pseudotuberculosis attenuated strain: Immune response against a C. pseudotuberculosis strain', 2016),
    ('4f82afdb-1924-4f40-8cb5-6f1ab652e719', '8583e3d4-59e0-4361-956e-f0261641a013', '23189584', 'CENÁRIO DO GRUPO DE APOIO ÀS CRIANÇAS COM CÂNCER (GACC-BA): PROPOSTA DE UM AMBIENTE VIRTUAL COLABORATIVO COMO INSTRUMENTO DE INTERAÇÃO, PARTICIPAÇÃO E CONTRIBUIÇÃO PARA A INSTITUIÇÃO', 2020),
    ('69a14082-843d-4322-8001-61f167f32e5d', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '2296424X', 'Network analysis of spreading of dengue, Zika and chikungunya in the state of Bahia based on notified, confirmed and discarded cases', 2022),
    ('f09e01fa-f1ca-4d73-a202-87876d7af324', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '23293284', 'The Importance of the Facility Location Techniques to Assist Companies in Decision-Making for the Installation of Logistics Hub', 2024),
    ('34f5a6f4-5067-4bc4-bd70-a96727b5d6a2', '8583e3d4-59e0-4361-956e-f0261641a013', '23170026', 'Portal de Acesso às Informações das Ações das Universidades Federais em Resposta à Pandemia de Covid-19: uma análise do período pandêmico até a transição para uma pós-pandemia', 2023),
    ('71423cba-83a6-4663-9013-e6dd63050613', '8583e3d4-59e0-4361-956e-f0261641a013', '21792534', 'Perspectiva teórico epistemológica da modelagem conceitual relacionada com a análise cognitiva e semiótica no contexto da difusão do conhecimento em ambientes virtuais de aprendizagem', 2012),
    ('e1504318-3246-4a65-91f7-dfc91cb357c0', '8583e3d4-59e0-4361-956e-f0261641a013', '20711050', 'Analysis of Hydrous Ethanol Price Competitiveness after the Implementation of the Fossil Fuel Import Price Parity Policy in Brazil', 2021),
    ('f4c19b6f-2747-4a27-a5a0-b4d2ba7d18e1', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '20711050', 'Analysis of Hydrous Ethanol Price Competitiveness after the Implementation of the Fossil Fuel Import Price Parity Policy in Brazil', 2021),
    ('36556101-f813-444d-86f3-27e4eb4fb183', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25254553', 'CENÁRIO DO GRUPO DE APOIO ÀS CRIANÇAS COM CÂNCER (GACCBA): PROPOSTA DE UM AMBIENTE VIRTUAL COLABORATIVO COMO INSTRUMENTO DE INTERAÇÃO, PARTICIPAÇÃO E CONTRIBUIÇÃO PARA A INSTITUIÇÃO', 2020),
    ('5656c5e3-241b-4968-9f30-93660f7918ef', '8583e3d4-59e0-4361-956e-f0261641a013', '22309926', 'ECOM - COMPUTATIONAL MODEL FOR THE AUTOMATIC SELECTION OF CANDIDATE TERMS FROM TEXT MINING TO ASSIST ONTOLOGY BUILDING', 2017),
    ('3333c37a-a426-4bb8-9de9-06ac8932e325', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '22309926', 'ECOM - Computational Model for the Automatic Selection of Candidate Terms from Text Mining to Assist Ontology Building', 2017),
    ('bc6a1fe3-8e72-4408-ab95-ca7c459d2e5a', '8583e3d4-59e0-4361-956e-f0261641a013', '19832192', 'A REVOLUÇÃO DA ROBÓTICA UTILIZANDO LIXO ELETRÔNICO NO ENSINO BÁSICO: FORMAÇÃO AMPLIADA E MENOR VULNERABILIDADE DE JOVENS À VIOLÊNCIA NAS ESCOLAS PÚBLICAS', 2016),
    ('d2bd8584-b54f-4bc0-8290-289fb600f1eb', '8583e3d4-59e0-4361-956e-f0261641a013', '25253409', 'Spatial-temporal Correlation of Dengue Fever and Climatic Variables in the City of São Paulo, Brazil', 2021),
    ('3ed15d9e-f86f-4d04-b9d3-9c2191fd8f88', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19832192', 'A Revolução da Robótica Utilizando Lixo Eletrônico no Ensino Básico: Formação Ampliada e Menor Vulnerabilidade de Jovens à Violência nas Escolas Públicas', 2016),
    ('d0ea3cc4-e22f-440d-8b5d-0d68a6fcaf11', '8583e3d4-59e0-4361-956e-f0261641a013', '23170026', 'FACE SHIELD FOR LIFE 3D: PRODUÇÃO COLABORATIVA, USANDO A COMUNIDADE DE MAKERS, DOS PROTETORES FACIAIS PADRÃO RC3 PARA OS PROFISSIONAIS DE SAÚDE EM SALVADOR', 2020),
    ('1dbb891e-bcca-4ca8-9122-aa89d1463d18', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19326203', 'Correlation between hospitalized patients? demographics, symptoms, comorbidities, and COVID-19 pandemic in Bahia, Brazil', 2020),
    ('54da782b-a3c7-4e44-ac0d-f03385019bbc', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Spatial-temporal Correlation of Dengue Fever and Climatic Variables in the City of São Paulo, Brazil', 2021),
    ('0f92693d-33e7-4720-bce6-1795b0b5f67e', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '23170026', 'FACE SHIELD FOR LIFE 3D PRODUÇÃO COLABORATIVA USANDO A COMUNIDADE DE MAKERS DOS PROTETORES FACIAIS PADRÃO RC3 PARA OS PROFISSIONAIS DE SAÚDE EM SALVADOR', 2020),
    ('22e532da-1d6b-46c0-8f9c-5867e9e30267', '8583e3d4-59e0-4361-956e-f0261641a013', '23170026', 'CATÁLOGO DE AÇÕES DA AGÊNCIA UNEB DE INOVAÇÃO DURANTE O ANO DE 2018 COM BASE NA ESTRATÉGIA NACIONAL DE CT&I DO BRASIL 2016-2022', 2019),
    ('62da3842-e1fd-43cf-9fab-0d93ea472fe4', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '18093957', 'ROBÓTICA EDUCACIONAL: CONSTRUÇÃO DE UMA DINÂMICA A PARTIR DO ROBÔ ARDU EDUCATIONAL ROBOTICS: BUILDING A DYNAMIC BASED ON ROBOT ARDU', 2020),
    ('c38d1073-28da-4d64-bfff-941366007c6a', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '23170026', 'CATÁLOGO DE AÇÕES DA AGÊNCIA UNEB DE INOVAÇÃO DURANTE O ANO DE 2018 COM BASE NA ESTRATÉGIA NACIONAL DE CT&I DO BRASIL 2016-2022', 2019),
    ('e0a43bd7-0399-4b8e-8ee9-bd1179417b72', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Scenarios and opportunities in the sugar and ethanol industry - challenges and opportunities towards a low carbon economy in Brazil', 2024),
    ('d7ccac6d-57d0-4ecf-bf2b-09778ffab10d', '8583e3d4-59e0-4361-956e-f0261641a013', '19818920', 'Arquitetura da Informação Analítica para Integração de Dados da Pesquisa e Pós-Graduação: Um Estudo de Caso da Universidade do Estado da Bahia', 2020),
    ('1a8d782f-8af2-4e77-9982-02ca8917b089', '8583e3d4-59e0-4361-956e-f0261641a013', '21788030', 'IMPRESSÃO 3D: DA PESQUISA AO SETOR PRODUTIVO Um estudo exploratório sobre sua evolução histórica, origem, tecnologias, aplicações e inovações', 2022),
    ('bb433859-d288-428f-bff2-00f0931ca064', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21757275', 'Uma Revisão Sistemática dos Indicadores da Saúde e Bem-Estar no Brasil: Cenário Atual e Perspectivas Futuras da Agenda 2030', 2023),
    ('35ff3802-ca10-4b67-91ad-1c5d3937ac62', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21788030', 'IMPRESSÃO 3D: DA PESQUISA AO SETOR PRODUTIVO UM ESTUDO EXPLORATÓRIO SOBRE SUA EVOLUÇÃO HISTÓRICA, ORIGEM, TECNOLOGIAS, APLICAÇÕES E INOVAÇÕES', 2022),
    ('21753164-aa12-43b7-a797-7bb3bc294f90', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21788030', 'PRODUÇÃO DE PATENTES NA REGIÃO NORDESTE: UM ESTUDO COMPARATIVO ENTRE INSTITUIÇÕES DE ENSINO SUPERIOR PÚBLICAS NO PERÍODO DE 2002 A 2012', 2016),
    ('ac75f644-c83d-4511-a2e5-aed0e8bb96c8', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00105236', 'Comparison of multilayer perceptron neural network architecture in photovoltaic plants fault classification', 2023),
    ('1674afd3-5cfe-478f-8f9f-a090427cf70d', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00105236', 'Epidemiological outbreaks of dengue, chikungunya and zika from 2015 to 2019: Rio de Janeiro case', 2023),
    ('3baea258-d0ba-4e98-aa7a-7c083e205b8b', '8583e3d4-59e0-4361-956e-f0261641a013', '16604601', 'A Critical Analysis of the COVID-19 Hospitalization Network in Countries with Limited Resources', 2022),
    ('ff7bdde5-0e74-4a66-a59b-f68928f9ee14', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '09600779', 'Complex network analysis of arboviruses in the same geographic domain: Differences and similarities', 2023),
    ('14ca4dad-8de6-4e92-a813-04945842e1cb', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '16604601', 'A Critical Analysis of the COVID-19 Hospitalization Network in Countries with Limited Resources', 2022),
    ('0f7fc80c-1496-45b6-adc8-f8a3c2484fe1', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '20711050', 'Renewable Energy Generation Technologies for Decarbonizing Urban Vertical Buildings: A Path towards Net Zero', 2023),
    ('06242859-d514-4e0c-b832-2893161f8a94', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00105236', 'The complex networks of an entrepreneurship and innovation ecosystem: proposal for a representation model', 2024),
    ('2b011d79-07a9-43b8-b991-29b6ef8207ad', '8583e3d4-59e0-4361-956e-f0261641a013', '21757534', 'PROPOSTA DE (RE)DESIGN DO AMBIENTE EDUCATIVO FORMAL UNIVERSITÁRIO PARA ESTIMULAR UMA APRENDIZAGEM PROTAGONISTA, CRIATIVA E INOVADORA', 2020),
    ('25057642-7e8f-4a7c-8ff1-feff8f7f1a09', '8583e3d4-59e0-4361-956e-f0261641a013', '00105236', 'Maker Culture: dissemination of knowledge and development of skills and competencies for the 21st century', 2023),
    ('766caf99-c807-4d55-a3d3-015e7e244380', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00105236', 'Maker Culture: dissemination of knowledge and development of skills and competencies for the 21st century', 2023),
    ('9cab35cf-b4cf-4d1c-b7c0-0c93f07f4bc3', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Desenvolvimento de instrumento de pesquisa para identificação de modelos de elaboração da estratégia em burocracias profissionais: validação de conteúdo', 2024),
    ('5adada31-6615-434c-9d00-3bcd4a8d644a', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Transparência, comunicação, informação e movimentos sociais: formação política e participação sociopolítica dos portais institucionais', 2024),
    ('9ff0a8ce-4b0e-4785-bc8a-d55fde0c4b4b', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Juventude, política e fake news: metaestudo das produções acadêmicas em periódicos científicos entre os anos 2009 e 2019', 2024),
    ('3e0c58d4-3d69-4a38-81fb-cd472e560dce', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '20452322', 'A spatio-temporal analysis of dengue spread in a Brazilian dry climate region', 2021),
    ('a3806b39-ff4a-485d-81a9-6b382dfdeed8', '8583e3d4-59e0-4361-956e-f0261641a013', '19831358', 'Solução para Mapeamento e Consulta das Competências dos Pesquisadores: uma arquitetura para extração, integração e consultas de informações acadêmicas', 2024),
    ('0fee8d12-9f23-471d-b8d4-c13e8e7b053a', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19830882', 'A espiritualidade/religiosidade na formação do pedagogo/ professor pesquisado (R) implicado: reflexões autoetnográficas', 2024),
    ('99da2969-17db-45d8-8110-f5ea0541c612', '8583e3d4-59e0-4361-956e-f0261641a013', '25253409', 'Systemic arterial hypertension: treatment with Integrative and Complementary Health Practices', 2020),
    ('6b138eb6-ac28-4dbc-9227-82f610a09505', '8583e3d4-59e0-4361-956e-f0261641a013', '16762592', 'Inteligência Artificial e Virtualização em Ambientes Virtuais de Ensino e Aprendizagem: Desafios e Perspectivas Tecnológicas', 2021),
    ('511ef53d-3531-40b7-b59a-6d7e2ee12472', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Systemic arterial hypertension: treatment with Integrative and Complementary Health Practices', 2020),
    ('9106f640-dd8d-4e5a-94b8-0fbcc14f1133', '8583e3d4-59e0-4361-956e-f0261641a013', '22309926', 'A METHOD FOR ONTOLOGY MODELING BASED ON INSTANCES CONCEPTUAL CLASSIFICATION AND FORMALIZATION', 2020),
    ('4aae69fb-7d6a-469d-9de7-785440d9b679', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '2296424X', 'Renewable sources to promote well-being in poor regions of Brazil', 2022),
    ('2a459fe3-d11b-4def-8f2c-6562169e4422', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '14712458', 'Spatio-temporal correlation networks of dengue in the state of Bahia', 2014),
    ('cfb6936d-4c5b-4418-822d-c001d5eee434', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '22309926', 'A METHOD FOR ONTOLOGY MODELING BASED ON INSTANCES CONCEPTUAL CLASSIFICATION AND FORMALIZATION', 2020),
    ('7352dc31-30ae-4795-b4c2-6ce659d895fe', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '01000233', 'BIOSSEGURANÇA EM ONCOLOGIA E O PROFISSIONAL FARMACÊUTICO: ANÁLISE DE PRESCRIÇÃO E MANIPULAÇÃO DE MEDICAMENTOS ANTINEOPLÁSICOS', 2017),
    ('76fc2615-e0e6-4418-86ca-436ba0c45278', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '14131536', 'Indicação de Procedência: potencial do Recôncavo da Bahia no reconhecimento da  produção artesanal de licores de frutas', 2017),
    ('6bfb141a-eb1b-49c1-a7de-899b3f128c2b', '8583e3d4-59e0-4361-956e-f0261641a013', '15411389', 'Difusão e utilização de informações acadêmicas: um modelo de gestão do conhecimento para subsidiar gestores universitários', 2024),
    ('f1d83968-1de9-41b5-8386-1b89a43502cf', '8583e3d4-59e0-4361-956e-f0261641a013', '24112933', 'A Proposal for the Integration of the Energy Matrix from a Graph Theory Perspective', 2022),
    ('50ac47aa-59e5-4ae4-bbca-bc0f6fe5838c', '8583e3d4-59e0-4361-956e-f0261641a013', '24112933', 'Architectural design of classroom to stimulate learning in Higher Education', 2022),
    ('3ad682f1-2329-4eb5-8e84-e6fc61353a95', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '24112933', 'A Proposal for the Integration of the Energy Matrix from a Graph Theory Perspective', 2022),
    ('f547e440-d12f-4f90-b498-a7b5bda423d9', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '24112933', 'Architectural design of classroom to stimulate learning in Higher Education', 2022),
    ('bbcaa38f-b670-4b24-8a84-79d20c6d16a5', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21757275', 'Centroid model applied for energy scenarios in regions with limited resources', 2022),
    ('81456a04-c77a-4ff0-94a1-071d5adae9f7', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '22309926', 'Practices with educational robotics in professional and technological education', 2017),
    ('436073e0-1132-45a4-a72f-9085d59dbaf2', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '24112933', 'Media Bios and Artificial Intelligence: the dark side of Fake News', 2022),
    ('4e2f0719-da89-4af0-83e0-511bc261697d', '8583e3d4-59e0-4361-956e-f0261641a013', '15487709', 'Correlation between Transport and Occurrence of Dengue Cases in Bahia', 2014),
    ('d7f41e72-6fbe-4cc8-a9e7-91b66c1b5059', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '15487709', 'Correlation Between Transport and Occurrence of  Dengue Cases in Bahia', 2014),
    ('9dce5869-9ac9-4ec9-b4b5-1e3d0c44522c', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00489697', 'Paradox between adequate sanitation and rainfall in dengue fever cases', 2023),
    ('07526ccf-189a-481d-8604-174b973b9929', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Estudo da aplicação de algoritmos de machine learning na manutenção preditiva de motores elétricos', 2023),
    ('f4a68d4c-8bed-409f-96ea-15cd49861cc2', '8583e3d4-59e0-4361-956e-f0261641a013', '24112933', 'An evaluation model for accessibility conditions of salvador bus stops', 2022),
    ('9611c4dd-62c4-4b87-9486-660ce1a8ff01', '8583e3d4-59e0-4361-956e-f0261641a013', '17554365', 'Synchronized spread of COVID-19 in the cities of Bahia, Brazil', 2022),
    ('8e505026-73a2-4aa7-b797-18f545d163bd', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Um olhar teórico-prático da difusão da inovação e Propriedade Intelectual', 2020),
    ('9b3c8d9f-2f2c-4e77-9543-49e6b4d7220e', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '17554365', 'Synchronized spread of COVID-19 in the cities of Bahia, Brazil', 2022),
    ('05f71a5f-064e-49c9-9029-8920eecb1a1f', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Juventudes, formação política e fake news: vida ou morte da participação sociopolítica?', 2020),
    ('23d496fb-4739-4cea-90c3-53db02bcd888', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19830882', 'Percepções juvenis sobre as fake news em seus processos de formação e participação políticas', 2024),
    ('09c4fb75-1038-4f8f-9665-88f2ce4c0e4e', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '20711050', 'Induction of a Consumption Pattern for Ethanol and Gasoline in Brazil', 2022),
    ('9000963a-9ce5-4dd1-b723-1e91d258ba5b', '8583e3d4-59e0-4361-956e-f0261641a013', '23170026', 'Programa de Ideias Inovadoras do IFBA: proposição de melhorias baseada em critérios de avaliação', 2021),
    ('783e005f-506e-45f7-ba90-532729fc9584', '8583e3d4-59e0-4361-956e-f0261641a013', '25253409', 'Inteligência artificial em ambientes virtuais de ensino e aprendizagem: Uma proposta de modelo', 2021),
    ('a499d81e-3217-4f64-96ff-39e7c09f1d3b', '8583e3d4-59e0-4361-956e-f0261641a013', '00313203', 'A mobile, lightweight, poll-based food identification system', 2014),
    ('f83b2e07-6eb8-4dc1-b8aa-246d0d7a35a3', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Inteligência artificial em ambientes virtuais de ensino e aprendizagem: Uma proposta de modelo', 2021),
    ('38a3b0c9-5010-4e7b-a4d6-255f2190c49b', '8583e3d4-59e0-4361-956e-f0261641a013', '23166517', 'SAÚDE PÚBLICA: PROSPECÇÃO TECNOLÓGICA DOS REGISTROS DE SOFTWARES PARA O COMBATE A DENGUE', 2022),
    ('9442df72-f3f6-42e0-ade2-30f951752aca', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '23166517', 'SAÚDE PÚBLICA: PROSPECÇÃO TECNOLÓGICA DOS REGISTROS DE SOFTWARES PARA O COMBATE A DENGUE', 2022),
    ('dff7068c-391b-4555-9ff2-32afbeb41500', '8583e3d4-59e0-4361-956e-f0261641a013', '19832192', 'A INOVAÇÃO NO PROCESSO JUDICIAL ELETRÔNICO DA   BAHIA PARA ADMINISTRAÇÃO DA JUSTIÇA BRASILEIRA', 2015),
    ('3affdfd6-baa3-4761-910b-cb09943618d3', '8583e3d4-59e0-4361-956e-f0261641a013', '03029743', 'A Framework for Context-Aware Systems in Mobile Devices', 2012),
    ('d932265b-ac53-4345-9cd4-671448cca8b9', '8583e3d4-59e0-4361-956e-f0261641a013', '18093957', 'ANÁLISE DA RELAÇÃO DA CULTURA MAKER, FABLABS E ROBÓTICA EDUCACIONAL NA EDUCAÇÃO', 2019),
    ('ebfa3c01-4669-461b-b39c-7d3e2ec17004', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '01291831', 'Self-affinity in the dengue fever time series', 2016),
    ('0c7070a0-3031-4cca-a180-748f7c76d9ed', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '18093957', 'ANÁLISE DA RELAÇÃO DA CULTURA MAKER, FABLABS E ROBÓTICA EDUCACIONAL NA EDUCAÇÃO', 2019),
    ('a82d56f9-7869-482c-b369-ed0e21e8132f', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253514', 'Os jovens podem participar? Considerações acerca da participação e formação políticas juvenis', 2022),
    ('c3373547-743e-46a5-9455-171cc99aec50', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Persistências e rupturas no estudo do Coronavírus após a epidemia da COVID-19', 2023),
    ('8688f9fd-6502-408d-891c-c3c5650d528d', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '09277757', 'Preparation of hybrid nanocomposite particles for medical practices', 2021),
    ('cd307732-426e-4fb0-a286-a7ce0c8661b8', '8583e3d4-59e0-4361-956e-f0261641a013', '22360972', 'GERENCIAMENTO DE PROJETO OTIMISTA (GPO): UM MÉTODO QUE INTEGRA PERT/CPM À CCPM', 2011),
    ('05f7291f-fb76-46b7-9d1c-a4d5bca17b68', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19832192', 'A Inovação no Processo Judicial Eletrônico para Administração da Justiça Brasileira', 2015),
    ('3abae5eb-a96c-4d8a-a264-1481d8833744', '8583e3d4-59e0-4361-956e-f0261641a013', '18093957', 'ROBÓTICA EDUCACIONAL: CONSTRUÇÃO DE UMA DINÂMICA A PARTIR DO ROBÔ ARDU', 2020),
    ('17202ea2-5fda-4ea3-bb4c-b9e7cae6ad22', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25258761', 'ROBÔS CIRÚRGICOS: PROSPECÇÃO DE PATENTES RELACIONADAS A APLICAÇÕES HUMANAS', 2020),
    ('97b8f410-31a2-4d5d-a936-9651a083eb80', '8583e3d4-59e0-4361-956e-f0261641a013', '19805551', 'Estrutura Organizacional Alernativa Para Desenvolvimento de Software, em Fábrica de Software', 2007),
    ('96ad840b-c6ce-44a8-a1dc-9e6b9be483bd', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '00489697', 'Nonlocal dispersal of dengue in the state of Bahia', 2018),
    ('b457e6f4-9550-4c64-ad60-bfadfcd0ca2b', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'Implicações da desinformação e da infodemia no contexto da pandemia da Covid-19', 2021),
    ('2e0b8219-c712-43a1-854e-e9fcf787da4c', '8583e3d4-59e0-4361-956e-f0261641a013', '1981223X', 'APLICAÇÃO DE CONCEITOS E CRITÉRIOS DE DESEMPENHO PARA UMA SALA DE AULA INOVADORA', 2023),
    ('cc9c868e-96fb-4ebf-81d6-b0f9846e98b7', '8583e3d4-59e0-4361-956e-f0261641a013', '19818920', 'Inovação e empreendedorismo como caminhos para novos modelos de ensino/aprendizagem', 2017),
    ('9ccb05c2-2962-482a-b389-77bbd6ca0166', '8583e3d4-59e0-4361-956e-f0261641a013', '18093957', 'ASPECTOS COGNITIVOS DE APRENDIZAGEM MOTIVADOS POR JOGOS EDUCATIVOS DIGITAIS', 2017),
    ('29730d33-3010-42f1-8e5c-0fe7c0f6ad76', '8583e3d4-59e0-4361-956e-f0261641a013', '21789010', 'Desenvolvimento sustentável: uma proposta para descarbonização de frotas de veículos', 2023),
    ('94a674f4-cf25-4b9b-8803-6cf50ce32f79', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19818920', 'Inovação e empreendedorismo como caminhos para novos modelos de ensino/aprendizagem', 2017),
    ('ae4a73f3-e9bc-4e1d-9f2c-83220a18a1ce', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '23496495', 'Business Incubators and Sustainability: A Literature Review', 2022),
    ('10d106f4-c0dd-4ad6-83f7-78f1091d2e08', '8583e3d4-59e0-4361-956e-f0261641a013', '25253409', 'A teoria fundamentada em dados aplicada ao campo da educação superior', 2021),
    ('c989bf37-48a8-455f-8f39-a343e43889e4', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '21789010', 'Desenvolvimento sustentável: uma proposta para descarbonização de frotas de veículos', 2023),
    ('4786dcae-1dfa-49a6-a042-d8cbd3178825', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '25253409', 'A teoria fundamentada em dados aplicada ao campo da educação superior', 2021),
    ('35124571-7078-46a9-88b2-08a6c8b6df4a', '8583e3d4-59e0-4361-956e-f0261641a013', '15411389', 'Mapeamento científico e tecnológico sobre Impressão 3D', 2023),
    ('2cfd3e93-4c2f-4fc1-b0e3-6e051aa0988b', '8583e3d4-59e0-4361-956e-f0261641a013', '19818920', 'Redes complexas de homônimos para análise semântica textual', 2017),
    ('fda081f2-bbaf-4eb3-8a99-c473126fc0c1', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '15411389', 'Mapeamento científico e tecnológico sobre Impressão 3D', 2023),
    ('25c6251e-0d44-4dc3-b32d-d177519819ab', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19818920', 'Redes complexas de homônimos para análise semântica textual', 2017),
    ('736a1a04-5002-4b96-8562-9a8cc477425a', '8583e3d4-59e0-4361-956e-f0261641a013', '22372903', 'Um Sistema de apoio a Gerência de Requisitos Aderente ao MPS.BR', 2018),
    ('ab56430c-f94e-4845-b630-36aeadd478a6', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '03784371', 'Self-organized critical phenomenon as a', 2014),
    ('e8395003-4b3d-4707-bf29-c37a57c9e568', '8583e3d4-59e0-4361-956e-f0261641a013', '19887833', 'Diretrizes para o planejamento de um ambiente de aprendizagem neuroarqeducativo', 2023),
    ('699877e0-b596-4c07-a061-4df071ba217b', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '19887833', 'Diretrizes para o planejamento de um ambiente de aprendizagem neuroarqeducativo', 2023),
    ('634ed14b-bcd2-4979-8baa-13715439eb89', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '18093957', 'Indicações Geográficas como Estratégia para o Desenvolvimento Regional', 2017),
    ('e31cfef0-7fd4-4e0b-9dd6-882e19f61d7d', '1c902c6a-91ea-4c7c-a2a3-e0c6931b41c9', '15411389', 'Aprendizagem organizacional: sinergia interdisciplinar nos saberes', 2023);
"""

# Execute cada comando separadamente
try:
    with banco.cursor() as cursor:
        print("Inserindo pesquisador...")
        cursor.execute(sql_inserir_pesquisador)
        
        print("Inserindo produção...")
        cursor.execute(sql_inserir_producao)
        
        banco.commit()  # Confirma a transação (ambos os inserts)
        print("Dados inseridos com sucesso!")
except Exception as e:
    banco.rollback()  # Reverte a transação em caso de erro
    print(f"Erro ao inserir dados: {e}")
finally:
    banco.close()
    print("Conexão com o banco de dados encerrada.")
