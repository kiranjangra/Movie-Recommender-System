Movie Recommender System - Content-Based Filtering

* Libraries Used:
               - Pandas
               - NumPy
               - NLTK
               - Scikit-learn

* Dataset Used:
               - tmdb_5000_movies.csv
               - tmdb_5000_credits.csv

* Project Overview:
                  This project implements a content-based movie recommender system using Python. The recommendation system suggests movies based on their content, 
                  utilizing various features like genres, keywords, cast, and crew. Below are the key steps involved in creating the system:
         - Data Merging:
                  The two datasets (tmdb_5000_movies.csv and tmdb_5000_credits.csv) were merged to create a unified dataset.
         - Data Preprocessing:
                  Genres & Keywords: Extracted useful information from the genres and keywords columns.
                  Cast: Retrieved the first three characters from the cast column.
                  Crew: Fetched the director's name from the crew column.
         - Tags Creation:
                  Combined information from the overview, genres, keywords, cast, and crew to create a tags column for each movie. This provided a consolidated textual 
                  representation of each movie's content.
         - Text Processing:
                  Applied the Porter Stemmer to the tags column to reduce words to their base or root form.
                  Used CountVectorizer and TF-IDF Vectorizer to convert the tags into numerical vectors. Only the 5000 most commonly used words were considered, with 
                  stopwords removed to enhance vectorization accuracy.
         - Cosine Similarity Calculation:
                  Calculated the cosine similarity between the vectorized tags to measure the similarity between movies.

* Implementation:
            The final system allows users to input a movie and receive recommendations based on the content similarities calculated from the processed data.

* Web Application Development:
            Used PyCharm to convert the project into a web application.
            Implemented the front-end of the movie recommender system using Streamlit to create an interactive and user-friendly interface.

* Tools Used:
            Jupyter Notebook: For coding and experimenting with the dataset.
            PyCharm: For converting the project into a web application.
            Streamlit: For creating the web-based interface of the recommender system.
            GitHub: To manage and share the project.

This project demonstrates the application of natural language processing and machine learning techniques to build a functional content-based recommendation engine, along with converting it into a deployable web application that includes movie posters fetched via API.
  
