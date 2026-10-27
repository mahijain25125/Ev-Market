from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('../Data/ev_market_dataset.csv')
    total_sales = df['Annual_Sales_Units'].sum()
    avg_range = round(df['Driving_Range_km'].mean(), 1)
    total_models = len(df)
    return render_template('index.html', total_sales=total_sales, avg_range=avg_range, total_models=total_models)

if __name__ == '__main__':
    app.run(debug=True)
