import string

def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, '')
        
    # Split the text into a list of words
    words = text.split()
    
    # Use a dictionary to store counts
    word_counts = {}
    
    for word in words:
        # Increment the count for the word, or set it to 1 if first time
        word_counts[word] = word_counts.get(word, 0) + 1
        
    return word_counts

sentence = "Python is great. Python is easy. Python is powerful."
frequency_map = count_words(sentence)

print("--- Word Frequency Counter ---")
for word, count in frequency_map.items():
    print(f"'{word}': {count}")