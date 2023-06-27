import csv
import re
import csv
import string

filtered_words = []
filtered_frequencies = []

total_length = 0
filtered_length = 0

# Open the CSV file
with open('data/filtered_punc.csv', 'r+') as file:
    reader = csv.reader(file)
    
    header = next(reader)  # Skip the header row

    words = []
    frequencies = []
    # Iterate over each row in the CSV file
    for row in reader:
        word = row[0]
        frequency = row[1]
        total_length += 1
        
        # Check if the word is non-English and non-punctuation
        if not re.match(r'[a-zA-Z]+', word) and not all(char in string.punctuation for char in word):
            
            # check if first character is a punctuation
            if word[0] in string.punctuation:
                word = word[1:]  # remove the punctuation
                if word == '':
                    continue

            filtered_words.append(word)
            filtered_frequencies.append(frequency)
            filtered_length += 1
           
        else:
            print(word, frequency)
        
        # updates
        # if total_length % 100000 == 0:
        #     print('Processed {} words'.format(total_length))


# save the filtered words and frequencies to a new csv file
with open('data/filtered_punc.csv', 'w') as file:
    writer = csv.writer(file)
    # header
    writer.writerow(['word', 'frequency'])
    for word, frequency in zip(filtered_words, filtered_frequencies):
        writer.writerow([word, frequency])
    
# result
print('Total words: ', total_length)
print('Filtered words: ', total_length - filtered_length)