# TMDB Movie Recommendation System

This is a **content-based movie recommender system** that uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
It recommends similar movies by analyzing the plot overview, genres, cast, crew, and keywords using **text vectorization** and **cosine similarity**.

---

## Project Structure

```text
movie_recommendation/
├── tmdb_movie_recommendation.ipynb # Main Jupyter notebook (Google Colab-ready)
├── tmdb_5000_movies.csv # Kaggle dataset file (upload manually)
├── tmdb_5000_credits.csv # Kaggle dataset file (upload manually)
├── README.md # Project documentation
```

---

## Dataset Overview

- **Source:** [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used:**
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

- **Key Features Used:**
  - `overview`: movie description
  - `genres`: JSON list of genre tags
  - `keywords`: thematic tags
  - `cast`: top 3 actors
  - `crew`: director
  - Combined into a single `tags` field for modeling

---

## How It Works

1. Merge and clean the TMDB movie and credits datasets
2. Extract relevant fields (`genres`, `cast`, `crew`, `keywords`)
3. Use `CountVectorizer` to convert combined features into numerical vectors
4. Compute **cosine similarity** between movies
5. Recommend top 5 most similar movies to any given title

---

## How to Run the Project

1. Open `tmdb_movie_recommendation.ipynb` in [Google Colab](https://colab.research.google.com/)
2. Upload the following Kaggle files:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`
3. Run all the cells
4. Call the recommendation function:

```python
recommend("The Dark Knight")
```
---

## Sample Inputs
Try movie titles such as:

```text
recommend("Inception")
recommend("The Godfather")
recommend("Avatar")
recommend("Iron Man")
recommend("Interstellar")
```

> Make sure the movie title matches exactly as in the dataset.


---

## Example Output

```python
recommend("The Dark Knight")
```
```text
Batman Begins
The Dark Knight Rises
Watchmen
V for Vendetta
Man of Steel
```

---

## Possible Extensions
* Add fuzzy matching for partial titles
* Build a Streamlit or Flask app
* Combine with collaborative filtering for a hybrid system
* Deploy with model caching and user input forms

---

## Acknowledgments
Dataset sourced from a Kaggle-hosted GitHub mirror
> Inspired by standard sentiment analysis NLP tutorials

---



## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)


