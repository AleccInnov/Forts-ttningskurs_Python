# sortera med ord

def custom_key(word):
    # Gör en egen sortering här baserat på antalet vokaler
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

words = ["banana", "apple", "cat", "dog", "mongoose"]
sorted_words = sorted(words, key=custom_key)

print(sorted_words)
