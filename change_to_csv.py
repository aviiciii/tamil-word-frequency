import csv

def main():
    # read the file
    filename = 'data/output.txt'
    with open(filename) as f:
        lines = f.readlines()
    
    # seperate the frequency and the word
    for i in range(len(lines)):
        line = lines[i].split(':')
        lines[i] = line

    # remove the whitespace
    for i in range(len(lines)):
        lines[i][0] = lines[i][0].strip()
        lines[i][1] = lines[i][1].strip()
    
    # shift word to the front
    for i in range(len(lines)):
        lines[i][0], lines[i][1] = lines[i][1], lines[i][0]


    # change to csv
    with open('data/output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'frequency'])
        for line in lines:
            writer.writerow(line)

    # write to csv file
if __name__ == '__main__':
    main()