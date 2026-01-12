from src.models import load_data, search_quotes
import time

print("Starting verification...")
start = time.time()
load_data()
print(f"Data loaded in {time.time() - start:.2f}s")

print("Testing Search 'wisdom'...")
results = search_quotes("wisdom")
print(f"Found {len(results)} quotes for 'wisdom'")
if len(results) > 0:
    print(f"Sample: {results[0]['quote']} - {results[0]['author']}")

print("Verification Complete.")
