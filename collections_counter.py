from collections import Counter

data_list = [
    "apple", "banana", "apple", "orange", "banana", 
    "apple", "grape", "orange", "banana", "apple"
]

# Create a Counter object from the list
item_counts = Counter(data_list)

print("--- collections.Counter Demo ---")
print(f"All Counts: {item_counts}")

# Find the 3 most common items
most_common_items = item_counts.most_common(3)

print(f"Most common item: {item_counts.most_common(1)[0][0]}")
print(f"Top 3 most common items: {most_common_items}")