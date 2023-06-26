import nltk
import ssl

# ssl certificate error fix
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

# Read file
with open('data/cleaned_tamil.txt', 'r', encoding='utf-8') as f:
    print('Reading the file... ', end='')
    text = f.read()
    print('Done!')

# Tokenize the text using nltk
print('Tokenizing the text... ', end='')
words = nltk.word_tokenize(text)
print('Done!')

# Initialize the WordNetLemmatizer for Tamil
print('Initializing the WordNetLemmatizer... ', end='')
lemmatizer = WordNetLemmatizer()
print('Done!')

# Normalize and lemmatize the words
print('Normalizing and lemmatizing the words... ', end='')
normalized_words = [lemmatizer.lemmatize(word) for word in words]
print('Done!')

# Count the frequencies using a dictionary
print('Counting the frequencies... ')
i=0
word_freq = {}
for word in normalized_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
    if i%1000 == 0:
        print(f'Processed {i} words...')
    i+=1
print('Done!')
    
print('Sorting... ', end='')
# Sort the dictionary in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print('Done!')

# Write the output as a key value pair
print('Writing the output... ', end='')
with open('data/output.txt', 'w', encoding='utf-8') as f:
    for word, freq in sorted_word_freq:
        f.write(f'{freq}: {word}\n')
print('Done!')

