# Previsão de vendas para uma cadeias de farmácias Rossmann

![home](https://www.gsmmaniak.pl/wp-content/uploads/gsmmaniak/2019/03/rossmann-wypuscil-promocje-w-black-friday-ale-mocno-sie-przeliczyl-rozwscieczeni-klienci-skladaja-skargi-zwykle-zlodziejstwo-2389046.jpg) 

Este repositório contém os códigos realizados para realizar a previsão de vendas para as cadeias de farmácias da Rossmann. <br>
Os dados utilizados para esse projeto foram retirados do seguinte entedeço: [Rossmann Sales Prediction](https://www.kaggle.com/c/rossmann-store-sales).

#### Projeto - Previsão de Vendas:
Os principais objetivos desse projeto são:
* Analisar com ténicas de exploração de dados as vendas das lojas contidas em uma base de dados forneceida pela Rossmann.
* Prever as vendas para as próximas 6 semanas para cada loja.

---
## 1. Problema de negócio
Rossmann is a pharmacy chain that operates over 3,000 stores in 7 European countries. The stores are going to be renovated and the CFO needs to know how much can be invested in each one of them. <br>
The Data Scientist was requested to develop a sales prediction model that  forecast the sales for the next 6 weeks for each store. Therefore, the telegram bot must return this sales prediction for the given store.

## 2. Resultado da análise para o Negócio
The model developed predicts a gross income of $286.69 MM in the next 6 weeks for the stores available, where the best and worst case scenarios results on $313.65 MM and $259.73 MM, respectively. These scenarios were calculated based on mean absolute percentage error for each store.
<br>

## 3. Premissas do Negócio
* The data available is only from 2013-01-01 to 2015-07-31.
* Stores without information on distance from competitors are considered without competition nearby.
* Seasons of the year:<br>
   * Spring starts on March 1st<br>
   * Summer starts on June 1st<br>
   * Fall starts on September 1st<br>
   * Winter starts on December 1st<br>
<details><summary>Dicionário original dos dados:</summary><br>

Variable | Definition
------------ | -------------
|store | Identificar único de cada loja|
|days_of_week | weekday, starting 1 as Monday. |
|date | Data que foram realizadas as vendas |
|sales | Quantidade de vendas e/ou produtos realizadas na data especifica |
|customers | Quantidade de clientes que realizaram compras na data especifica |
|open | Informação se a loja esta ou não aberta na data especifica, 1 aberta, 0 fechada |
|promo | Informação se a loja estava participando de alguma promoção ou não, 1 estava participando, 0 não estava participando|
|sate_holiday | whether it was a state holiday (a=public holiday, b=easter holiday, c=christmas) or not (0) |
|store_type | designates the store model as a, b, c or d. |
|assortment | indicates the store assorment as: a=basic, b=extra, c=extended |
|competition_distance | distance in meters to the nearest competitor store |
|competition_open_since_month | the approximate month competitor was opened |
|competition_open_since_year | the approximate year competitor was opened |
|promo2 | wheter the store was participating on a consecutive promotion (1) or not (0)|
|promo2_since_week | indicates the calendar week the store was participating in promo2 |
|promo2_since_year | indicates the year the store was participating in promo2 |
|promo2_interval | indicates the intervals in which promo2 started |
</details>

<details><summary>Variables created during the project development goes as follow:</summary><br>

Variable | Definition
------------ | -------------
| year | year from date that the sales occurred |
| month | month from date that the sales occurred |
| day | day from date that the sales occurred |
| week_of_year | week of the year from date that the sales occurred, considering the first week of a year a thursday and begins at 1. (int type) |
| year_week | week of the year from date that the sales occurred, considering the first week of a year with a monday and begins at 0. (object type, %Y-%W) |
| season | season from date that the sales occurred |
| competition_open_since | concatenation of 'competition_open_since_year' and 'competition_open_since_month' |
| competition_open_timeinmonths | calculates the time in months that competitor has been open based on the purchased date |
| promo2_since | concatenation of 'promo2_since_year' and 'promo2_since_week' |
| promo2_since_timeinweeks | calculates the time in weeks that promotion began based on the purchased date |
| month_map | month from date that the sales occurred as auxiliar feature |
| is_promo2 | whether the purchase occurred during an active promo2 (1) or not (0)  |
<!-- | x | xxx | -->
</details><br>

## 4. Abordagem para solução do problema
1. Limpeza de dados
2. Feature Engineering
3. Filtragem de variáveis
4. Exploração de dados
5. Preparação dos dados
6. Seleção de variáveis
7. Aplicação de modelos de ML
8. Fine-Tuning Hyperparameter
9. Avaliação dos algoritmos
10. Modelo em produção
<br>

## 5. Top 3 Data Insights
**1. Distance from competitors does not seem to correlate with store sales.** 
<img src="https://user-images.githubusercontent.com/77681284/152861743-97d3a616-0ea7-4129-b250-4fe99f025f9d.png">

**2. Stores sold more in the seconde semester in 2013, but not in 2014.**
<img src="https://user-images.githubusercontent.com/77681284/152862286-1c72acf6-ddbb-47f0-84c0-827ed6029f7d.png">

**3. Sales during the sring correspond to 41.41% of total.**<br>
<img src="https://user-images.githubusercontent.com/77681284/152863943-f8b28f40-5e6f-4c9b-9aec-b035d8f66a32.png">
<br>

## 6. Machile Learning Model
Machine learning models used:
* Linear Regression
* Regularized Linear Regression
* Random Forest Regressor
* Xgboost Regressor <br><br>

Results after cross-validation, where:
MAE = mean absolute error;
MAPE = mean absolut percentage error;
RSME = root mean squared error.<br><br>
![image](https://user-images.githubusercontent.com/77681284/152865017-82031281-0faa-4621-ac08-e7ef30bf4dd3.png)

Final xgboost result after fine tunning:<br><br>
![image](https://user-images.githubusercontent.com/77681284/152865128-2ffe1a2e-ab84-405d-a323-44af6c71d95e.png)

Error rate: <br>
![image](https://user-images.githubusercontent.com/77681284/152866889-f0980683-cf4f-4912-b5e8-ba00f8f41887.png)


## 7. Telegram Bot
Access telgram bot [here](https://t.me/rossmannMBA_bot).<br>
![image](https://user-images.githubusercontent.com/77681284/152866141-84e53ce0-b44d-4e25-8614-dce0e3b36368.png)


## 8. Conclusion
The objective of this project was develop a prediction model for Rossmann stores. Developing the telegram bot as the data deliverable product successfully satisfies the CFO demands.

## 9. Next Steps
* Address missing values in a better way.
* Test other machine learning models.
* Improve messages on telegram bot.

----
**References:**
* Blog [Seja um Data Scientist](https://sejaumdatascientist.com/eu-criei-esse-projeto-e-consegui-meu-primeiro-emprego-como-data-scientist/)
* Dataset Rossmann Store Sales from [Kaggle](https://www.kaggle.com/c/rossmann-store-sales/overview)
* Variables meaning on [Kaggle](https://www.kaggle.com/c/rossmann-store-sales/data)

----
