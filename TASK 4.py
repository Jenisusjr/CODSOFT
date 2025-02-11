import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movie_title, movies_df, num_recommendations=5):
    # Convert genres into a TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['genres'].fillna(''))
    
    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Get the index of the movie
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    # Get recommended movie titles
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices]

# Example dataset
movies_data = {
    'title': ["Inception", "Interstellar", "The Dark Knight", "The Matrix", "Avatar"],
    'genres': ["Sci-Fi Thriller", "Sci-Fi Adventure", "Action Crime Thriller", "Sci-Fi Action", "Fantasy Adventure"]
}
movies_df = pd.DataFrame(movies_data)

# Example usage
print(recommend_movies("Inception", movies_df))