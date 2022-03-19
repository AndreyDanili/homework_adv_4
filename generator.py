if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
                ]

    nested_list_2 = [
        [['a', [1, 4, [6]]], 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
                ]

    def FlatIterator(my_list):
        start = 0
        end = len(my_list)
        if start == end:
            raise StopIteration
        for elements in my_list:
            for element in elements:
                yield element

    def FlatIterator_2(my_list):
        for elements in my_list:
            if isinstance(elements, list):
                yield from FlatIterator_2(elements)
            else:
                yield elements

    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('*' * 50)

    for item in FlatIterator_2(nested_list_2):
        print(item)
    flat_list = [item for item in FlatIterator_2(nested_list_2)]
    print(flat_list)
