import pathlib
import re

def process_lines(lines):
    sum = 0
    matches = re.finditer(r'\d+', lines[1])
    for match in matches:
        neighbours = ''
        for line in lines:
            neighbours += line[match.start()-1:match.end()+1]
        found = re.findall(r'[^0-9.]', neighbours)
        if len(found) > 0:
            sum += int(match.group())
    return sum

def process(file):
    sum = 0
    with open(file) as f:        
        lines = ['.{}.'.format(line.strip()) for line in f]
        pad_line = '.' * len(lines[0])
        lines.insert(0, pad_line)
        lines.append(pad_line)
        for i in range(len(lines)-2):
            sum += process_lines(lines[i:i+3])
    return sum
    
__location__ = pathlib.Path(__file__).parent

def main():
    assert(process(__location__ / 'input.txt') == 4361)
    print(process(__location__ / 'input2.txt'))
    
if __name__ == '__main__':
    main()
