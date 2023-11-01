from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
import random
from flask_cors import CORS

app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self,number):

        row_df = pd.DataFrame.from_dict({'tx_amount': [number+random.randint(0,10)],
                        'tx_time_seconds': [number+random.randint(0,10)],
                        'tx_time_days': [number+random.randint(0,10)]})        
                
        model = pickle.load(open('dump.pkl', 'rb'))
        prediction = model.predict(row_df)       
        return str(prediction)

api.add_resource(prediction, '/prediction/<int:number>')

if __name__ == '__main__':
    app.run(debug=True)
