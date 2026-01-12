import pandas as pd
from typing import List, Dict

# Global DataFrame
_quotes_df = None

def load_data():
    global _quotes_df
    if _quotes_df is None:
        try:
            print("Loading quotes dataset...")
            _quotes_df = pd.read_json("hf://datasets/Abirate/english_quotes/quotes.jsonl", lines=True)
            print(f"Loaded {_quotes_df.shape[0]} quotes.")
        except Exception as e:
            print(f"Error loading dataset: {e}")
            _quotes_df = pd.DataFrame(columns=["quote", "author", "tags"])

def search_quotes(query: str) -> List[Dict]:
    global _quotes_df
    if _quotes_df is None:
        load_data()
    
    if not query:
        # Return 10 random quotes if no query
        if _quotes_df.empty:
            return []
        return _quotes_df.sample(n=min(10, len(_quotes_df))).to_dict(orient="records")

    # Filter Case Insensitive
    mask = (
        _quotes_df['quote'].str.contains(query, case=False, na=False) | 
        _quotes_df['author'].str.contains(query, case=False, na=False) |
        _quotes_df['tags'].apply(lambda x: any(query.lower() in t.lower() for t in x) if isinstance(x, list) else False)
    )
    
    results = _quotes_df[mask].head(20) # Limit to 20
    return results.to_dict(orient="records")
