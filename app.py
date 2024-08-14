from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    district_name = request.form.get('district_name')
    market_name = request.form.get('market_name')
    commodity = request.form.get('commodity')
    min_price = float(request.form.get('min_price'))
    max_price = float(request.form.get('max_price'))
    
    year = request.form.get('year')
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
    
    new_data_df = pd.DataFrame(data)

    # Predict using the pipeline (assuming you have a pipeline defined)
    with open(r'C:\Users\hetbh\OneDrive\Desktop\CropInsight3\Artifacts\price.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    prediction = pipeline.predict(new_data_df)
    
    return render_template('predict.html', prediction=prediction[0])



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
