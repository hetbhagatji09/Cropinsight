from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import pickle

with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

app= Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    district_name = request.form.get('district_name')
    market_name = request.form.get('market_name')
    commodity = request.form.get('commodity')
    min_price = float(request.form.get('min_price'))
    max_price = float(request.form.get('max_price'))
    
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    day = int(request.form.get('day'))
    
    # Create a DataFrame with a single row
    data = {
        'District Name': [district_name],
        'Market Name': [market_name],
        'Commodity': [commodity],
        'Min Price(Rs.)': [min_price],
        'Max Price(Rs.)': [max_price],
        'Year': [year],
        'Month': [month],
        'Day': [day]
    }
    
    dataframe = pd.DataFrame(data)
    
    # Debug: print DataFrame
    print("DataFrame for prediction:")
    print(dataframe)
    
    try:
        print('hejkbewc ,sz')
        # Make predictions
        predictions = pipeline.predict(dataframe)
        # print("Predictions:", predictions)
    except Exception as e:
        print("Error during prediction:", str(e))
        return render_template('predict.html')
    
    return render_template('predict.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)
