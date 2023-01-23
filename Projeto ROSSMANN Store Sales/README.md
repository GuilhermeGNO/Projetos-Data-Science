# Rossmann Store Sales -> Data Science Project

![rossmann](https://user-images.githubusercontent.com/75986085/152585675-a7ceff53-8a6f-4548-84ea-abfd32c00fbf.png)

<a href='https://github.com/xGabrielR/Rossmann-Store-Sales/blob/main/notebooks/Storytelling_Documentation_Rossmann.pdf'>Full PDF Documentation PT-BR.</a>

<h2>0. Rossmann Stores Data and Info</h2>
<p>Rossmann are a chain of pharmacies located in Europe, mainly in Germany, with around 56,200 employees and more than 4000 stores. The company was founded by Dirk Rossmann with its headquarters in Burgwedel near Hanover in Germany. ~ Wiki.</p>
<p>What is a pharmacies chain?<br>Basically the chain start with one shop open named 'matrix', the next shop open is the branche. Have two types of chain, the associated chain is when several pharmacies with different owners get together & private chain which starts with the 'matrix' company and has a general owner.</p>

<p>Rossmann CFO on a monthly results meeting asked to all store mananger a sales forecast for the next six months.</p>

<p>CFO Like to know next sales for start a reform of all shops.
Pharmaceutical Bussiness Model
Rossmann is present with an e-commerce and in physical stores available for sales of household items, makeup and of course drugstore items, as it is a chain of pharmacies, it is spread over several parts of Europe, thus being able to select regions with greater growth potential and reducing the competition rate.
'First Assumptions'</p>
<p>The Course Base <a href='https://sejaumdatascientist.com/eu-criei-esse-projeto-e-consegui-meu-primeiro-emprego-como-data-scientist/'>Seja Um Data Scientist</a>.</p>

<ul>
  <dl>
    <dt>Market Size.</dt>
      <dd>All persons over 18 years old, with preference for older persons.</dd>
    <dt>Marketing Channels.</dt>
      <dd>Rossmann Website & Shops.</dd>
    <dt>Principal Metrics.</dt>
      <dd>Channel Offline: Working on physical stores.</dd>
      <dd>Recency: Purchases over time.</dd>
      <dd>Frequency: Shop sales frequency for sales forecast.</dd>
      <dd>Market Share: Sales competitions.</dd>
  </dl>
</ul>

![chanel](https://user-images.githubusercontent.com/75986085/153439927-f4684894-7067-4023-b089-2116e6d5a7bb.png)

1. Do older customers buy more from physical stores or from competitors?
2. What is the marketing investment compared to physical stores in terms of e-commerce?
3. What are the new products that make customers buy from Rossmann stores instead of competing stores?
4. How do these stores behave in terms of receiving new merchandise to sell to new customers?
5. Are the products sold easily accessible?
6. How are the prices of the products in relation to the location of the stores?
7. How are rossmann products and stores being evaluated?
8. What is the buying process like for these customers?
9. Would a customer who bought in a physical store buy again?
10. How much does a customer cost for physical stores?
11. Who are the main partners of the rossmann brand?
12. Is there a community of customers where they can engage with the products? ...

<p>Data Information at: https://www.kaggle.com/c/rossmann-store-sales</p>

<p>First Deploy is Telegram Bot</p>

![rossbot](https://user-images.githubusercontent.com/75986085/155425763-b8051e72-e81a-4287-a43e-d2fdc4e35adf.gif)

<p>Second Deploy executable software.</p>
<p>In Dev</p>

<h2>1. Business Problem</h2>

<p>Rossman's CFO would like to predict how much money its stores will generate to renovate them in the future.</p>
<p>Rossmann CFO, asked to all of shops merchant's to send for him this prediction, with this problem, all rossmann's merchant's asked to data/analisys team this prediction.</p>
<p>New Version of project (04/02/2021)</p>

<h2>2. Solution Strategy & Assumptions </h2>
<h3>First CRISP Cycle</h3>

<h4>2.1. After Stakeholder Interview</h4>

> *How might we identify the budget needed for stores reformation?*

<h4>2.2. Data Product</h4>

> *A.I Model to forecast the sales at smartphone*

<ul>
  <dl>
    <dt>Data Clearing & Descriptive Statistical.</dt>
      <dd>First real step is download the dataset, import in jupyter and start in seven steps to change data types, data dimension, fillout na... At first statistic dataframe, i used simple statistic descriptions to check how my data is organized.</dd>
    <dt>Feature Engineering.</dt>
      <dd>In this step, with coggle.it to make a mind map and use the mind map to create some hypothesis list, after this list, i created some new features based on date.</dd>
    <dt>Data Filtering.</dt>
      <dd>Simple way to reduce dimensionality of dataset.</dd>
    <dt>Exploration Data Analysis.</dt>
      <dd>Validation of all hypotesis list with data.</dd>
    <dt>Data Preparation.</dt>
      <dd>Split & Prepare and Prepare & Split, this two versios of preparation can provide data leak.</dd>
    <dt>Machine Learning Modeling.</dt>
      <dd>Selection of Four ML Models, Base, Linear and two Tree-Based.</dd>
  </dl>
</ul>

<h2>3. EDA Insight's</h2>

<p>After brainstorming and hypothesis validation, some insights appeared.</p>
<h3> Top 3 Insight's </h3>
<ul>
  <li>Stores with large assortment, sell less.</li>

![sales](https://user-images.githubusercontent.com/75986085/153096505-fe9a9afb-f6e6-451d-a85d-d5579839071d.jpeg)

  
  <li>Stores with consecutive promo, sell less if long time of promo.</li>
  
![promo](https://user-images.githubusercontent.com/75986085/153096571-6f01a3b5-a87c-487d-acdd-7c1592e379c3.jpg)

  
  <li>Stores with closely competitors, sell more.</li>
  
![less](https://user-images.githubusercontent.com/75986085/153096584-eb58b3c4-2d4e-457e-a7f8-82ef6f9b5604.jpg)
  
</ul>

<h2>4. Data Preparation</h2>
<p>When you have "date" features on dataset, its possible to you get data leak during model training. I have selected two tipes of preparation, one splited train and test after data preparation, and before data preparation to check the data leakege.</p>
<ul>
  <dl>
    <dt>Categorical Data.</dt>
      <dd>Used the Frequency Encoding to all Categorical Data.</dd>
    <dt>Normalization.</dt>
      <dd>After KStest and QQplot, it was not necessary to normalize, because dont have normal distribution.</dd>
    <dt>Nature Transformation.</dt>
      <dd>Working with Sin/Cos for seasonal data.</dd>
  </dl>
</ul>
<h3>4.1. Frequency Encoding</h3>
<p>It is an encoder method that takes into account the number of times the value appears, for example in 10 records, 5 of which are blue and red, so the frequency is .5%
</p>

<h3>4.2. QQPlot</h3>
<p>With QQPlot Quantile-Quantile Plot it is possible to observe how close the tested distribution is to a normal distribution, the normal distribution is characterized when blue line is equal to red line, there are other ways of doing this verification such as statistical tests, among others.</p>

![1](https://user-images.githubusercontent.com/75986085/154390648-3e89fe22-c6f8-4e65-ac09-b025e364766a.png)

<h3>4.3. Feature Selection</h3>
<p>XGBoost Feature Importance is a fast and good way to see which feature is important, feature selection is a second way to select features for better performace of model and following the principles of Occam's Razor.</p>

![feature_importance](https://user-images.githubusercontent.com/75986085/154825186-179f4ce0-86f8-4add-96ac-4138eed46c62.png)

<p>Feature selection is one of most importante step on data science projects.</p>

<h2>5. Machine Learning Models</h2>
<p>I have used three models, SVR (Support Vector Regression), Random Forest and XGBoost (Gradient boosted decision tree).</p>

![models](https://user-images.githubusercontent.com/75986085/154582560-384c54b0-c4a3-4e11-8862-5905ac12c197.png)

<p>I have selected the XGBoost than all of other two for production, in the step of hyperparameter fine tuning I used a tuning technique called Random Search and tested the trained model in the dataset with data leakage and in the dataset without data leakage. The information are in Notebook m03_machine_learningII.</p>

<p>Neural Network performace for aprox 40 epochs.</p>

![nn](https://user-images.githubusercontent.com/75986085/155723418-ae002196-8c5f-40a3-85be-0e74ba9337ea.png)


<h2>6. Bussiness Results</h2>
<p>This istep is to convert the model performace in money!!.</p><p>Below have model performace for two of the mos harder shops to forecast, there are stores where the algorithm cannot predict sales, so the RMSE error was high. MAE error be greater too, to avoid this is train more the model and work on better features. Have two columns, worst & best scenario, this columns is the sum and subtraction respectively os MAE for each model forecast.</p>

![hard_shops](https://user-images.githubusercontent.com/75986085/155026649-f00b6e31-740c-465e-b67c-ddccee4342e8.png)

<p>Below have the Sum of sales for each senario.</p>

![model_money](https://user-images.githubusercontent.com/75986085/155026940-46e5fd45-4d2c-4287-bf5e-ae2ccea0cbf8.png)

<h2>7. Model Deployment</h2>
<p>For deployment i selected Heroku for base clound 24/7h free.</p>
<p>Made a Telegram Bot and Personal '.exe' app for CFO to check the sales on smartphone and desktop.</p>

![sales](https://user-images.githubusercontent.com/75986085/155308939-12f879ae-bdde-41f7-b02d-dade281606b6.png)

![img](https://user-images.githubusercontent.com/75986085/155615627-dcbe0fd7-6116-4a91-ae17-40d4e5ee3e8b.png)

<h2>7. References</h2>
<ul>
  <li><a href='https://www.oreilly.com/library/view/practical-statistics-for/9781491952955/'>Practical Statistics Book</li>
  <li><a href='https://www.strategyzer.com/books/business-model-generation'>Model Bussiness Book</li>
  <li><a href='https://www.docusign.com.br/blog/indicadores-do-varejo'>Retail Metrics</li>
  <li><a href='https://www.kaggle.com/bhavikapanara/frequency-encoding'>Frequency Encoding</li>
  <li><a href='https://en.wikipedia.org/wiki/Gradient_boosting'>Gradient Boosting</li>
  <li><a href='https://en.wikipedia.org/wiki/Occam%27s_razor'>Occam's Razor</li>
  <li><a href='https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/'>Random Search Tuning</li>
</ul>
