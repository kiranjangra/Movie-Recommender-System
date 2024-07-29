import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_ = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list_:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ad5218cb1aee668a12cceea807a4975d&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

similarity = pickle.load(open('tfidf_similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Select your movie',
    movies['title'].values)
# options = list(range(1, 16))
# selected_no_movie_name = st.selectbox(
#     'Select how many recommended movies you want',
#     options)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5,gap="medium")
    with col1:
        st.subheader(names[0])
        st.image(posters[0])
    with col2:
        st.subheader(names[1])
        st.image(posters[1])
    with col3:
        st.subheader(names[2])
        st.image(posters[2])
    with col4:
        st.subheader(names[3])
        st.image(posters[3])
    with col5:
        st.subheader(names[4])
        st.image(posters[4])
