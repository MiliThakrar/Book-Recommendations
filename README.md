# Book Recommendation System

#### Author: Mili Ketan Thakrar  
#### Date: TBD  
#### Product Demo: [To be completed as the project progresses]  
#### Dataset link: [Kaggle Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)  

## 1. Project Overview

### Problem Area
Readers often struggle to find new titles that match their interests, leading to decreased engagement with reading. This project aims to develop a sophisticated book recommendation system using a hybrid approach that combines collaborative filtering and content-based filtering techniques to analyze user ratings, reading history, and book metadata, providing personalized recommendations.

### Those Affected
- Readers seeking new books aligned with their preferences
- Libraries and bookstores looking to improve customer engagement
- Publishers aiming to increase book discoverability

### Proposed Data Science Solution
We will create a hybrid recommendation engine that combines collaborative filtering and content-based filtering, suggesting relevant books based on user preferences and book features. The project will involve:

- Data collection and preprocessing
- Exploratory data analysis
- Implementation of content-based filtering techniques
- Implementation of collaborative filtering algorithms
- Integration of both approaches into a hybrid model
- Evaluation and optimization of the recommendation system

### Impact of the Solution
By providing personalized recommendations, we aim to:
- Increase reader engagement and satisfaction
- Help readers discover new authors and genres
- Boost book sales and library circulation
- Improve recommendation accuracy and diversity

## 2. Data Information

#### Books Table

| Field Name | Type | Description |
|------------|------|-------------|
| ISBN | string | Unique identifier for books |
| Title | string | The title of the book |
| Author | string | The name of the author |
| Publisher | string | The name of the publisher |
| Publication_year | int | The year published |
| Image_URL | string | URL link to the cover image |

#### Ratings Table

| Field Name | Type | Description |
|------------|------|-------------|
| User_id | float | Unique identifier for each user |
| ISBN | string | ISBN of the rated book |
| Ratings | float | User's rating (1-10) |

#### Users Table

| Field Name | Type | Description |
|------------|------|-------------|
| User_id | float | Unique identifier for each user |
| Age | float | Age of the user |
| Location | string | User's location |

# Book Recommendation System

## 3. Project Workflow (Revised)

1. **Data Collection**:
   - Download dataset from Kaggle.

2. **Data Preprocessing**:
   - Handle missing values, clean data, and normalize text.

3. **Exploratory Data Analysis**:
   - Analyze reading patterns and book popularity.
   - Identify challenges like data sparsity or cold start problems.
   - Explore distributions of ratings, users, and books.

4. **Baseline Modeling**:
   - **Content-Based Filtering**:
     - Implement TF-IDF vectorization of book titles/authors
     - Compute cosine similarity between book features
     - Generate recommendations based on feature similarity
   - **Logistic Regression**:
     - Predict user preferences based on book metadata
     - Establish baseline performance metrics

5. **NLP and Word Embeddings**:
   - Utilize GloVe pretrained word embeddings for title analysis
   - Download GloVe embeddings from [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/) (glove.6B.zip recommended)
   - Combine with cosine similarity for enhanced content-based recommendations

6. **Advanced Modeling**:
   - **Collaborative Filtering**:
     - Implement user-item matrix factorization
     - Develop neighborhood-based recommendation algorithms
   - **Hybrid Approach**:
     - Combine content-based and collaborative filtering outputs
     - Implement weighted hybrid recommendation engine
     - Experiment with stacking ensemble methods

7. **Evaluation Metric Selection**:
   - Use metrics like RMSE, MAP@K, and diversity measures

8. **Model Refinement**:
   - Address cold start problems using content features
   - Implement matrix factorization with implicit feedback
   - Optimize hyperparameters using grid search

9. **User Interface Development**:
   - Create recommendation demonstration interface
   - Implement basic search and recommendation display


## 4. Repository Navigation
[To be completed as the project progresses]

## 5. Setup
All necessary packages are included in `book_recommendation_env.yml`.

