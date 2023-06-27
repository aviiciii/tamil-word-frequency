import csv
from collections import defaultdict

# Paths
input1 = 'data/output/1.csv'  # smaller file
input2 = 'data/output/2.csv'  # larger file
output_path = 'data/output/2.csv'  # output file

word_freq = defaultdict(int)  # Dictionary to store word frequencies

# Read input1
print('Reading input1... ', end='')
with open(input1, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        word = row['word'].strip()
        freq = int(row['frequency'])
        word_freq[word] += freq
print('Completed.')
print(len(word_freq))

# Read input2
print('Reading input2... ', end='')
with open(input2, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        word = row['word'].strip()
        freq = int(row['frequency'])
        word_freq[word] += freq
print('Completed.')
print(len(word_freq))

# Write to file
print('Writing to file... ', end='')
with open(output_path, 'w', newline='') as csv_file:
    fieldnames = ['word', 'frequency']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for word, freq in word_freq.items():
        writer.writerow({'word': word, 'frequency': freq})
print('Done!')
