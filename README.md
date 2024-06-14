# HousePrices-RNK

<h1 align="center"> House Prices - RNK </h1>
<h4 align="center">Projeto de Análise de Preços de Casas</h4>

Este projeto foi desenvolvido como parte de um trabalho acadêmico com o objetivo de aplicar técnicas de regressão linear para analisar e prever os preços de casas. Utilizando um conjunto de dados contendo diversas características das casas, foi possível construir um modelo de regressão linear que ajuda a entender os fatores que influenciam os preços.<br>

<h2>Conjunto de Dados</h2>
O conjunto de dados utilizado para este projeto contém informações sobre várias características das casas e seus preços. As colunas do conjunto de dados são:<br>

Taxa_Criminalidade (CRIM): Taxa de criminalidade per capita por cidade.<br>
Zona_Residencial (ZN): Proporção de terrenos residenciais com mais de 25.000 pés quadrados.<br>
Proporcao_Comercial (INDUS): Proporção de acres comerciais não comerciais por cidade.<br>
Proximidade_Rio (CHAS): Variável fictícia que indica se a área faz fronteira com o rio Charles (1 se limita; 0 caso contrário).<br>
Concentracao_NOX (NOX): Concentração de óxidos nítricos (partes por 10 milhões).<br>
Media_Quartos (RM): Número médio de quartos por habitação.<br>
Proporcao_Unidades_Antigas (AGE): Proporção de unidades ocupadas por proprietários construídas antes de 1940.<br>
Distancia_Centros (DIS): Distâncias ponderadas até cinco centros de emprego em Boston.<br>
Acessibilidade_Rodovias (RAD): Índice de acessibilidade às rodovias radiais.<br>
Taxa_Imposto (TAX): Taxa de imposto sobre propriedade de valor integral por $10.000.<br>
Proporcao_Aluno_Professor (PTRATIO): Proporção aluno-professor por cidade.<br>
Proporcao_Negros (B): 1000(Bk - 0.63)^2, onde Bk é a proporção de negros por cidade.<br>
Proporcao_Status_Baixo (LSTAT): Porcentagem da população com status socioeconômico baixo.<br>
Valor_Medio (MEDV): Valor médio das casas ocupadas pelos proprietários em $1000s.<br>

<h2>Metodologia</h2>
A análise foi conduzida seguindo estas etapas:<br>

<strong>Exploração e Preparação dos Dados:</strong> Análise inicial dos dados, tratamento de valores ausentes e exploração de características importantes.<br>
<strong>Desenvolvimento do Modelo de Regressão Linear:</strong> Divisão dos dados em conjuntos de treinamento e teste, treinamento do modelo e avaliação de seu desempenho.<br>
<strong>Avaliação do Modelo:</strong> Utilização de métricas como Erro Quadrático Médio (MSE) e Coeficiente de Determinação (R²) para avaliar o modelo.<br>
<strong>Interpretação dos Resultados:</strong> Análise dos coeficientes do modelo e identificação das variáveis mais influentes.<br>

<h2>Resultados </h2>
O modelo de regressão linear apresentou um Erro Quadrático Médio (MSE) de 25.42 e um Coeficiente de Determinação (R²) de 0.67. Os coeficientes do modelo revelaram que variáveis como Media_Quartos e Proximidade_Rio têm um impacto significativo nos preços das casas.<br>

<h2>Conclusão</h2>
O modelo de regressão linear desenvolvido permite prever os preços das casas com uma precisão razoável, destacando a importância de características como o número médio de quartos e a proximidade ao rio Charles. Este modelo pode ser útil para agentes imobiliários, compradores e investidores que desejam entender os fatores que influenciam os preços das casas.<br>