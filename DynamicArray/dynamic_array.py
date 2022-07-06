import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.create_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            raise IndexError("Index is out of bounds!")
        return self.A[index]

    def append(self, ele):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        self.A[self.n] = ele
        self.n += 1

    def resize(self, capacity):
        temp_arr = self.create_array(capacity)

        for i in range(self.n):
            temp_arr[i] = self.A[i]

        self.A = temp_arr
        self.capacity = capacity

    def create_array(self, capacity):
        return (capacity * ctypes.py_object)()
