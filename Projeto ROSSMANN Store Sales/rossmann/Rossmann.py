import pickle
import inflection
import pandas as pd
import numpy as np
import math
import datetime

class Rossmann(object):
    def __init__( self ):
        self.path = '' 
        self.competition_distance_scaler    = pickle.load( open( self.path + 'parameter/competition_distance_scaler.pkl', 'rb'))
        self.competition_time_month_scaler  = pickle.load( open( self.path + 'parameter/competition_time_month_scaler.pkl', 'rb'))
        self.promo_time_week_scaler         = pickle.load( open( self.path + 'parameter/promo_time_week_scaler.pkl', 'rb'))
        self.year_scaler                    = pickle.load( open( self.path + 'parameter/year_scaler.pkl', 'rb'))
        self.store_type_scaler              = pickle.load( open( self.path + 'parameter/store_type_scaler.pkl', 'rb'))
        
    def data_cleaning(self, df1):
        
        # 1.1 Rename Columns
        # Foi removido da cols_old, Sales and Customers

        cols_old = ['Store', 'DayOfWeek', 'Date', 'Open', 'Promo',
               'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment',
               'CompetitionDistance', 'CompetitionOpenSinceMonth',
               'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek',
               'Promo2SinceYear', 'PromoInterval']

        # Colocar os nomes todos em minusculo e underscore
        snakecase = lambda x: inflection.underscore( x )

        cols_new = list(map(snakecase, cols_old ))

        # Rename
        df1.columns = cols_new

        ## 1.3 Data Types 

        # Transformação da coluna date
        df1['date'] = pd.to_datetime(df1['date'])

        ## 1.5 Fillout NA 

        # Consultar funcao criada para descricao do dicionario, glossary(glossary_df) 
        # competition_distance (compeditor mais proximo)
        df1['competition_distance'] = df1['competition_distance'].apply(lambda x: 200000.0 if math.isnan(x) else x )

        # competition_open_since_month (mes e ano que o competidor abriu uma 'loja')
        # se eu tenho a informacao dos metros em competitor_distacen, fica ilogico eu nao tem a informacao do mes ou ano de que
        # o competidor abriu a loja
        # Motivos de NA, pode nao existem competidor perto
        # Pode nao ter sido anotado, a data de abertura do competidor
        # Ou quando a loja da Rossman foi aberta, ja existia um competidor
        # O tempo que eu tenho competidor mais proximo pode influenciar no motivo de aumento ou diminuicao de vendas
        df1['competition_open_since_month'] = df1.apply(lambda x: x['date'].month if math.isnan(x['competition_open_since_month'])
                                                                                 else x['competition_open_since_month'], axis = 1)

        # competition_open_since_year
        # Nos da a informacao do mes ou ano que o competidor mais proximo, abriu loja
        df1['competition_open_since_year'] = df1.apply(lambda x: x['date'].year if math.isnan(x['competition_open_since_year'])
                                                                               else x['competition_open_since_year'], axis = 1)

        # Promo2 é uma consecutiva e continua informação se a loja esta em uma promoção

        # promo2_since_week
        # Descreve o ano e semana quando a loja comecou a partipar da Promo2
        df1['promo2_since_week'] = df1.apply(lambda x: x['date'].week if math.isnan(x['promo2_since_week']) 
                                            else x['promo2_since_week'], axis = 1 )
        # promo2_since_year
        df1['promo2_since_year'] = df1.apply(lambda x: x['date'].year if math.isnan(x['promo2_since_year'])
                                            else x['promo2_since_year'], axis = 1 )

        # promo_interval
        # Descreve o intervalo consecutivo que a Promo 2 foi iniciada, nomeando os meses que ela comecou outra vez, por exemplo
        # Feb, May, Aug, Nov, significa que cada nova promocao comecou nesses meses
        month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                     7: 'Jul', 8: 'Aug', 9: 'Sept', 10: 'Oct',11: 'Nov',12: 'Dec'}

        # Preenchi os valores NaN por 0
        df1['promo_interval'].fillna(0, inplace = True)

        # Peguei as datas de vendas daquela loja e coloquei em uma coluna com o nome do respectivo mes
        df1['month_map'] = df1['date'].dt.month.map(month_map)


        # Se o mes contido na coluna month_map esta na coluna promo_interval, significa que estava em promocao, entao
        # 0 sera para lojas que nao aderiram a promocao consecutiva ou continua e 1 sera para as quais aderiram
        # Esse procedimento foi realizado, pois no desenvolvimento de modelos de ML, vemos como interessante saber se a 
        # loja, estava ou nao em promocao, apesar de termos a informacao dos meses que a loja estava em promocao, e necessario
        # transformar essa informacao de string para numerica
        df1['is_promo'] = df1[['promo_interval', 'month_map']].apply(lambda x: 0 if x['promo_interval'] == 0 
                                                                     else 1 if x['month_map'] in x['promo_interval'].split( ',' )
                                                                     else 0, axis = 1 )

        ## 1.6 Change Types 

        # As informacoes das datas estavam em decimais
        df1['competition_open_since_month'] = df1['competition_open_since_month'].astype(int)
        df1['competition_open_since_year'] = df1['competition_open_since_year'].astype(int)
        df1['promo2_since_week'] = df1['promo2_since_week'].astype(int)
        df1['promo2_since_year'] = df1['promo2_since_year'].astype(int)
        
        return df1

    def feature_engineering( self, df2):
        ## 2.3. Feature Engineering
        # year
        df2['year'] = df2['date'].dt.year

        # month
        df2['month'] = df2['date'].dt.month

        # day
        df2['day'] = df2['date'].dt.day

        # week of year
        df2['week_of_year'] = df2['date'].dt.weekofyear

        # year week
        df2['year_week'] = df2['date'].dt.strftime( '%Y-%W')

        # competition since
        # adicionado da1 = 1, pois nas colunas manipuladas, não temos o dia então generalizamos
        df2['competition_since'] = df2.apply( lambda x: datetime.datetime( year = x['competition_open_since_year'],
                                                                          month = x['competition_open_since_month'], day = 1),
                                                                          axis = 1 )

        # O tempo que a competição começou em meses
        df2['competition_time_month'] = (( df2['date'] - df2['competition_since']) / 30 ).apply( lambda x: x.days).astype(int)

        # promo since
        df2['promo_since'] = df2['promo2_since_year'].astype(str) + '-' + df2['promo2_since_week'].astype(str)

        df2['promo_since'] = df2['promo_since'].apply(
                                      lambda x:datetime.datetime.strptime ( x + '-1', '%Y-%W-%w') - datetime.timedelta( days = 7 ))

        # Resultada da diferença em semanas
        # A promocao comecou, antes ou depois da ultima venda?
        # valores positivos, ela estava ou esta em promocao
        # valores negativos, ela entrou em promocao depois da data da ultima venda
        df2['promo_time_week'] = (( df2['date'] - df2['promo_since'] ) / 7 ).apply(lambda x: x.days).astype(int)

        # assortment
        df2['assortment'] = df2['assortment'].apply( lambda x: 'basic' if x == 'a' else 'extra' if x == 'b' else 'extended')

        # state holiday
        df2['state_holiday'] = df2['state_holiday'].apply(lambda x: 'public_holiday' if x == 'a'
                                                                     else 'easter_holiday' if x == 'b'
                                                                     else 'christmas' if x == 'c' else 'regular_day')

        ### 3.1. Filtragem de linhas
        # Retirada do filtro a coluna Sales

        df2 = df2[df2['open'] != 0]

        ### 3.2. Seleção das colunas
        # Customers, não temos o número de customers para o momento daqui 6 meses, o que não é a proposta do projeto
        # Open, não nos fornece muitas informações, já que 0 e fechado e 1 e simsplismente loja aberta
        # Promo_interval, geramos variáveis dela, ou seja, outras colunas, dessa maneira, podemos descarta-la
        # Month_map, geramos variáveis dela, ou seja, outras colunas, dessa maneira, podemos descarta-la
        # Retirado de cols_drop, a coluna customers
        cols_drop = ['open', 'promo_interval', 'month_map']
        df2 = df2.drop(cols_drop, axis = 1)
        
        return df2
    
    def data_preparation(self, df5):

        # competiton distance
        # Devido a apresentacao de outliers, sera utilizada RobustScaler
        df5['competition_distance'] = self.competition_distance_scaler.transform(df5[['competition_distance']].values )
        # Salvando as transformaçães em pickle, para aplicação em dados novos

        # competition_time_month
        df5['competition_time_month'] = self.competition_time_month_scaler.transform(df5[['competition_time_month']].values )

        # promo_time_week
        df5['promo_time_week'] = self.promo_time_week_scaler.transform(df5[['promo_time_week']].values )

        # year
        df5['year'] = self.year_scaler.transform(df5[['year']].values )

        ### 5.3. Transformação

        #### 5.3.1 Encoding

        # state_holiday - One-Hot Encoding
        df5 = pd.get_dummies(df5, prefix = ['state_holiday'], columns = ['state_holiday'])

        # store_type - Label Encoding
        df5['store_type'] = self.store_type_scaler.transform(df5['store_type'])


        # assortment - Ordinal Encoding
        assortment_dict = {'basic': 1, 'extra':2, 'extended':3}
        df5['assortment'] = df5['assortment'].map(assortment_dict)

        #### 5.3.3 Nature Transformation

        # day of week - Atencao para ajustar o periodo max, por exemplo dias 7, mes 30, ... ciclos !
        df5['day_of_week_sin'] = df5['day_of_week'].apply(lambda x: np.sin( x * (2. * np.pi/7 ) ) )
        df5['day_of_week_cos'] = df5['day_of_week'].apply(lambda x: np.cos( x * (2. * np.pi/7 ) ) )

        # month
        # Divido pelo número do ciclo, para mês, 12
        df5['month_sin'] = df5['month'].apply(lambda x: np.sin( x * (2. * np.pi/12 ) ) )
        df5['month_cos'] = df5['month'].apply(lambda x: np.cos( x * (2. * np.pi/12 ) ) )

        # day
        # Divido pelo número do ciclo, para o dia, 30
        df5['day_sin'] = df5['day'].apply(lambda x: np.sin( x * (2. * np.pi/30 ) ) )
        df5['day_cos'] = df5['day'].apply(lambda x: np.cos( x * (2. * np.pi/30 ) ) )

        # week of year
        # Divido pelo número do ciclo, para a semana do ano, 52
        df5['week_of_year_sin'] = df5['week_of_year'].apply(lambda x: np.sin( x * (2. * np.pi/52 ) ) )
        df5['week_of_year_cos'] = df5['week_of_year'].apply(lambda x: np.cos( x * (2. * np.pi/52 ) ) )
        
        cols_selected = ['store',
             'promo',
             'store_type',
             'assortment',
             'competition_distance',
             'competition_open_since_month',
             'competition_open_since_year',
             'promo2',
             'promo2_since_week',
             'promo2_since_year',
             'competition_time_month',
             'promo_time_week',
             'day_of_week_sin',
             'day_of_week_cos',
             'month_sin',
             'month_cos',
             'day_sin',
             'day_cos',
             'week_of_year_sin',
             'week_of_year_cos']
        
        return df5[cols_selected]
    
    def get_prediction(self, model, original_data, test_data ):
        # prediction
        pred = model.predict( test_data )
        
        # Join pred into the original data
        original_data['predictions'] = np.expm1( pred )
        
        return original_data.to_json( orient = 'records', date_format = 'iso' )
