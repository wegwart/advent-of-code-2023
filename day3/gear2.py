import pathlib
import re

def process_lines(lines, i, gears):
    matches = re.finditer(r'\d+', lines[1])
    for match in matches:
        for j, line in enumerate(lines):
            gear_matches = re.finditer(r'[*]', line[match.start()-1:match.end()+1])            
            for gear_match in gear_matches:
                gear_id = 1000 * (i+j) + match.start()-1+gear_match.start()     
                if gear_id in gears:
                    gears[gear_id] = abs(gears[gear_id]) * int(match.group())
                else:
                    gears[gear_id] = -int(match.group())

def process(file):
    sum = 0
    gears = dict()
    with open(file) as f:        
        lines = ['.{}.'.format(line.strip()) for line in f]
        pad_line = '.' * len(lines[0])
        lines.insert(0, pad_line)
        lines.append(pad_line)
        for i in range(len(lines)-2):
            process_lines(lines[i:i+3], i, gears)
        for i, (gear_id, gear_ratio) in enumerate(gears.items()):
            if gear_ratio > 0:
                sum += gear_ratio
    return sum
    
__location__ = pathlib.Path(__file__).parent

def main():
    assert(process(__location__ / 'input.txt') == 467835)
    print(process(__location__ / 'input2.txt'))
    
if __name__ == '__main__':
    main()
