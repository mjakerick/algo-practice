class DynamicArray:
    def __init__(self, capacity=1):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def pushback(self, val):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.arr[self.size] = val
        self.size += 1

    def popback(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.arr[self.size]

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.arr[index]

    def set(self, index, val):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[index] = val

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def _resize(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

