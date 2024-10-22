class RevertedListIterator:
    def __init__(self, input_list):
        self.input_list = input_list
        self.list_length = len(self.input_list)

    def __setattr__(self, key, value):
        if key == 'input_list' and isinstance(value, list) is not True:
            raise TypeError("The input object type must be a list")

        super().__setattr__(key, value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_length > 0:
            self.list_length -= 1
            return self.input_list[self.list_length]
        else:
            raise StopIteration


class EvenNumbersIterator:
    def __init__(self, finite_num):
        self.finite_num = finite_num
        self.current = -1

    def __setattr__(self, key, value):
        if key == 'finite_num' and isinstance(value, int) is not True:
            raise TypeError("The finite number must be integer")
        if key == 'finite_num' and value <= 0:
            raise ValueError("The finite number must be greater than 0")

        super().__setattr__(key, value)

    def __iter__(self):
        return self

    def __next__(self):
        while self.current < self.finite_num:
            self.current += 1
            if self.current % 2 == 0:
                return self.current
        raise StopIteration
