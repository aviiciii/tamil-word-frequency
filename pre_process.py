import nltk
import re

def main():
    """
    Remove English words, numbers and emojis from the raw text (.txt files)
    """
    
    filename = 'data/raw.txt'

    with open(filename, 'r') as f:
        text = f.read()

    # Tokenize the text using nltk
    text = nltk.word_tokenize(text)

    # Clean the text
    text = clean_text(text)
    text = remove_english_words(text)
    text = remove_emoji(text)


    # save the cleaned text
    with open('data/cleaned_tamil.txt', 'w') as f:
        f.write(' '.join(text))

    print("Text cleaned")


def clean_text(words):
    # Remove numbers
    words = [re.sub(r'\d+', '', word) for word in words]
    print("Numbers removed")

    return words


def remove_english_words(words):
    # Define a regular expression pattern to match English words
    english_word_pattern = r'[A-Za-z]+'

    # Filter out English words
    non_english_words = [word for word in words if not re.match(english_word_pattern, word)]
    print("English words removed")

    return non_english_words

def remove_emoji(words):
    # Define a regular expression pattern to match emojis
    emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+'

    # Filter out emojis
    non_emoji_words = [word for word in words if not re.match(emoji_pattern, word)]
    print("Emojis removed")

    return non_emoji_words


if __name__ == '__main__':
    main()