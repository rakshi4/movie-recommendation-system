import pickle
import streamlit as st
import pandas as pd
import requests
import time

# Fetch poster with error handling
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dc557161d390fb4c75e72b77bb1b1a8f&language=en-US"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        time.sleep(0.5)  # to prevent overloading the API

    return recommended_movie_names, recommended_movie_posters

# Streamlit app UI
st.header('🎬 Movie Recommender System')

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)  # Use modern syntax instead of beta_columns
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
