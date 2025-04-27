import pandas as pd  
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def import_csv(file_path):
    """
    Import CSV data into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.
    """
    data = pd.read_csv(file_path)
    pd.set_option('display.max_rows', None)
    print(f'Successfully imported data from {file_path}')
    return data


def generate_data_dictionary(df):
    """
    Generate a data dictionary.

    Parameters:
        df (pd.DataFrame): The DataFrame.

    Returns:
        pd.DataFrame: Return the data-dictionary for all the columns in the Data-frame.
    """
    df = df.reset_index(drop=True)
    
    books_dict = []

    column_descriptions = {
        "ISBN": "International Standard Book Number, unique identifier for books", 
        "Title": "The title of the book",
        "Author": "The name of the book's author",
        "Ratings": "User's rating of the book, scale of 1-10",
        "Total_num_of_ratings": "Total number of ratings for the book",
        "Avg_ratings": "Average rating score for the book",
        "Avg_ratings_excluding_zero": "Average rating score for the book excluding 0 values",
        "Publisher": "The name of the book's publisher",
        "Publication_year": "The year the book was published",
        "Year_Category": "Categorized time period of publication",
        "User_id": "Unique identifier for each user",
        "Age_Category": "Categorized Age into age ranges",
        "City": "City where the user is located", 
        "State": "State or region where the user is located",
        "Country": "Country where the user is located",
        "Image_URL": "URL link to the book's cover image"
    }

    for column in df.columns:
        books_dict.append({
            'Column Name': column,
            'Data Type': df[column].dtype,
            'Description': column_descriptions.get(column, 'Description not available'),
            'Unique Values': df[column].nunique(),
            'Missing Values': df[column].isnull().sum(),
            'Value Range': (df[column].min(), df[column].max()) if 
            pd.api.types.is_numeric_dtype(df[column]) else 'N/A',
        })

    books_dict_df = pd.DataFrame(books_dict)
    return books_dict_df


def define_df_settings():
    """
    Define the necessary data frame settings.
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)


def custom_tokenizer(text):
    """
    Define the necessary word tokenizer settings with lemmatization.
    """
    forbidden_char = string.punctuation + "1234567890"
    
    # Initialize lemmatizer inside the function
    lemmatizer = WordNetLemmatizer()
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove special characters (including apostrophes)
    text = re.sub(f"[{re.escape(forbidden_char)}]", "", text)  # re.escape fixes regex issues
    
    # Split into words
    tokens = text.split()
    
    # Remove stopwords AND single-character tokens, then apply lemmatization
    tokens = [lemmatizer.lemmatize(tok) for tok in tokens 
              if (tok not in ENGLISH_STOP_WORDS) and (len(tok) > 1)]
    
    return tokens
