nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
            ]


class FlatIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.cursor = 0
        self.cursor_in = 0
        self.end = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        while self.cursor < len(self.my_list):
            if self.cursor_in < len(self.my_list[self.cursor]):
                result_in = self.my_list[self.cursor][self.cursor_in]
                self.cursor_in += 1
                return result_in
            self.cursor += 1
            self.cursor_in = 0
        raise StopIteration


if __name__ == '__main__':
    for elem in FlatIterator(nested_list):
        print(elem)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
