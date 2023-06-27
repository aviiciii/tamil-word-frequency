import csv
import json

csv_file = 'output/v3/top_250.csv'  # Replace with the path to your CSV file
json_file = 'data.json'  # Replace with the desired path for the JSON file

words = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        words.append(row[0])
        
# use double in list
words_json = json.dumps(words, indent=2, ensure_ascii=False)

with open(json_file, 'w') as file:
    file.write(words_json)

print("Conversion to JSON completed. Output saved at:", json_file)
