# Book Recommendation System

#### Author: Mili Ketan Thakrar

#### Date: TBD

#### Product Demo: [To be completed as the project progresses]

#### Dataset link: https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

## 1. Project Overview

### Problem Area
With the vast number of books available, readers often struggle to find new titles that match their interests, leading to decreased engagement with reading. This project aims to develop a sophisticated book recommendation system using collaborative filtering techniques to analyze user ratings, reading history, and book metadata, providing personalized book recommendations to enhance the reading experience for users.

### Those Affected
- Readers seeking new books aligned with their preferences
- Libraries and bookstores looking to improve customer engagement
- Publishers aiming to increase book discoverability

### Proposed Data Science Solution
We will create a recommendation engine using collaborative filtering, which will suggest relevant books to users based on their past preferences and similarities with other users. The project will involve:
1. Data collection and preprocessing
2. Exploratory data analysis
3. Implementation of collaborative filtering algorithms
4. Evaluation and optimization of the recommendation system

### Impact of the Solution
By providing personalized book recommendations, we aim to:
- Increase reader engagement and satisfaction
- Help readers discover new authors and genres
- Potentially boost book sales and library circulation

## 2. Data Information

### Brief Description
The dataset is from the Book-Crossing collection, compiled by Cai-Nicolas Ziegler. It contains 278,858 users providing 1,149,780 ratings for 271,379 books.

### Data Dictionary
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

3. Exploratory Data Analysis:
   - Analyze user reading patterns and book popularity distributions
   - Identify potential challenges such as data sparsity or cold start problems

4. Initial Model Development:
   - Implement basic collaborative filtering algorithm
   - Explore both user-based and item-based collaborative filtering methods

5. Evaluation Metric Selection:
   - Determine appropriate metrics (e.g., RMSE, MAP@K)

6. Advanced Modeling:
   - Refine collaborative filtering model
   - Explore matrix factorization techniques
   - Address cold start problems and improve recommendation diversity

7. User Interface Development:
   - Create a simple interface to demonstrate the recommendation system

8. Testing and Optimization:
   - Conduct user testing
   - Gather feedback on recommendation relevance and system usability

## 4. Repository Navigation

[To be completed as the project progresses]

## 5. Setup

I've included all the appropriate packages needed to be installed in the environment file book_recommendation_env.yml
