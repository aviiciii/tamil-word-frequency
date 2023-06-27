import nltk
import re
import io



def remove_unusual_line_terminators(filepath):
    with io.open(filepath, 'r', newline='', encoding='utf-8') as file:
        text = file.read()

    # Remove unusual line terminators
    text = text.replace('\r', '').replace('\x0b', '').replace('\x0c', '')

    with io.open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Unusual line terminators removed. Output saved at: {filepath}")

def main():
    """
    Remove English words, numbers and emojis from the raw text (.txt files)
    """
    
    filename = 'data/input/v3/raw.txt'

    remove_unusual_line_terminators(filename)

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    print("File read")

    # Tokenize the text using nltk
    text = nltk.word_tokenize(text)
    print("Text tokenized")

    # Clean the text
    text = clean_text(text)
    text = remove_english_words(text)
    text = remove_emoji(text)


    # save the cleaned text
    with open('data/input/v3/pre.txt', 'w') as f:
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