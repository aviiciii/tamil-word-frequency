import nltk
import re

def clean_text(words):
    # Remove numbers
    words = [re.sub(r'\d+', '', word) for word in words]
    return words

def remove_english_words(words):
    # Define a regular expression pattern to match English words
    english_word_pattern = r'[A-Za-z]+'

    # Filter out English words
    non_english_words = [word for word in words if not re.match(english_word_pattern, word)]
    return non_english_words

def main():
    # Sample Tamil text
    # text = " slkdfj உலகம் test மிகப்பெரிய தடைகள் y not ? அடைந்துள்ளது. இது திரையை ehlp புதுப்பிக்க தடை எடுத்துவிடுகிறது."
    
    # Tokenize the text using nltk
    text = nltk.word_tokenize(text)

    # Clean the text
    text = clean_text(text)
    text = remove_english_words(text)
    
    print(text)

if __name__ == '__main__':
    main()
