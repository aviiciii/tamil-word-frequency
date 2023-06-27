import nltk
import ssl
import csv

# SSL certificate error fix
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.stem import WordNetLemmatizer
from collections import defaultdict
nltk.download('punkt')
nltk.download('wordnet')

version = 3

with open(f'data/input/v{version}/pre.txt', 'r', encoding='latin-1') as f:
    text = f.read()
print("File read successfully.")

# Tokenize the text using nltk
words = nltk.word_tokenize(text)
print("Text tokenized successfully.")

# Initialize the WordNetLemmatizer for Tamil
lemmatizer = WordNetLemmatizer()
print("Lemmatizer initialized successfully.")

# Normalize and lemmatize the words
normalized_words = (lemmatizer.lemmatize(word) for word in words)
print("Words normalized and lemmatized successfully.")

# Count the frequencies using a defaultdict
word_freq = defaultdict(int)
for word in normalized_words:
    word_freq[word] += 1
print("Word frequencies counted successfully.")

# Sort the dictionary in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print("Word frequencies sorted successfully.")

# Write the output to a CSV file
output_path = f'data/output/{version}.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['word', 'frequency'])
    writer.writerows(sorted_word_freq)
print("Output written to CSV file successfully.")

