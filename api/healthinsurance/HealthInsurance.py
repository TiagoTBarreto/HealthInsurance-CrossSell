import pickle
import inflection

class HealthInsurance (object):
    def __init__(self):
        self.mms_vintage = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/mms_vintage.pkl', 'rb'))
        self.mms_age = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/mms_age.pkl', 'rb'))
        self.ss = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/ss.pkl', 'rb'))
        self.frequency_gender = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/frequency_gender.pkl', 'rb'))
        self.target_encode_policy_sales = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/target_encode_policy_sales.pkl', 'rb'))
        self.target_encode_region_code = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/target_encode_region_code.pkl', 'rb'))
        self.target_encode_vehicle_age = pickle.load(open('/home/tiagobarreto/DS/repos/health-insurance1/parameter/target_encode_vehicle_age.pkl', 'rb'))
    
    def data_cleaning(self, df1):
        # rename columns
        cols_old = list(df1.columns)
        cols_new = [inflection.underscore(col) for col in cols_old]
        df1.columns = cols_new

        return df1
    
    def feature_engineering(self, df2):
        # feature engineering
        df2['vehicle_damage'] = df2['vehicle_damage'].apply(lambda x: 1 if x == 'Yes' else 0)
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'old' if x == '> 2 Years' else 'used' if x == '1-2 Year' else 'new')
    
        return df2

    def data_preparation(self, df5):
        # standartization
        df5['annual_premium'] = self.ss.fit_transform(df5[['annual_premium']].values)

        # rescaling
        df5['age'] = self.mms_age.fit_transform(df5[['age']].values)
        df5['vintage'] = self.mms_vintage.fit_transform(df5[['vintage']].values)

        # encoding       
        df5['gender'] = df5['gender'].map(self.frequency_gender)

        df5.loc[:, 'region_code'] = df5['region_code'].map(self.target_encode_region_code)

        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(self.target_encode_policy_sales)

        df5.loc[:, 'vehicle_age'] = df5['vehicle_age'].map(self.target_encode_vehicle_age)
        df5['vehicle_age'] = df5['vehicle_age'].astype(float)

        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code','policy_sales_channel', 'previously_insured', 'vehicle_damage', 'vehicle_age', 'gender']

        return df5[cols_selected]

    def get_prediction(self, model, original_data, test_data):   

        result_data = original_data.copy()
        # prediction
        pred = model.predict_proba(test_data)
        result_data['Percentage'] = pred[:, 1]
        result_data = result_data.sort_values('Percentage', ascending = False)

        return result_data.to_json(orient = 'records', date_format = 'iso')