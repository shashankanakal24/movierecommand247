import streamlit as st
import pickle
import requests

def fetch_poster(movie_title):
    url = "http://www.omdbapi.com/"
    params = {"apikey": "6cf650ff", "t": movie_title}
    data = requests.get(url, params=params).json()
    poster_path = data.get('Poster', '')
    return poster_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

# Create a dropdown to select a movie
selected_movie = st.selectbox("Select a movie:", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), key=lambda vector: vector[1], reverse=True)
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]]['title'])
        movie_title = movies.iloc[i[0]]['title']
        recommend_poster.append(fetch_poster(movie_title))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        if movie_poster[0]:
            st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        if movie_poster[1]:
            st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        if movie_poster[2]:
            st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        if movie_poster[3]:
            st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        if movie_poster[4]:
            st.image(movie_poster[4])
