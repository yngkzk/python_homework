import re
import sys


with open(sys.argv[1], encoding='utf-8') as file:
    text = file.read()

def find_value(data):
    patterns = [r'([0-9]*?.?[0-9] [A-Z]{3})', r'([0-9]*[.]?[0-9]+?[$€])']
    value = []

    for pattern in patterns:
        value += (re.findall(pattern, data))
    return value

value = find_value(text)

def convert_value(data):
    for value in data:
        if value.endswith('$') or value.endswith('USD'):
            number = float(re.sub('[$]| USD', '', value))
            number *= 476.84
            data[data.index(value)] = str(round(number, 2)) + '₸' 
        elif value.endswith('€') or value.endswith('EUR'):
            number = float(re.sub('[€]| EUR' , '', value))
            number *= 501.99
            data[data.index(value)] = str(round(number, 2)) + '₸' 
    return data

converted_value = convert_value(value)

with open(sys.argv[2], 'w', encoding='utf-8') as secondFile:
    secondFile.write(' '.join(converted_value))