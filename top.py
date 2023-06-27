import csv
import os

def main():
    # Version
    version = 2

    # Number of rows
    no_of_rows = (100, 250, 500, 1000, 5000, 10000)

    # Call function
    for n in no_of_rows:
        top(n, version)

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

if __name__ == '__main__':
    main()