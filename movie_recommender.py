import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8ac088ea98a3ee9cefd0b8037bc89146&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

movies_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Select the movie...',
    movies_list)

if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_posters[4])