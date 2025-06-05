import streamlit as st
import pickle
from surprise import dump
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Cache models and data for performance
@st.cache_resource
def load_models():
    with open('../models/book_title_embeddings_updated.pkl', 'rb') as f:
        df = pickle.load(f)
    _, collab_model = dump.load('../models/funkSVD_model.pkl')
    return df, collab_model

df, collab_model = load_models()

# Optional: Initialize user history if you want to use it
# if 'history' not in st.session_state:
#     st.session_state.history = []

def hybrid_recommendation(
    df, collab_model, user_id=None, user_query=None, top_n=10, alpha=0.5, emb_col='Text_emb'
):
    """
    Generate hybrid book recommendations.
    """
    # Map title to ISBN if needed
    if not user_query:
        raise ValueError("Please provide a book title or ISBN as user_query.")
    if user_query in df['ISBN'].values:
        query_isbn = user_query
    else:
        match = df[df['Title'].str.lower() == user_query.lower()]
        if not match.empty:
            query_isbn = match.iloc[0]['ISBN']
        else:
            raise ValueError("Book not found in dataset.")

    # Content-based similarity
    query_vec = df.loc[df['ISBN'] == query_isbn, emb_col].values[0].reshape(1, -1)
    all_vecs = list(df[emb_col])
    cos_sims = cosine_similarity(query_vec, all_vecs).flatten()
    df['content_score'] = cos_sims

    # Collaborative filtering (if user_id provided)
    if user_id:
        df['collab_score'] = df['ISBN'].apply(lambda x: collab_model.predict(int(user_id), x).est)
    else:
        df['collab_score'] = 0

    # Normalize scores
    scaler = MinMaxScaler()
    if user_id:
        df[['content_score', 'collab_score']] = scaler.fit_transform(df[['content_score', 'collab_score']])
        df['hybrid_score'] = alpha * df['collab_score'] + (1 - alpha) * df['content_score']
    else:  # Content-only mode
        df['hybrid_score'] = df['content_score']

    # Filter out history (optional)
    # df = df[~df['ISBN'].isin(st.session_state.history)]

    # Show top recommendations (include Image_URL)
    result = df.sort_values('hybrid_score', ascending=False)
    return result[['Title', 'Author', 'Genre', 'Image_URL', 'hybrid_score']].head(top_n)

# Streamlit UI
st.title("Book Recommender")
st.markdown("""
Welcome to the Book Recommender!

Discover new books tailored to your tastes.  
This app uses both your favorite books and your reading history (if available) to suggest titles you'll love.  
Select a book you like below, and get personalized recommendations!
""")
# Search-as-you-type for book title
user_query_input = st.text_input("Search Book Title", help="Start typing to see matching titles")
matching_titles = [title for title in df['Title'].unique() if user_query_input.lower() in title.lower()]
if matching_titles:
    user_query = st.selectbox("Select from matches", matching_titles)
else:
    user_query = user_query_input

# User ID input
user_id = st.text_input("Enter User ID (optional)")

# Set fixed values for alpha and top_n
ALPHA = 0.8
TOP_N = 10

# When button is pressed
if st.button("Recommend Me Some Books"):
    try:
        recommendations = hybrid_recommendation(
            df, collab_model,
            user_id=user_id if user_id else None,
            user_query=user_query,
            top_n=TOP_N,
            alpha=ALPHA
        )
        for _, row in recommendations.iterrows():
            # Use columns for better layout
            col1, col2 = st.columns([1, 4])
            with col1:
                if 'Image_URL' in row and pd.notnull(row['Image_URL']) and isinstance(row['Image_URL'], str):
                    try:
                        st.image(row['Image_URL'], width=120)
                    except:
                        st.write("Could not load image.")
                else:
                    st.write("No book cover available.")
            with col2:
                st.markdown(f"**{row['Title']}**")
                st.write(f"**Author:** {row['Author']}")
                st.write(f"**Genre:** {row['Genre']}")
            st.write("---")
            # Optional: Add to session state history
            # st.session_state.history.append(row['ISBN'])
    except Exception as e:
        st.error(str(e))

