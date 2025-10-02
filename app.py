import pickle
import streamlit as st
import requests
 
 
      
st.header(" MOVIE FROM ME FOR U...")
movies = pickle.load(open('artificats/movie_list.pkl','rb'))
similarity = pickle.load(open('artificats/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'TYPE / SELECT A MOVIE TO GET YOUR SIMILAR MOVIE ',
    movie_list
)
 
 
# def fetch_poster(movie_id):
#     url = 'https://api.themoviedb.org/3/discover/movie/{}?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc'.format(movie_id)
#     data = requests.get(url)
#     data =data.json()
#     poster_path = data['poster_path']
    
    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name


if st.button('show recommendation'):
    recommended_movies_name = recommend(selected_movie)

    if len(recommended_movies_name) > 1:
        num_to_show = min(5, len(recommended_movies_name))
        cols = st.columns(num_to_show)
        for i in range(num_to_show):
            with cols[i]:
                st.text(recommended_movies_name[i])
    else:
        st.warning("Not enough recommendations to display (need at least 2).")
