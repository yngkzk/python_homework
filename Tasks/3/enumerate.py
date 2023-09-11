keyBoard = [["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="]]

for row, keys in enumerate(keyBoard):
    for col, keys in enumerate(keys):
        print(row, col, keys)