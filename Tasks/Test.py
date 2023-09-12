
# key = "tan"

_display = '5251'

# if key == "log":
#     display = list(display)
#     cut_word = ['l', 'o', 'g', '10', '(']
#     for x in range(5):
#         display.insert(x, cut_word[x])
#         display.append(')')
#         display = ''.join(display)

# if key == "2√x":
#     display = list(display)
#     cut_word = [')', '*', '*', '0.5']
#     for x in range(4):
#         display.append(cut_word[x])
#         display.insert(0, '(')
#         display = ''.join(display)

# if key == "tan":
#     display = list(display)
#     cut_word = ['t', 'a', 'n', '(']
#     for x in range(4):
#         display.insert(x, cut_word[x])
#         display.append(')')
#         display = ''.join(display)


def insert_function(key):
    global _display
    display = list(display)
    cut_word = list(key)
    cut_word.append('(')
    for x in range(len(cut_word)):
        display.insert(x, cut_word[x])
    display.append(')')
    display = ''.join(display)
    return display


print(insert_function('tan'))
