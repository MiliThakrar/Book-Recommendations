# Book Recommendation System

#### Author: Mili Ketan Thakrar  
#### Date: February 21, 2025  
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
- Implementation of collaborative filtering algorithms
- Development of content-based filtering techniques
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

## 3. Project Workflow

1. **Data Collection**:  
   - Download dataset from Kaggle.

2. **Data Preprocessing**:  
   - Handle missing values, clean data, and normalize text.

3. **Exploratory Data Analysis**:  
   - Analyze reading patterns and book popularity.
   - Identify challenges like data sparsity or cold start problems.
   - Explore distributions of ratings, users, and books.

4. **NLP for Book Titles**:  
   - Apply NLP techniques to extract meaningful features from book titles.
   - Techniques include:
     - Tokenization
     - Keyword Extraction
     - TF-IDF
   - These features will enhance content-based filtering.

5. **Initial Model Development**:  
   - Implement collaborative filtering algorithms.
   - Develop content-based filtering using extracted features.

6. **Hybrid Model Integration**:  
   - Combine collaborative and content-based approaches.
   - Experiment with different weighting schemes.

7. **Evaluation Metric Selection**:  
   - Use metrics like RMSE, MAP@K, or diversity measures.

8. **Advanced Modeling**:  
   - Refine hybrid models.
   - Explore matrix factorization techniques.
   - Address cold start problems.

9. **User Interface Development**:  
   - Create a simple interface to demonstrate recommendations.

10. **Testing and Optimization**:  
    - Conduct user testing.
    - Gather feedback on recommendation relevance.
    - Fine-tune models based on performance.

## 4. Repository Navigation

[To be completed as the project progresses]

## 5. Setup

All necessary packages are included in the environment file `book_recommendation_env.yml`.
