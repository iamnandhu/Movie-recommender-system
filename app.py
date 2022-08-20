import streamlit as st
import pickle
import pandas as pd
import requests

def poster(mov_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=604934b62639e758374f8e6e3931715b&language=en-US '.format(mov_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


sim=pickle.load(open('similar.pkl','rb'))
movies_dict=pickle.load(open('dict_movies.pkl','rb'))
def recommend(mv):
  index=movie[movie['title'] == mv].index[0]
  dist = sim[index]
  mov = sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_mov=[]
  recommended_mov_post=[]
  for i in mov:
    mov_id=movie.iloc[i[0]].movie_id
    #poster
    recommended_mov.append(movie.iloc[i[0]].title)
    recommended_mov_post.append(poster(mov_id))
  return recommended_mov,recommended_mov_post

movie=pd.DataFrame(movies_dict)
st.title('Movie Recommendations')
selected_mov = st.selectbox('Select the movies you are interested in!',movie['title'].values) 

if st.button('Find Similar'):
    names,poster=recommend(selected_mov)
    col1,col2,col3,col4,col5=st.columns(5)
    col=[col1,col2,col3,col4,col5]
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
    
    