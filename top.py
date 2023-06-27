import csv

def main():
    # Variables (set here)
    no_of_rows = 5000
    version = 1

    # paths
    input_path = f'data/output/filtered/{version}.csv'
    output_path = f'output/v{version}/top_{no_of_rows}.csv'

    # Call function
    rows = read_n_rows(input_path, no_of_rows)

    # Save to csv file
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow([row[0], row[1]])

def read_n_rows(file_path, n):
    rows = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= n:
                break
            rows.append(row)
    return rows

if __name__ == '__main__':
    main()