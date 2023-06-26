def read_n_lines(file_path, n):
    lines = []
    with open(file_path, 'r') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break
            lines.append(line.rstrip('\n'))  # Remove newline character

    return lines

def strip_frequency(lines):
    for i in range(len(lines)):
        # keep text after :
        line = lines[i].split(':')[-1]
        # remove whitespace
        line = line.strip()
        # update the element in the lines list
        lines[i] = line
    return lines

# variables (set here)
no_of_lines = 10000
file_path = 'data/output.txt'
    
# call function
lines = read_n_lines(file_path, no_of_lines)

# process lines

lines = strip_frequency(lines)
    


# save to file
with open(f'output/top_{no_of_lines}.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
