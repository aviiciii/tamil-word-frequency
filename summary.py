import csv


def count_words_above_frequency(csv_path, n):
    count = 0

    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row

        for row in reader:
            frequency = int(row[1])

            if frequency > n:
                count += 1

    return count

# Example usage
csv_path = 'data/output/filtered/2.csv'  # Replace with your large CSV file path

total_count = count_words_above_frequency(csv_path, 0)
freq5 = count_words_above_frequency(csv_path, 5)
freq100 = count_words_above_frequency(csv_path, 100)
freq1000 = count_words_above_frequency(csv_path, 1000)

print(f'Total count: {total_count}')
print(f'Frequency > 5: {freq5}')
print(f'Frequency > 100: {freq100}')
print(f'Frequency > 1000: {freq1000}')