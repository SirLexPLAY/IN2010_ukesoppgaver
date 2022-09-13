
class Set:
    _data = []

    def contains(self, x):
        for element in self._data:
            if x == element:
                return True
        return False
    

    def insert(self, x):
        if not self.contains(x):
            self._data.append(x)
        else:
            print(f"{x} is already in the set.")

    
    def remove(self, x):
        if self.contains(x):
            self._data.remove(x)
        else:
            print(f"{x} does not exist in the set.")


    def size(self):
        count = 0
        for element in self._data:
            count += 1
        
        return count


class Test:
    data = Set()

    def read_input():
        file_name = input("Input file name: ")
        file = open(file_name)

        amount_lines = int(file.readline())
        line = 1

        while line <= amount_lines:
            strings = file.readline().strip()  # the operation

            if (strings[0] == "contains"):
                self.data.contains(int(strings[1]))
