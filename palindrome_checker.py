def is_palindrome(text):
    # Normalize the string: remove spaces and convert to lowercase
    normalized_text = "".join(text.split()).lower()
    
    # Check if the string is equal to its reverse
    # [::-1] is the Python slicing shortcut for reversal
    return normalized_text == normalized_text[::-1]

word1 = "level"
word2 = "Python"
phrase1 = "A man a plan a canal Panama"

print("--- Palindrome Checker ---")
print(f"'{word1}' is a palindrome: {is_palindrome(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome(word2)}")
print(f"'{phrase1}' is a palindrome: {is_palindrome(phrase1)}")