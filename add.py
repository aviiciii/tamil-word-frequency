import csv

# paths
input_path = 'data/input/4.csv'

output_path = 'data/output/2.csv'

words = []
frequencies = []
words_read = 0

# read output file
with open(output_path, 'r') as csv_file:
    print('reading output file')

    reader = csv.reader(csv_file)

    for row in reader:
        words.append(row[0].strip())
        frequencies.append(row[1].strip())
        words_read += 1

        if words_read % 50000 == 0:
            print(words_read)

print('read output file')


with open(input_path, 'r') as csv_file:
    print('reading input file')
    reader = csv.reader(csv_file)

    for row in reader:
        words_read += 1
        # check if word is in list
        if row[0] in words:
            # get index of word
            index = words.index(row[0])
            # add frequency
            frequencies[index] = int(frequencies[index]) + int(row[1])
        else:
            words.append(row[0])
            frequencies.append(row[1])
        if words_read % 50000 == 0:
            print(words_read)

    

print('read input2')

print('writing to file')
# write to file
with open(output_path, 'w') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['word', 'frequency'])
    for i in range(len(words)):
        writer.writerow([words[i], frequencies[i]])
    
print('done')
