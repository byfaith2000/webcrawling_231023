# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def print_info(self):
#         print(f'name:{self.name}, age:{self.age}, address:{self.address}')
#
#
# obj1 = Person('smith', 40, 'utah')
# obj1.print_info()

# for i in range(4):
#     print(i)

# iter = range(4).__iter__()
# print(iter)
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())
# print(iter.__next__())

# ldata = [10,20,30,40]
# iter2 = ldata.__iter__()
# print(iter2)
# print(iter2.__next__())
# print(iter2.__next__())
# print(iter2.__next__())
# print(iter2.__next__())
# print(iter2.__next__())


class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            rvalue = self.current
            self.current += 1
            return rvalue
        else:
            raise StopIteration


for i in CustomRange(1, 5):
    print(i)