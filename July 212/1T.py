def get_diag_words(element=None):
    if element:
        word = ''
        for i in range(len(element)):
            for x in range(len(element[i])):
                if i < x:
                    continue
                elif i > x:
                    continue
                else:
                    word += element[i][x]
        word += ' '

        for y in range(len(element)):
            length = len(element[y])
            index = length - y - 1
            word += element[y][index]
        return word
    else:
        return ''


def test_get_diag_words():
    input = [['ж','ф','л'],
             ['р','и','а'],
             ['с','з','л']]
    expect = "жил лис"
    assert get_diag_words(input) == expect

    input = [['б','ф','л','т',']','в'],
             ['р','е','а','о','о','щ'],
             ['е','и','л','р','э','к'],
             ['г','ы','о','а','ф','о'],
             ['н','н','а','а','я','ч'],
             ['а','з','л','ц','в',' ']]
    expect = "белая  ворона"
    assert get_diag_words(input) == expect

    input = []
    expect = ""
    assert get_diag_words(input) == expect

test_get_diag_words()
