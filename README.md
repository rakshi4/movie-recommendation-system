🎬 Movie Recommendation System

GOAL
The main goal of this project is to develop a content-based movie recommendation system using machine learning and natural language processing. It suggests similar movies based on metadata such as cast, crew, genres, and storyline, enhancing user engagement by personalizing movie discovery.

DATASET
Dataset Name: Movie Metadata

Source: TMDB / Kaggle / Custom collected dataset

Format: CSV

Key Features: movie_id, title, genres, overview, keywords, cast, crew

DESCRIPTION
This project leverages a content-based filtering approach to recommend movies. The system uses metadata (plot summaries, genres, cast, etc.) to compute textual similarities between movies. The cosine similarity of vectorized features determines how closely related movies are to one another.

TECHNOLOGIES USED
Pandas: Data loading and cleaning

NumPy: Efficient array operations

Scikit-learn: Feature extraction using CountVectorizer, similarity calculation using cosine_similarity

Pickle: Model serialization

Python: Core logic and scripting

MODEL PIPELINE
Data Cleaning: Loaded movie metadata and filled missing values.

Feature Engineering:

Combined multiple columns (overview, genres, cast, crew, keywords) into a single textual feature.

Applied CountVectorizer to convert text into numerical vectors.

Similarity Calculation:

Used cosine similarity to find movies with similar content.

Model Persistence:

Saved preprocessed data and similarity matrix using Pickle.

Recommendation Logic:

Given a movie title, retrieves the top 5 most similar movies.

WHY CONTENT-BASED FILTERING?
No Need for User Ratings: Works even if user interaction data is unavailable.

Explainable Results: Recommendations are based on visible metadata.

Scalable: Easily extendable to include additional metadata like director, production house, etc.

WHAT I HAD DONE
✅ Loaded and cleaned the movie metadata
✅ Created a combined feature from multiple relevant columns
✅ Vectorized features using CountVectorizer
✅ Computed similarity matrix using cosine similarity
✅ Built a simple terminal-based and Streamlit-based UI
✅ Saved and loaded model components using Pickle

INSTALLATION & USAGE
Installation

bash
Copy
Edit
pip install -r requirements.txt
Run the System

bash
Copy
Edit
python movie_recommendation_system.py
Interactive Streamlit Version

bash
Copy
Edit
streamlit run app.py
RESULTS
The system successfully recommends 5 similar movies for any given movie title.

Fast real-time recommendations due to precomputed similarity matrix.

Easy-to-understand suggestions using visible metadata.

EXAMPLE OUTPUT
markdown
Copy
Edit
Enter a movie title to get recommendations: Inception

Top 5 recommendations:
1. Interstellar
2. The Prestige
3. The Matrix
4. Shutter Island
5. Memento
CONCLUSION
This content-based movie recommender system provides meaningful suggestions without relying on user history. It demonstrates effective use of vectorization, text similarity, and metadata aggregation. This model serves as a strong foundation for further enhancements like hybrid recommendations or integration with user feedback systems.

