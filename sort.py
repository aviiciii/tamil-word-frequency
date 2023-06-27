import csv

# Path to the large CSV file
csv_path = 'data/output/2.csv'
output_path = 'data/output/filtered/2.csv'

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
