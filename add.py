import csv

# 1, 2, 3 done

# paths
input1 = 'data/input/4.csv' # smaller file
input2 = 'data/input/5.csv' # larger file

output_path = 'data/output/2_a.csv' # output file

words = []
frequencies = []
words_read = 0

# read output file
with open(input1, 'r') as csv_file:
    print('Reading input1... ', end='')

    reader = csv.reader(csv_file)

    for row in reader:
        words.append(row[0].strip())
        frequencies.append(row[1].strip())
        words_read += 1

        if words_read % 10000 == 0:
            print("#", end='')

print(f'\nCompleted. Words read: {words_read}')
words_read = 0

with open(input2, 'r') as csv_file:
    print('Reading input2... ', end='')
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
        if words_read % 10000 == 0:
            print("#", end='')

print(f'\nCompleted. Words read: {words_read}')

    
print('Writing to file... ', end='')
# write to file
with open(output_path, 'w') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['word', 'frequency'])
    for i in range(len(words)):
        writer.writerow([words[i], frequencies[i]])
    
print('Done!')
