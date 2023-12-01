import pathlib

def get_calibration_values(calibration):
    with open(calibration) as f:
        calibration_values = []
        for line in f:
            digits = ''.join([x for x in line if x.isdigit()])
            calibration_value = int(digits[0] + digits[-1])
            calibration_values.append(calibration_value)
    return calibration_values
    
def get_answer(calibration):
    return sum(get_calibration_values(calibration))

__location__ = pathlib.Path(__file__).parent

def test_get_answer_example():
    assert(get_answer(__location__ / 'calibration_example.txt') == 142)
  
def get_answer_puzzle():   
    print(get_answer(__location__ / 'calibration_puzzle.txt'))
    
if __name__ == '__main__':
    test_get_answer_example()
    get_answer_puzzle()