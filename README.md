# Book Recommendation System

#### Author: Mili Ketan Thakrar
#### Date: TBD
#### Product Demo: [To be completed as the project progresses]
#### Dataset link: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

## 1. Project Overview

### Problem Area
With the vast number of books available, readers often struggle to find new titles that match their interests, leading to decreased engagement with reading. This project aims to develop a sophisticated book recommendation system using a hybrid approach that combines collaborative filtering and content-based filtering techniques to analyze user ratings, reading history, and book metadata, providing personalized book recommendations to enhance the reading experience for users.

### Those Affected
- Readers seeking new books aligned with their preferences
- Libraries and bookstores looking to improve customer engagement
- Publishers aiming to increase book discoverability

### Proposed Data Science Solution
We will create a hybrid recommendation engine that combines collaborative filtering and content-based filtering, which will suggest relevant books to users based on their past preferences, similarities with other users, and book content features. The project will involve:

- Data collection and preprocessing
- Exploratory data analysis
- Implementation of collaborative filtering algorithms
- Development of content-based filtering techniques
- Integration of both approaches into a hybrid model
- Evaluation and optimization of the recommendation system

### Impact of the Solution
By providing personalized book recommendations, we aim to:

- Increase reader engagement and satisfaction
- Help readers discover new authors and genres
- Potentially boost book sales and library circulation
- Improve recommendation accuracy and diversity

## 2. Data Information

#### Books Table

| Field Name | Type | Description |
|------------|------|-------------|
| ISBN | string | International Standard Book Number, unique identifier for books |
| Title | string | The title of the book |
| Author | string | The name of the book's author |
| Publisher | string | The name of the book's publisher |
| Publication_year | int | The year the book was published |
| Image_URL | string | URL link to the book's cover image |

#### Ratings Table

| Field Name | Type | Description |
|------------|------|-------------|
| User_id | float | Unique identifier for each user |
| ISBN | string | International Standard Book Number of the rated book |
| Ratings | float | User's rating of the book, scale of 1-10 |

#### Users Table

| Field Name | Type | Description |
|------------|------|-------------|
| User_id | float | Unique identifier for each user |
| Age | float | Age of the user |
| Location | string | Location where the user is located |

## 3. Project Workflow

1. Data Collection:
   - Download dataset from Kaggle

2. Data Preprocessing:
   - Handle missing values
   - Clean and normalize the dataset
   - Extract relevant features for content-based filtering

3. Exploratory Data Analysis:
   - Analyze user reading patterns and book popularity distributions
   - Identify potential challenges such as data sparsity or cold start problems
   - Explore book content features for content-based filtering

4. Initial Model Development:
   - Implement basic collaborative filtering algorithm
   - Develop content-based filtering using book features

5. Hybrid Model Integration:
   - Combine collaborative and content-based approaches
   - Experiment with different weighting schemes for the hybrid model

6. Evaluation Metric Selection:
   - Determine appropriate metrics (e.g., RMSE, MAP@K, diversity measures)

7. Advanced Modeling:
   - Refine hybrid model
   - Explore matrix factorization techniques
   - Address cold start problems and improve recommendation diversity

8. User Interface Development:
   - Create a simple interface to demonstrate the recommendation system

9. Testing and Optimization:
   - Conduct user testing
   - Gather feedback on recommendation relevance and system usability
   - Fine-tune the hybrid model based on performance and user feedback

## 4. Repository Navigation

[To be completed as the project progresses]

## 5. Setup

I've included all the appropriate packages needed to be installed in the environment file book_recommendation_env.yml
