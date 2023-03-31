# Projeto de Previsão de Vendas: Drogarias Rossmann

O objetivo desse projeto é fornecer para o CFO e Gerentes das Lojas ,uma previsão de faturamento no final de 6 semanas, para que o CFO possa planejar e alocar valores para futuras reformas das lojas.

Para alcance dessa proposta será utilizada técnicas de exploração de dados, focando nas vendas das lojas contidas em uma base de dados fornecida pela Rossmann.

**## 1. Drogarias ROSSMANN**

### 1.1 Contexto do negócio:

A Rossmann é uma cadeia de formácias fundada em 1972 por Dirk Rossmann. É considerada uma das maiores redes de farmácias na Europa com cerca de 56.200 colaboradores e mais de 4000 lojas. Em 2019 Rossmann faturou mais de 10 bilhões, considerando países como: Alemanha, Polonia, Hungria, Republica Tcheca, Turkia, Albania, Kosovo e Espanha. Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Rossmann_(company)

O objetivo do case é fornecer os valores de vendas das farmácias para que assim o CFO e Gerentes, possam alocar mais precisamente e corretamente os valores para realizações de eventuais melhorias e reformas das lojas. Desse maneira o CFO solicitou para equipe de DS da empresa, uma previsão das vendas das lojas no final de 6 semanas.

A principal estratégia para resolução da solicitação do CFO, será utilizadas técnicas de análises exploratórias com base em um arquivo disponibilizado pelo CFO das vendas das lojas dos anos de 2013, 2014 e 2015.

### 1.2 Questão do negócio:

Considerações:

a) O time do negócio não consegue fornecer essas informações ao CFO;

b) O portfólio é muito grande, o que tomaria muito tempo para fazer o trabalho manualmente.

Em resumo, o projeto visa responder às seguintes perguntas de negócio:

- Qual é o valor total de produtos vendidos para cada loja no final de 6 semanas ?

- Com base no projeto, qual é o melhor e pior cenário de vendas em valores ?

### 1.3 Sobre os dados:

Os dados foram extraídos do link abaixo, onde constam todas as vendas das farmácias do período de 2013 a 2015.

[https://www.kaggle.com/harlfoxem/housesalesprediction](https://www.kaggle.com/c/rossmann-store-sales)

Abaixo uma tabela com os atributos e descrição do conjunto de dados:

|***Atributo*** | ***Descrição*** |

| -------- | --------- |

|**store** | Identificação de cada loja |

|**day_of_week** | dia da semana |

|**date** | data da realização da venda |

|**sales** | quantidade de vendas de uma determinada data |

|**promo** | aponta se uma farmácia esta realizando promoção ou não |

|**state_holiday** | Indica feriados nacionasi. Geralmente todas as lojas entram em recesso em feriados nacionais, a seguinte legenda pode ser interpretada para essa coluna de informações: a = public holiday, b = easter holiday, c = christmas e 0 = None|

|**school_holiday** | indica se a loja foi afetada pelo fechamento de escolas públicas devido a algum feriado |

|**store_type** | Diferencia as lojas em 4 modelos diferentes: a, b, c e d |

|**assortment** | Indica o tipo de sortimentos que a loja possuí, a = basic, b = extra e c = extended |

|**competition_distance** | Distância em metros, da loja concorrente mais próxima |

|**competition_open_since_month** | Indica o mês que o competidor mais próximo foi aberto |

|**competition_open_since_year** | Indica o ano que o competidor mais próximo foi aberto |

|**promo2** | Indica se a loja efetuou em algum momento promoções consecutivas, 0 = store is no participating, 1 = store is participating  |

|**promo2_since_week** | Descreve a semana que a loja aderiu a promo2 |

|**promo2_since_year** | Descreve o ano que a loja aderiu a promo2 |

|**is_promo** | Descreve se a loja esta ou não em promoção, 0 = não esta em promoção, 1 = esta em promoção |

|**year** | Ano da venda |

|**month** | Mês da venda |

|**day** | Dia da venda |

|**week_of_year**| Semana do ano |

|**year_week**| Concatenação da semana do ano e o ano |

|**competition_since**| Concatenação das colunas: competition_open_since_month e competition_since_year  |

|**competition_time_month**| Quantidade de meses desde que a competição mais próxima começou |

|**promo_since**| Concatenação das colunas promo2_since_year e promo2_since_week |

|**promo_time_week**| Descreve a quantidade em semanas que uma promoção esta ocorrendo |

### 1.5 Premissas do negócio:

Dentro do processo de entendimento de negócio, exploração dos dados e decisão para fornecer os insights finais, foram adotadas as seguintes premissas:

- Os dados disponíveis são do período de 01/01/2013 a 31/07/2015;
- Lojas sem informação de distância do competidor mais próximo, foram consideradas com distância de 200.000 metros;

**## 2. Planejamento para solução do problema:**

1. Limpeza de dados
2. Feature Engineering
3. Filtragem de variáveis
4. Exploração de dados
5. Preparação dos dados
6. Seleção de variáveis
7. Aplicação de modelos de ML
8. Fine-Tuning Hyperparameter
9. Avaliação dos algoritmos

### 2.1  Insights e Hipóteses encontradas:

#### H8. Lojas deveriam vender mais ao longo dos anos.

- *FALSA** Apesar de não termos o ano de 2015 fechado, vemos uma tendência das lojas venderem menos ao longo dos anos

#### H9. Lojas deveriam vender mais no segundo semestre dos anos.

- *FALSA** Lojas vendem menos ao longo do segundo semestre dos anos

#### H10. Lojas deveriam vender mais depois do dia 10 de cada mês.

- *VERDADEIRA** Lojas vendem mais depois do dia 10 de cada mês

#### H11. Lojas deveriam vender menos aos finais de semana.

- *VERDADEIRA** Lojas vendem menos no finais de semana

#### H12. Lojas deveriam vender menos durante os feriados escolares.

- *VERDADEIRA** Lojas vendem menos durante os feriados escolares, exceto os meses de Julho e Agosto.

### 2.2  Modelos de Machine Learning Utilizados e métricas de performance:

Para esse projeto foram utilizados os seguintes algoritmos de Machine Learning:

- Linear Regression
- Linear Regression Regularized com Lasso
- Random Forest Regressor
- XGBoost Regressor

Na avaliação de performance, o XGBoost não desempenhou a melhor performance de todas, porém devido a questão de aprendizado, seguimos com ele, pois no entendimento para esse projeto tentei uma abordagem diferente, já que a utilização dos outros algoritmos possuí vasta aplicação e possuí amplo material de consulta, diferente do XGBoost.

**### 3. Resultado da análise para o Negócio:**

Apos todo o processo descrito no notebook, para preparação e treinamento do modelo desenvolvido, chegamos em uma predição de receita bruta no final de 6 semanas de $ 286.45 Milhões de dólares, também consideramos o pior e melhor cenários, ao qual utilizamos para o calculo o Mean Absolute Error (MAE), o melhor e pior cenários são $ 287.29 Milhões e $ 285.57 Milhões, respectivamente.

Apesar de chegarmos aos valores brutos, entendemos que uma consulta por loja seria mais interessenta para detalhamento das receitas. Utilizando dessa premissa, deixamos também como parte do projeto a opção do CFO analisar a previsão de cada loja serapardamente além de disponibilizar um acesso a um bot do telegram, a qual o mesmo, ou qualquer pessoa interessada, bastará possuir o app Telegram em seu telefone, o endereço do bot do Telegram e um acesso a internet. Uma imagem da previsão de cada loja, e o link do bot telefram encontram-se abaixo:

Abaixo conseguimos ver o resultando em uma time line das previsões e uma comparação quanto ao baseline.

Também para colaborar com a análise do CFO, expomos um gráfico abaixo que demonstra se as previsões subestimaram ou superestimaram os valores preditos.

## 4. Conclusão e pontos de melhorias:

O projeto tem como princípio a geração de insights para o negócio, assim como responder algumas perguntas feitas pela empresa. O objetivo foi concluído, e foi possível extrair informações relevantes e com potencial forma de gerar direcionamento para as próximas operações da House Rocket.

As visualizações fornecidas irão permitir com que a empresa possa avaliar as regiões mais lucrativas, os atributos que levam o imóvel a se tornar mais viável para as operações de compra e venda, e ainda visualizar o lucro máximo que poderá ser alcançado de acordo com as opções de negócio.

Pontos de Melhorias:

Melhor a técnica de preenchimento de ************Missing Values,************ por exemplo, competition_distance, poderá ser métodos como preenchimento considerando a média da distância das lojas perto dessa loja da Rossmann, assim também como poderá ser utilizada mediana.

Coletar mais dados, por exemplo o ano de 2015 não esta completo como informado no tópico que trata das premissas do negócio.









00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# Projeto de Previsão de Vendas: Drogarias Rossmann

O objetivo desse projeto é fornecer para o CFO e Gerentes das Lojas ,uma previsão de faturamento no final de 6 semanas, para que o CFO possa planejar e alocar valores para futuras reformas das lojas. 

Para visualização dos resultados, será disponibilizada na Web, utilizando a ferramenta Streamlit, a possibilidade ao CEO e a equipe de corretores acesso a tais informações com disponibilidade de 24/7, bastando ter um dispositivo que tenha conexão com a internet.

O resultado geral obtido foi uma seleção de __10.604 imóveis__ (podendo ser variável de acordo com as condições/localizações) que corresponde a quase 50% dos imóveis do portfólio disponibilizado.

| __Número de imóveis__ | __Custo total__ | __Receita de vendas__ | __Lucro (profit)__ |
| ----------------- | ----------------- | ----------------- | ----------------- |
| 10.604 | US$ 4.141.568.273,00 | US$ 4.634.592.801,50 | US$ 493.024.528,50 |

Link para visualização:  [<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>](https://apphr-def.herokuapp.com)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 1. A House Rocket

### 1.1 Contexto do negócio:

A Rossmann é uma cadeia de formácias fundada em 1972 por Dirk Rossmann. É considerada uma das maiores redes de farmácias na Europa com cerca de 56.200 colaboradores e mais de 4000 lojas. Em 2019 Rossmann faturou mais de 10 bilhões, considerando países como: Alemanha, Polonia, Hungria, Republica Tcheca, Turkia, Albania, Kosovo e Espanha. Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Rossmann_(company)

A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando a tecnologia para analisar suas melhores oportunidades.

O objetivo do case é fornecer insights para a empresa encontrar as melhores oportunidades de negócio no mercado de imóveis. O CEO da House Rocket gostaria de ***maximizar*** a receita da empresa encontrando ***boas oportunidades*** de negócio.

Sua principal estratégia é ***comprar boas casas*** em ótimas localizações com preços baixos e depois revendê-las posteriormente a preços mais altos. Quanto maior a diferença entre a compra e a venda, maior o lucro da empresa.

Entretanto, as casas possuem muitos atributos fato que as tornam mais ou menos atrativas aos compradores e vendedores, e a localização e conforme análise, o período do ano também podem influenciam os preços.

### 1.2 Questão do negócio:

Considerações:

a) O time do negócio não consegue tomar boas decisões de compra sem analisar os dados,e;

b) O portfólio é muito grande, o que tomaria muito tempo para fazer o trabalho manualmente.

O objetivo desse projeto é fornecer uma seleção de imóveis, de acordo com  as melhores condições, para que a empresa possa realizar suas operações de compra e venda. 
A proposta é demonstrar através de visualizações, quais as melhores oportunidades e qual resultado (lucro) máximo que pode ser alcançado.

Em resumo, o projeto visa responder às seguintes perguntas de negócio:

- Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?
 - Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?

### 1.3 Sobre os dados:

Os dados foram extraídos do link abaixo, onde constam todos os imóveis em portfólio e disponíveis para a empresa.

https://www.kaggle.com/harlfoxem/housesalesprediction

Abaixo uma tabela com os atributos e descrição do conjunto de dados:

|***Atributo*** | ***Descrição*** |
| -------- | --------- |
|**id** | Identificação de cada imóvel | 
|**date** | Data de quando a venda foi realizada |
|**price** | Preço que a casa foi vendida pelo proprietário |
|**bedrooms** | Número de quartos |
|**bathrooms** | Número de banheiros (0.5 = banheiro em um quarto, mas sem chuveiro) |
|**sqft_living** | Medida em pés quadrados dos espaços interiores dos apartamentos |
|**sqft_lot** | Medida em pés quadrados  |
|**floors** | Número de andares | 
|**waterfront** | Indica se o imóvel possui vista para água (0 = não e 1 = sim) | 
|**view** | Um índice de 0 a 4 que indica a qualidade da vista da propriedade. Varia de 0 a 4, onde: 0 = baixa 4 = alta | 
|**condition** | Um índice de 1 a 5 que indica a condição da casa. Varia de 1 a 5, onde:1 = baixo 5 = alta | 
|**grade** | Um índice de 1 a 13 que indica a construção e o design do edifício. Varia de 1 a 13, onde: 13 = baixo, 7 = médio e 1113 = alta | 
|**sqft_basement** | Medida em pés quadrados  | 
|**yr_built** | Ano de construção | 
|**yr_renovated** | Ano de reforma | 
|**zipcode** | CEP da casa | 
|**lat** | Latitude | 
|**long** | Longitude | 
|**sqft_livining15** | Medida em pés quadrado do espaço interno de habitação para os 15 vizinhos mais próximo | 
|**sqft_lot15**| Medida (em pés quadrado) dos lotes de terra dos 15 vizinhos mais próximo | 

*Além do dataset acima citado, foi utilizado um arquivo geojson para a criação de mapas de densidade. A API foi extraída do site ArcGIS Hub, https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson *

### 1.5 Premissas do negócio:

Dentro do processo de entendimento de negócio, exploração dos dados e decisão para fornecer os insights finais, foram adotadas as seguintes premissas:

- A coluna *price* significa o preço que a casa foi ou será comprada pela empresa House Rocket;
- Os valores iguais a zero em *yr_renovated* são casas que nunca foram reformadas;
- As informações do __preço mediano da região __ e a __condição__  foram características decisivas recomendação de compra ou não comprar dos imóveis
- Para as condições dos imóveis, foi determinada a seguinte classificação: __1 = muito ruim, 2 = ruim, 3 = regular, 4 = bom e 5 = muito bom__
- Como a sazonalidade também influencia diretamente a demanda por investimento em imóveis, a estação do ano foi a característica decisiva para a época da venda do imóvel. Foram assumidos valores medianos de acordo com sua região e sazonalidade. As épocas do ano, foram determinadas de acordo com as data de estação do ano da cidade Kings County USA, cidade ao qual pertence o conjunto de dados.
-Uma das premissas mais relevantes, a recomendação do preço de venda, foi aplicada o seguinte cálculo, quando o preço de compra for menor do que a mediana da região + mediana da sazonalidade, foi aplicado um percentual de 30% para venda do imóvel, sendo que este valor não poderá passar do valor da mediana da região  + mediana sazonalidade, para casos como esse, serão considerados os valores da mediana da região + mediana da sazonalidade. Para preços acima da mediana da região + mediana da sazonalidade, foi aplicado o percentual de 10% em relação ao preço de compra.
-Imóvel com informação de 33 quartos, foi interpretado como erro de digitação e foi assumido o valor de 3 quartos, já que após análise de imóveis parecidos, foi concluido que quantidade de 3 seria plausível.
-Não foi encontrado motivos para deixar no conjunto de dados, imóveis com quantidade de banheiros iguais a 0, por isso todos os registros desse tipo (total 10) foram retirados do conjunto de dados.

## 2. Planejamento da solução:

### 2.1  Exploração de dados:

A primeira etapa do projeto foi realizar a coleta, tratamento e exploração dos dados. Nessa etapa foi possível realizar identificar necessidades de limpeza e transformação de dados, realizar uma análise das estatísticas descritivas dos conjuntos de dados, e ainda realizar a criação de novas *features* para facilitar e proporcionar as visualizações e criações dos insights que serão apresentados. A motivação da criação das novas features serão explanadas em outro momento.

- Estatísticas descritivas:

| **attributes** | **maximum**|  **minimum** |  **mean** |  **median** |  **std** | 
| -------- | --------- |---------| -------- | --------- |--------- |
| price | 7700000.00 | 75000.00 | 541645.37 | 450000.00 | 367314.32 |
| bedrooms | 11.00 | 0.00 | 3.37 | 3.00 | 0.91 |
| bathrooms | 8.00 | 0.00 | 2.12 | 2.25 | 0.77 |
| sqft_living | 13540.00 | 290.00 | 2082.73 | 1920.00 | 919.14 |
| sqft_lot | 1651359.00 | 520.00 | 15136.06 | 7614.00 | 41538.57 |
| floors | 3.50 | 1.00 | 1.50 | 1.50 | 0.54 | 
| view | 4.00 | 0.00 | 0.24 | 0.00 | 0.77 |
| condition | 5.00 | 1.00 | 3.41 | 3.00 | 0.65 |
| grade | 13.00 | 1.00 | 7.66| 7.00| 1.17 |
| sqft_above| 9410.00| 290.00| 1791.00| 1560.00| 829.01 |
| sqft_basement| 4820.00| 0.00| 291.73| 0.00| 442.78 |
| yr_built| 2015.00| 1900.00| 1971.10| 1975.00| 29.38 |
| yr_renovated| 2015.00| 0.00| 84.73| 0.00| 402.43 |
| sqft_living15| 6210.00| 399.00| 1988.35| 1840.00| 685.68 |
| sqft_lot15| 871200.00| 651.00| 12786.34| 7620.00| 27375.41 |


| **attributes** | **mean**|  **minimum** |  **max** |  **std** |  **median** | 
| -------- | --------- |---------| -------- | --------- |--------- |
|price	|541693.6|	|78000|	|7700000|	|367296.43|	|450000|
|bedrooms	|3.37|	|0|	|11|	|0.9|	|3|
|bathrooms	|2.12|	|0.5|	|8|	|0.77|	|2.25|
|sqft_living	|2082.91|	|370|	|13540|	|918.85|	|1920|
|sqft_lot	|15135.1|	|520|	|1651359|	|41547.34|	|7613.5|
|floors	|1.5|	|1|	|3.5|	|0.54|	|1.5|
|waterfront	|0.01|	|0|	|1|	|0.09|	|0|
|view	|0.24|	|0|	|4|	|0.77|	|0|
|condition	|3.41|	|1|	|5|	|0.65|	|3|
|grade	|7.66|	|3|	|13|	|1.17|	|7|
|sqft_above	|1791.03|	|370|	|9410|	|828.7|	|1560|
|sqft_basement	|291.88|	|0|	|4820|	|442.84|	|0|
|yr_built	|1971.1|	|1900|	|2015|	|29.39|	|1975|
|yr_renovated	|84.77|	|0|	|2015|	|402.52|	|0|
|zipcode	|98077.87|	|98001|	|98199|	|53.47|	|98065|
|lat	|47.56|	|47.16|	|47.78|	|0.14|	|47.57|
|long	|-122.21|	|-122.52|	|-121.31|	|0.14|	|-122.23|
|sqft_living15	|1988.36|	|399|	|6210|	|685.47|	|1840|
|sqft_lot15	|12783.86|	|651|	|871200|	|27380.23|	|7620|
|month	|6.56|	|1|	|12|	|3.12|	|6|


- Novas features:
-*standard*: Padrão das casas pelo valor de vendar; Imóveis com preço acima de 540 k  foram considerados de alto padrão(high_standard), imóveis abaixo de 540 k  foram consideras de baixo padrão (low_standard)
-*dormitory_type*: Tipo do imóvel (house, studio, apartment); Imóveis com o tipo de 'bedrooms' iguais a 1 foram considerados como 'studio', 'bedrooms' iguais a 2 foram considerados do tipo apartamento (apartment) e dormitórios iguais a 3 foram considerados como 'house'.
-*condition_type*: Condição do imóvel (very bad, bad, regular, good, very good); Imóveis com 'condition' iguais a 1 foram considerados imóveis muito ruins (very bad), imóveis com valores iguais a 2 foram considerados imóveis ruins (bad), imóveis com valores iguais a 3, foram considerados imóveis de qualidade mediada (regular), imóveis iguais a 4 foram considerados de boa qualidade (good) e valores iguais a 5 foram considerados imóveis muito bons (very good).
-  *construction:* ano de construção maior ou menor que 1955;
- *basement:_status* imóvel com ou sem porão
- *month:* mês que o imóvel ficou disponível para venda
- *season:* estação do ano que o imóvel ficou disponível para venda; Dos meses de Março (3) a Maio (5), foi considerado estação 'spring', dos meses de Junho (6) a Agosto (8) foi foram considerados 'summer', os meses de Setembro (9) a Novembro (11) foram considerados 'fall' e dos meses de Dezembro (12) a Fevereiro (2) foram considerados 'winter'.
- *waterfront_status:* vista ou não para água; Com referência ao atributo 'waterfront', valores iguais a 0 foram considerados como que 'no', ou seja, não possuem vista para a água, valores iguais a 1 foram considerados  como 'yes', ou seja, possuem vista para água.
- *renovated_status:* imóvel foi ou não reformado;  Valores na coluna 'yr_renovated' iguais a zero foram consideados como imóveis que não foram renovados, imóveis que foram encontrados algum registro foram considerados como imóveis renovados.
-*year*: Ano da data de venda/disponibilidade para venda do imóvel
-*year_month*: Mês e ano de venda/disponibilidade do imóvel
-*recomendation*: Coluna de recomendação de compra ou não de um imóvel
-*sell_price*: recomendação do valor que os imóveis deveriam ser comprados
-*profit*:

### 2.2  Seleção dos imóveis:

Todo planejamento dessa solução foi pensando na criação de um aplicativo de visualização, onde a empresa poderá consultar a seleção dos imóveis, seus insights e outras informações inerentes às perguntas de negócio.

Para iniciar a montagem das visualizações, foram realizados os seguintes passos para cada pergunta de negócio:

__a) Quais são os imóveis que a House Rocket deveria comprar e por qual preço ?__
- Agrupado os imóveis por região ( *zipcode* );
- Dentro de cada região, foi encontrada a mediana do preço do imóvel;
- Essa mediana foi retornada em cada linha do dataset para ser possível a comparação;
- Foi assumida a seleção dos imóveis que estão abaixo ou igual ao preço mediano da região e que estejam em boas condições - *condition* com valor iguais a e acima de 3.
- O próximo passo foi a criação de uma feature auxiliar para receber a indicação se o imóvel deve ou não ser comprado. Ou seja, se o imóvel estiver com preço abaixo da mediana da região e, estiver em condição “regular”(3) , “good” (4) ou “very good” (5), o imóvel é selecionado.

__b) Uma vez a casa comprada, qual o melhor momento para vendê-las e por qual preço ?__
- Agrupar os imóveis selecionados na questão 1 por região ( *zipcode* ) e também por temporada (*season*);
- Dentro de cada região e temporada, foi encontrada a mediana do preço do imóvel;
- Para cálculo do valor de venda, foram assumidas as seguintes condições, as quais foram aplicadas em novas features criadas - ***sell_price e profit:***

   1. Se o preço da compra for maior que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 10%
   2. Se o preço da compra for menor que a mediana da região + sazonalidade. O preço da venda será igual ao preço da compra + 30% valor que não seja maior que a região + sazonalidade, caso o valor seja maior, será considerado o valor da região + sazonalidade

### 3. Portfólio total:

Tendo todo entendimento do negócio, e respondida as perguntas de negócio, foram levantadas algumas hipóteses para serem validadas, com o objetivo de gerar insights para próximas questões de negócio ou mesmo gerar novas estratégias para a House Rocket:

| __Hipótese__ | __Resultado__ | __Tradução para negócio__ |
| ------------ | ------------ | ------------ |
| __H1__ -Imóveis que possuem vista para água, são em média 30% mais caros | Verdadeira | Imóveis com vista para água são em média 212% mais caros. Procurar investir em imóveis sem vista para água, por terem custo de negócio menor |
| __H2__ - Imóveis com data de construção menor que 1955 são em média 50% mais baratos | Falsa | A diferencia média dos valores é de apenas 1%. Investir em imóveis independente da data de construção |
| __H3__ - Imóveis sem porão são em média 50% maiores do que imóveis com porão | Falsa | Casas sem porão são apenas 19% maiores que casa sem porão. Caso seja estretegia da House Rocket, é segerido investimento em imóveis sem porão, pois oferecem maior área de terreno |
| __H4__ - O crescimento do preço dos imóveis entre os anos de 2014 e 2015 é em média de 10%  | Falsa | Não houve considerável crescimento no preço médio entre os anos (cerca de somente 0.22%). Ou seja, o período analisado teve preços médios próximos, sem variações que poderia ser estudadas como anormalidades |
| __H5__ - Imóveis com 3 banheiros tem um crescimento MoM (month of month) de 15% | False | Em média o crescimento MoM das casas com 3 banheiros é de somente 0.18% |
| __H6__ - Imóveis com 2 andares são em média 15% mais caros do que aqueles com somente um andar | Verdadeira | Imóveis com 2 andares são em média 26.58% mais caros do que imóveis com apenas um andar. |
| __H7__ - A maioria dos imóveis tornou-se disponível durante as estações 'summer/spring' | Verdadeira | Cerca de 59% dos imóveis ficaram disponíveis nessa época do ano |
| __H8__ - Imóveis disponíveis durante summer/spring são em média 20% mais caros | False | Imóveis disponíveis entre summer/spring são apenas em média 5% mais caros |
| __H9__ - Imóveis que foram reformado, são em média 40% mais caros | Verdadeira | Em média os imóveis reformados são cerca de 43.28% mais caros |

## 4. Resultados financeiros:

O objetivo desse projeto era fornecer uma lista de imóveis com opções de compra e venda, e consequentemente o __lucro máximo__ que poderá ser obtido se todas as transações ocorrerem. Ou seja, o resultado financeiro apresentado abaixo representa o lucro máximo que pode ser obtido utilizando as recomendações informadas:

| __Número de imóveis__ | __Custo total__ | __Receita de vendas__ | __Lucro (profit)__ |
| ----------------- | ----------------- | ----------------- | ----------------- |
| 10.604 | US$ 4.141.568.273,00 | US$ 4.634.592.801,50 | US$ 493.024.528,50 |

Todavia cabe reforçar, que o lucro pode ser explorado por condições e região dos imóveis, onde as visualizações fornecidas demonstram todo resultado do projeto, assim como o resultado financeiro, de forma customizada para as opções escolhidas.

## 5. Conclusão:

O projeto tem como princípio a geração de insights para o negócio, assim como responder algumas perguntas feitas pela empresa. O objetivo foi concluído, e foi possível extrair informações relevantes e com potencial forma de gerar direcionamento para as próximas operações da House Rocket.

As visualizações fornecidas irão permitir com que a empresa possa avaliar as regiões mais lucrativas, os atributos que levam o imóvel a se tornar mais viável para as operações de compra e venda, e ainda visualizar o lucro máximo que poderá ser alcançado de acordo com as opções de negócio.
