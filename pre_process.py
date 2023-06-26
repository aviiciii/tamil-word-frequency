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

def remove_emoji(words):
    # Define a regular expression pattern to match emojis
    emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+'

    # Filter out emojis
    non_emoji_words = [word for word in words if not re.match(emoji_pattern, word)]
    return non_emoji_words

def main():
    # Sample Tamil text
    # text = " slkdfj உலகம் test மிகப்பெரிய தடைகள் y not ? அடைந்துள்ளது. இது திரையை ehlp புதுப்பிக்க தடை எடுத்துவிடுகிறது."
    
    filename = 'data/raw.txt'

    with open(filename, 'r') as f:
        print('Reading file: {}'.format(filename))
        text = f.read()
        print('File read successfully')



    # Tokenize the text using nltk
    text = nltk.word_tokenize(text)
    print('Tokenization done')

    # Clean the text
    text = clean_text(text)
    print('Cleaning done')
    text = remove_english_words(text)
    print('English words removed')
    text = remove_emoji(text)
    print('Emojis removed')

    # print(text)

    # save the cleaned text
    with open('data/cleaned_tamil.txt', 'w') as f:
        print('Writing to file: data/cleaned_tamil.txt')
        f.write(' '.join(text))
        print('File written successfully')

if __name__ == '__main__':
    main()
