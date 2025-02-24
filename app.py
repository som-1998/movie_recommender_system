from flask import Flask, render_template, request
import sqlite3
import numpy as np
import pandas as pd
import requests
from helper.helper_functions import recommended
from data import movies_df, similarity


app = Flask(__name__)




# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    movie_list = movies_df['title'].tolist()
    recommendations = None
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            recommendations = recommended(movie_name = selected_movie, movies_df=  movies_df, similarity_matrix=similarity,TOP_N = 5 )

    return render_template('index.html', movies=movie_list, recommendations=recommendations, selected_movie=selected_movie)

if __name__ == '__main__':
    app.run(debug=True)