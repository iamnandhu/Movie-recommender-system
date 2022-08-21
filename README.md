
# Movie Recommendation System
A simple recommendation system made using [Streamlit](https://docs.streamlit.io/)


![Logo](https://cdn.pixabay.com/photo/2017/06/02/22/01/dog-2367414_960_720.png)


## Demo

The project is deployed on Heroku. You can view it here [Movie Recommedation](https://recommend-18.herokuapp.com/)


## How recommendation works!

Recommender systems are an important class of machine learning algorithms that offer relevant suggestions to users. Recommendation Systems work based on the similarity between either the content or the users who access the content.Youtube, Amazon, Netflix, all function on recommendation systems where the system recommends you the next video or product based on your past activity (Content-based Filtering) or based on activities and preferences of other users similar to you (Collaborative Filtering)

In this project we calculats the cosine of angle between the vectors (keywords in this case) projected in multidimensional space.
We achieve this by utilizing

*CountVectorizer* from *sklearn.feature_extraction.text* to convert the keywords to vectors and

*cosine_similarity* from *sklearn.metrics.pairwise* to calculate the distance between each vectors




## Screenshots

![screenshot](https://github.com/iamnandhu/Movie-recommender-system/blob/master/Screenshot.png)

