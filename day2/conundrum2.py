import pathlib
import math

config = {
    'red': 12,
    'green': 13,
    'blue': 14    
}

def process(file):
    with open(file) as f:
        sum = 0
        for line in f:
            sets = line.strip().split(': ')[1].split('; ')
            for c in config:
                config[c] = 0
            for set in sets:
                cubes = set.split(', ')
                for cube in cubes:
                    count = int(cube.split(' ')[0])
                    color = cube.split(' ')[1]
                    if count > config[color]:
                        config[color] = count
            sum += math.prod(config.values())
    return sum
    
__location__ = pathlib.Path(__file__).parent

def main():
    assert(process(__location__ / 'input.txt') == 2286)
    print(process(__location__ / 'input2.txt'))
    
if __name__ == '__main__':
    main()