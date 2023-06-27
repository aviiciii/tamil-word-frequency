import csv
import os

def main():
    """
    Sorting
    Create top csv files
    Create summary md file
    """

    # Version
    version = 3

    # Sort the file
    sort(version)

    # Call function to create top csv files
    no_of_rows = (100, 250, 500, 1000, 5000, 10000)
    for n in no_of_rows:
        top(n, version)

    # Call function to create summary md file (only do if directory exists)
    summary(version)


# SORT FUNCTIONS
def sort(version):
    # paths
    csv_path = f'data/output/{version}.csv'
    output_path = f'data/output/filtered/{version}.csv'

    # Read the CSV file into a list of dictionaries
    data = []
    with open(csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)

    # Sort the data based on the 'frequency' column
    sorted_data = sorted(data, key=lambda x: int(x['frequency']), reverse=True)

    # Write the sorted data to a new CSV file

    fieldnames = ['word', 'frequency']  # Assuming the column names are 'word' and 'frequency'

    with open(output_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_data)

    print("Sorting completed. Sorted file saved at:", output_path)


# TOP FUNCTIONS
def top(no_of_rows, version):

    # paths
    input_path = f'data/output/filtered/{version}.csv'

    output_dir = f'output/v{version}'
    output_path = f'{output_dir}/top_{no_of_rows}.csv'

    # check if output folder exists
    if not os.path.exists(output_dir):
        os.makedirs(f'output/v{version}')
        print("The new directory is created!")

    # Call function
    rows = read_n_rows(input_path, no_of_rows)

    # Save to csv file
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow([row[0], row[1]])

    print(f'Summary: {len(rows)} rows saved to {output_path}')

def read_n_rows(file_path, n):
    rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= n:
                break
            rows.append(row)
    return rows


# SUMMARY FUNCTIONS
def summary(version):
    summary = {}

    summary['total_count'] = count_words_above_frequency(version, 0)
    summary['freq5'] = count_words_above_frequency(version, 5)
    summary['freq100'] = count_words_above_frequency(version, 100)
    summary['freq1000'] = count_words_above_frequency(version, 1000)

    # Create a md file
    with open(f'output/v{version}/summary.md', 'w') as file:
        summary_text = f'# Summary\n\nTotal count of words: {summary["total_count"]}\n\nFrequency > 5: {summary["freq5"]}\n\nFrequency > 100: {summary["freq100"]}\n\nFrequency > 1000: {summary["freq1000"]}'
        file.write(summary_text)

def count_words_above_frequency(version, n):

    # paths
    csv_path = f'data/output/filtered/{version}.csv'

    count = 0

    with open(csv_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row

        for row in reader:
            frequency = int(row[1])

            if frequency > n:
                count += 1

    return count


if __name__ == '__main__':
    main()