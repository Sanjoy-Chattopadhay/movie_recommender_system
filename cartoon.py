import pickle
import pandas as pd
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# with st.sidebar:
#     selected = option_menu(
#         menu_title = 'Main Menu',
#         options=["Movies",'Cartoons'],
#         icons=['house','book','envelope'],
#         default_index=0,
#         orientation='horizontal',
#
#     )
selected = option_menu(
        menu_title = 'Hii, I Welcome you to my Recommender Machine:  ',
        options=['Source Code','Contact Me','My Portfolio'],
        icons=['house','book','envelope'],
        default_index=-1,
        orientation='horizontal',

    )
if selected == 'Cartoon':
    st.title("Cartoon")
if selected == 'Movies':
    st.title("Movies")

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c0617ea9b5e793517d64f7c5a4818b78&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = cartoon_similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters= []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


cartoons_dict = pickle.load(open('cartoons_dict.pkl','rb'))
movies= pd.DataFrame(cartoons_dict)

cartoon_similarity = pickle.load(open('cartoon_similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox("How do you want to get connected? ",movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])