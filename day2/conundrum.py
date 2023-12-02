import pathlib

config = {
    'red': 12,
    'green': 13,
    'blue': 14    
}

def process(file):
    with open(file) as f:
        sum = 0
        for line in f:
            id = line.strip().split(': ')[0].split(' ')[1]
            game = line.strip().split(': ')[1]
            sets = game.split('; ')
            possible = True
            for set in sets:
                cubes = set.split(', ')
                for cube in cubes:
                    count = cube.split(' ')[0]
                    color = cube.split(' ')[1]
                    if int(count) > config[color]:                       
                        possible = False
            if possible:                
                sum += int(id)
    return sum
    
__location__ = pathlib.Path(__file__).parent

def main():
    assert(process(__location__ / 'input.txt') == 8)
    print(process(__location__ / 'input2.txt'))
    
if __name__ == '__main__':
    main()
