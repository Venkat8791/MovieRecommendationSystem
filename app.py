import numpy as np
import pandas as pd
import json
import requests



from flask import Flask, render_template


app = Flask(__name__)



def get_popular_movies():
    popular_movies = pd.read_csv('/datasets/popularmovies.csv')
    return list(popular_movies['id'].head(10))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
