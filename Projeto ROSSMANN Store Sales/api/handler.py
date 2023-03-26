# Biblioteca Flask, lida com requests da web
import                        os
from flask             import Flask, request, Response
from rossmann.Rossmann import Rossmann
import pandas as pd
import pickle



# loading the model
model = pickle.load(open('model/model_rossman.pkl', 'rb'))

# initialize API
app = Flask( __name__ )

# Criando o endpoint, a url que ira receber os dados/request's
# POST = somente envia dados, olhar documentação
# O @app.route, executará a primeira função que esta abaixo dele
@app.route('/rossmann/predict', methods = ['POST'] )
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # teste para verificar se existe dados em resposta
        if isinstance( test_json, dict): # teste se existe somente uma linha de retorno
            test_raw = pd.DataFrame(test_json, index = [0] )
            
        else: # teste para vericar se existe multiplos exemplos
            test_raw = pd.DataFrame( test_json, columns = test_json[0].keys() )
            
        # Instanciando a classe Rossmann
        pipeline = Rossmann()
        
        # Data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # Feature Engineering 
        df2 = pipeline.feature_engineering(df1)
        
        # Data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)
            
        return df_response
    
    else:
        return Response( '{}', status = 200, mimetype = 'application/json')
    
if __name__ == '__main__':
    os.environ.get('PORT', 5000)
    app.run('0.0.0.0', port = port)
