data = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 92),
    ("Eve", 85)
]

# Sort the list of tuples based on the score (the second element, index 1)
# The lambda function defines the custom sorting criteria
sorted_by_score = sorted(data, key=lambda item: item[1], reverse=True)

# Sort the list, prioritizing score (index 1) then name (index 0) for tie-breaking
sorted_by_score_then_name = sorted(data, key=lambda item: (item[1], item[0]), reverse=True)

print("--- Custom List Sorting Demo ---")
print("Original Data:", data)
print("-" * 35)
print("Sorted by Score (Descending):")
for item in sorted_by_score:
    print(item)

print("\nSorted by Score, then Name:")
for item in sorted_by_score_then_name:
    print(item)