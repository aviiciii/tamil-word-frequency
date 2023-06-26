import nltk
import ssl
import re

# ssl certificate error fix
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')


with open('data/cleaned_tamil.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text using nltk
words = nltk.word_tokenize(text)

# Initialize the WordNetLemmatizer for Tamil
lemmatizer = WordNetLemmatizer()

# Normalize and lemmatize the words
normalized_words = [lemmatizer.lemmatize(word) for word in words]

# Count the frequencies using a dictionary
word_freq = {}
for word in normalized_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the dictionary in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Write the output to a dictionary file
with open('data/output.txt', 'w', encoding='utf-8') as f:
    for word, freq in sorted_word_freq:
        f.write(f'{freq}: {word}\n')

