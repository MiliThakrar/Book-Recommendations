# Book Recommendation System

**Author:** Mili Ketan Thakrar

**Date:** June 2025

**Dataset:** [Kaggle Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

**Live Demo:** [Try the Streamlit App](https://book-recommendations-r8wirca.streamlit.app/)


## ✨ Executive Summary

In a world overflowing with reading options, identifying the next great read remains a challenge for book lovers. This project develops a **hybrid book recommendation system** that combines content-based filtering with matrix factorization (FunkSVD). By leveraging user ratings, book metadata, genre information, and textual features, the system provides personalized suggestions that enhance reader satisfaction, promote exploration, and support the publishing ecosystem.

The final solution addresses the **cold start problem**, balances **accuracy with diversity**, and can be adapted for commercial use by **libraries, bookstores, or digital reading platforms**.


## 🔗 Problem Statement

Many readers struggle to find books that align with their tastes, particularly when entering new genres or platforms. This leads to missed opportunities for engagement. Our goal is to:

* Recommend books based on **user behavior and content similarity**.
* Tackle challenges like **data sparsity**, **cold starts**, and **rating inconsistencies**.
* Provide a solution that works at scale and across user demographics.


## 📑 Dataset Overview

The project uses three core tables:

### ✉️ Books Table

| Field      | Description            |
| ---------- | ---------------------- |
| ISBN       | Unique book identifier |
| Title      | Book name              |
| Author     | Book author            |
| Publisher  | Publisher name         |
| Year       | Year of publication    |
| Image\_URL | Book cover image URL   |

### ⭐ Ratings Table

| Field   | Description            |
| ------- | ---------------------- |
| User ID | Unique user identifier |
| ISBN    | Book identifier        |
| Rating  | Score (1–10)           |

### 👤 Users Table

| Field    | Description            |
| -------- | ---------------------- |
| User ID  | Unique user identifier |
| Age      | User age               |
| Location | Geographical info      |


## 📊 Key Steps & Methodology

### 1. Data Wrangling & Cleaning

* Merged the three datasets and removed nulls, duplicates, and incorrect ISBNs.
* Standardized text formats (e.g., title casing, punctuation removal).

### 2. Exploratory Data Analysis (EDA)

* Visualized rating distribution (skewed toward 8–10).
* Identified top-rated books and frequently rated titles.
* Analyzed age distributions and geographic spread of users.

### 3. Content-Based Filtering

* Applied **TF-IDF vectorization** on book titles.
* Used **cosine similarity** to recommend books based on textual metadata.
* Integrated **GloVe embeddings** to enhance semantic understanding of titles.
* **Enriched book metadata** by fetching genre information via an open-source book genre API to improve similarity matching.

### 4. Collaborative Filtering with FunkSVD

* Constructed a user-item matrix.
* Data filtering (users with >200 ratings and books with >50 reviews) was applied to improve model robustness.
* Implemented **FunkSVD** (a matrix factorization technique) to model latent user-book interactions.
* Tuned hyperparameters including number of latent features, learning rate, and iterations.
* Final model evaluation was performed on the test set.

### 5. Hybrid Recommendation Strategy

* Combined normalized scores from content-based and FunkSVD models.
* Used weighted averaging to generate final ranked recommendations.
* Ensured fallback mechanism to use content-based scores for new users/books (cold start).

### 6. Evaluation & Metrics

**RMSE (Root Mean Square Error)** was the primary evaluation metric:

| Model Type        | RMSE Score |
| ----------------- | ---------- |
| FunkSVD           | 3.2648     |
| Hybrid (Weighted) | 3.6262     |

While FunkSVD performed better in terms of RMSE, the hybrid model ensures better diversity and cold start handling.


Here's an updated version of your README with a clear mention that the model `.pkl` files are hosted on your S3 bucket, seamlessly integrated into the relevant sections:

---

## 🤝 Final Outcomes

* Successfully implemented a hybrid book recommender system.
* Addressed cold start problem using semantic content analysis and genre metadata.
* Delivered personalized recommendations without requiring heavy computational infrastructure.
* **Model artifacts (e.g., FunkSVD and word embedding `.pkl` files) are hosted on an AWS S3 bucket** and dynamically accessed by the Streamlit application during runtime.


## 🚀 Deployment & Next Steps

* A **Streamlit application** has been developed to demonstrate the recommendation system with an interactive UI.
* The app **pulls pre-trained model files from a secure S3 bucket**, ensuring lightweight deployment without bundling large files.

**▶ Try it here:** [https://book-recommendations-r8wirca.streamlit.app/](https://book-recommendations-r8wirca.streamlit.app/)


### Future Enhancements:

* Fine-tune hybrid weights based on user feedback.
* Experiment with contextual recommendations (e.g., time of day, mood, seasonality).

## 📂 Repository Structure

```
.
├── Data/               # All datasets and Python data wrangling scripts
├── Notebooks/          # Jupyter Notebooks
├── Models/             # Saved model files (e.g., .pkl)
├── Slides/             # Presentation decks
├── Doc/                # Initial idea and planning documents
├── Streamlit/          # Streamlit app (.py) for interactive demo
├── .gitignore
├── book_recommendation_env.yml
└── README.md
```

## 🚪 Setup Instructions

1. Clone this repository.

2. Create the environment:

   ```bash
   conda env create -f book_recommendation_env.yml
   conda activate book_recommendation
   ```

3. Run notebooks in sequence.

4. To launch the Streamlit app:

   ```bash
   cd Streamlit
   streamlit run Recommender.py
   ```

Alternatively, use the hosted version here:
👉 [https://book-recommendations-r8wirca.streamlit.app/](https://book-recommendations-r8wirca.streamlit.app/)

## 📄 License & Credits

* **Dataset:** Kaggle Book Recommendation Dataset
* **Embeddings:** [GloVe](https://nlp.stanford.edu/projects/glove/)
* **Genre Metadata:** Open-source Book Genre API

## 📢 Connect

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/mili-ketan-thakrar) or reach out via email for collaborations or questions!


