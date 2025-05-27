import requests
import pandas as pd
import time
from requests.exceptions import RequestException
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import os

def get_genre(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            if f"ISBN:{isbn}" in data:
                book_data = data[f"ISBN:{isbn}"]
                subjects = book_data.get("subjects", [])
                return ", ".join([subject["name"] for subject in subjects[:3]])
            return "Genre not found"
        except RequestException:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                return "Error fetching genre"
        except (KeyError, ValueError):
            return "Error processing genre"

def fetch_genre(index, isbn):
    genre = get_genre(isbn)
    return index, genre

# Load your dataset
df = pd.read_csv("/Users/milithakrar/Desktop/Data_Science/Capstone_Project/Book-Recommendations/notebooks/cleaned_data.csv")
top_10000_books = df.sort_values('Total_num_of_ratings', ascending=False).drop_duplicates('Title').head(10000)
top_10000_books["Genre"] = ""

# File paths
output_file = "top_10000_books_with_genre.csv"
index_file = "last_completed_index_10000.txt"
save_every = 100
max_workers = 5

# Determine where to resume
start_idx = 0
if os.path.exists(index_file):
    with open(index_file, "r") as f:
        start_idx = int(f.read().strip()) + 1  # Resume from next index

# Prepare list of records to process
records_to_process = [(idx, row["ISBN"]) for idx, row in top_10000_books.iterrows() if idx >= start_idx]

# Parallel processing with progress bar and periodic saving
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = [executor.submit(fetch_genre, idx, isbn) for idx, isbn in records_to_process]
    completed = 0
    for i, future in enumerate(tqdm(as_completed(futures), total=len(futures), desc="Processing books"), 1):
        idx, genre = future.result()
        top_10000_books.at[idx, "Genre"] = genre
        completed += 1
        # Save every 100 records or at the end
        if completed % save_every == 0 or completed == len(futures):
            top_10000_books.to_csv(output_file, index=False)
            with open(index_file, "w") as f:
                f.write(str(idx))
            print(f"Auto-saved after {completed} records. Last completed index: {idx}")

# Final save
top_10000_books.to_csv(output_file, index=False)
with open(index_file, "w") as f:
    f.write(str(idx))
print(f"Processing complete. Data saved to '{output_file}'. Last completed index: {idx}")
