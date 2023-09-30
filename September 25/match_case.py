import time


# 1 Простой пример Match-Case

def get_day_name(day):
    match day:
        case 1: return 'Monday'  # SyntaxError: '->' invalid syntax
        case 2: return 'Tuesday'
        case 3: return 'Wednesday'
        case 4: return 'Thursday'
        case 5: return 'Friday'
        case 6: return 'Saturday'
        case 7: return 'Sunday'
        case _:  # SyntaxError: 'else:' invalid syntax
            return 'Nothing'


# for x in range(1, 9):
#     print(get_day_name(x))
#     time.sleep(0.25)


# 2 Сопоставление по типам данных

def get_type(value):
    match value:
        case int(value): return 'this is a int'  #  SyntaxError: name capture 'int' makes remaining patterns unreachable
        case str(value): return 'this is a str' 
        case tuple(value): return 'this is a tuple'
        case _:  # SyntaxError: 'else:' invalid syntax
            return 'Nothing'
        

# print(get_type(27))
# print(get_type('hello'))
# print(get_type(('hello', 'im', 'a', 'tuple')))


# 3 Сопоставление и деконструкция

def deconstruct(data):
    match data:
        case [x, y]: return f'this is a list of "{x}" and "{y}"'
        case (x, y, z): return f'this is a tuple of "{x}", "{y}" and "{z}"'
        case _:
            return 'Nothing'
        

# print(deconstruct(['im a', 'list']))
# print(deconstruct((2, 'hello', 7)))
# print(deconstruct(1))


# 3.1 Еще пример деконструкции

def get_quadrant(point):
    match point:
        case (x, y) if x > 0 and y > 0: return f'this point in the 1st quadrant: x={x}, y={y}' 
        case (x, y) if x < 0 and y > 0: return f'this point in the 2nd quadrant: x={x}, y={y}'
        case (x, y) if x < 0 and y < 0: return f'this point in the 3rd quadrant: x={x}, y={y}'
        case (x, y) if x > 0 and y < 0: return f'this point in the 4th quadrant: x={x}, y={y}'
        case _:
            return 'Congratulations, you have unlocked the fifth dimension'
        

# print(get_quadrant((1, 1)))
# print(get_quadrant((-1, 1)))
# print(get_quadrant((-1, -1)))
# print(get_quadrant((1, -1)))


# 4 Сопоставление словарей

def deconstruct_dict(data):
    match data:
        case {'name': str(name), 'age': int(age)}:  # <-- {'name': str, 'age': int}
            return f'Dictionary with keys {data["name"]} and {data["age"]}'
        case _:
            return 'Nothing'
        

# print(deconstruct_dict({'name': 'Python', 'age': 32}))
# print(deconstruct_dict({'name': 55, 'age': 'python'}))
# print(deconstruct_dict({'name': 'Python', 'age': '64'}))
# print(deconstruct_dict({'name': 27, 'age': 32}))


# 5 Вариативное сопоставление

def guess_number(num):
    match num:
        case 0 | 1: return '0 or 1'
        case 2 | 3 | 4: return '2, 3 or 4'
        case _:
            return 'Another number'
        

# for x in range(6):
#     print(guess_number(x))
#     time.sleep(0.25)


# 6 Расширенный синтаксис

# Расширенный синтаксис больше не доступен
