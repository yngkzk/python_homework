import re
import sys


with open(sys.argv[1], encoding='utf-8') as file:
    text = file.read()

def find_and_convert_value(data):
    patterns = [r'([0-9]*?.?[0-9] [A-Z]{3})', r'([0-9]*[.]?[0-9]+?[$€])']
    result = []

    for pattern in patterns:
        result += (re.findall(pattern, data))
        for value in result:
            if value.endswith('$') or value.endswith('USD'):
                number = float(re.sub('[$]| USD', '', value))
                number *= 476.84
                number = str(round(number, 2)) + '₸'
                # result[result.index(value)] = str(round(number, 2)) + '₸' 
                data = data.replace(value, number)
            elif value.endswith('€') or value.endswith('EUR'):
                number = float(re.sub('[€]| EUR' , '', value))
                number *= 501.99
                number = str(round(number, 2)) + '₸'
                data = data.replace(str(value), str(number))
    return data

value = find_and_convert_value(text)

with open(sys.argv[2], 'w', encoding='utf-8') as secondFile:
    secondFile.write(value)