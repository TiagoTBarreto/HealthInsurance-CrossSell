import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance
import pickle 

# loading model
model = pickle.load( open('model/model_health_insurance.pkl', 'rb'))

app = Flask(__name__)

@app.route( '/predict', methods=['POST'] )
def health_insurance_predict():
    test_json = request.get_json()

    if test_json: # there is data
        if isinstance(test_json, dict): # Unique example
            test_raw = pd.DataFrame(test_json, index=[0])

        else: # Multiple Examples
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys() )
        
        # copy test_raw
        test_raw_inicial = test_raw.copy()

        # instantiate Health Insureance Class
        pipeline = HealthInsurance()
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # feature engineering
        df2 = pipeline.feature_engineering(df1)

        # data preparation
        df3 = pipeline.data_preparation(df2)

        # prediction
        df_response = pipeline.get_prediction(model, test_raw_inicial, df3)

        return df_response
    
    else:
        return Response('{}', status = 200, mimetype='application/json' )
    
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run( '0.0.0.0', port = port, debug = True )