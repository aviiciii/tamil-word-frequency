import nltk
import ssl
import csv

# ssl certificate error fix
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

version = 2

# Read file
with open(f'data/input/v{version}/data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize the text using nltk
words = nltk.word_tokenize(text)

# Initialize the WordNetLemmatizer for Tamil
lemmatizer = WordNetLemmatizer()

# Normalize and lemmatize the words
normalized_words = [lemmatizer.lemmatize(word) for word in words]

# Count the frequencies using a dictionary
count=0
word_freq = {}
for word in normalized_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

    if count%1000 == 0:
        print(count)
    count+=1
    
# Sort the dictionary in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Write the output as a csv file
with open(f'data/output/{version}.csv', 'w', encoding='utf-8') as csv:
    csv.write('word,frequency\n')
    for word, freq in sorted_word_freq:
        csv.write(word + ',' + str(freq) + '\n')
