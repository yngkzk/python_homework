class FileFAQ:
    count = 0
    average_length = 0

    def __init__(self, file):
        self.file = file

    def _read_line(self, file):
        print('Дошел')
        with open(self.file, encoding='utf-8') as file:
            for line in file:
                yield line

    def _line_and_length_counter(self, line):
        total_length = 0
        self.count = 0
        for x in self._read_line(line):
            if x == '\n':
                continue
            total_length += len(x)
            self.count += 1
        self.average_length = total_length / self.count

    def info(self):
        self._line_and_length_counter(self.file)
        return f"Средняя длина строк в файле - {round(self.average_length, 1)}, всего строк в файле - {self.count}"

file = FileFAQ('file.txt')
print(file.info())