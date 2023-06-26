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


# Sample Tamil text
text = "உலகம் மிகப்பெரிய தடைகள் அடைந்துள்ளது. இது திரையை புதுப்பிக்க தடை எடுத்துவிடுகிறது."

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

# Print the word frequencies
for word, freq in word_freq.items():
    print(word, freq)


def clean_text(text):
    # Remove punctuations
    text = re.sub(r'[^\w\s]', '', text)

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove English characters
    text = re.sub(r'[A-Za-z]+', '', text)