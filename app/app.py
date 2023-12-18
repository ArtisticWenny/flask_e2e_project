from flask import Flask, render_template, request, jsonify
import pandas as pd
import geopandas as gpd
import json
import requests
import matplotlib.pyplot as plt
import io
import os
import authlib
import base64
import sentry_sdk


sentry_sdk.init(
    dsn="https://c2c707a5fb4afe23fe0cae1f76224e01@o4506412108480512.ingest.sentry.io/4506412111691776",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def index():
    # Access API key from environment variable
    api_key_1 = os.getenv("API_KEY_1")
    
    # Make an API call using the key (replace with your actual API call)
    # ...
    
    # Render the HTML template with data (optional)
    return render_template("index.html", api_key=api_key_1)

if __name__ == "__main__":
    app.run(debug=True)

df_COVID19deaths = pd.read_csv('https://raw.githubusercontent.com/ArtisticWenny/flask_e2e_project/main/data/COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv')
merged_map = pd.read_csv('https://raw.githubusercontent.com/ArtisticWenny/flask_e2e_project/main/data/covid-19-pandemic-worldwide-data.geojson')
df_COVIDMAP = gpd.read_file('https://raw.githubusercontent.com/ArtisticWenny/flask_e2e_project/main/data/covid-19-pandemic-worldwide-data.geojson')
df_COVIDMAP.dtypes

@app.route('/data')
def data(data=df_COVID19death):
    data = data
    return render_template('data.html', data=data)



@app.route('/', methods=['GET', 'POST'])
def index():
    states = sorted(df_COVID19deaths['StateDesc'].unique())
    selected_state = request.form.get('state') or states[0]
    
    img = create_plot(selected_state)
    
    return render_template("index.html", states=states, selected_state=selected_state, img=img)


    return base64.b64encode(img.getvalue()).decode()


if __name__ == "__main__":
    app.run(debug=True)



if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
        )



