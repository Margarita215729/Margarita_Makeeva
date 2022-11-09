# Тема - массивы
# Написать программу, выводящую на экран треугольник Паскаля с вершиной n, заданной с клавиатуры
# https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/

def create_array():
    n = int(input())
    pyramid_list = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(i-j)
            pyramid_list.append(row)
    return pyramid_list


arr = create_array()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print("{:<3}".format(arr[i][j]), end=" ")
    print()


# Тема - классы
# Create a class Triangle with methods :
# Maximum range of a triangle's third edge.
# Minimum range of a triangle's third edge.
# https://edabit.com/challenge/Zerwo2AENbvRZTe83


class Triangle:

    def __init__(self, first, second):
        self.first = first
        self.second = second


    def max_third(self):
        max_third_side = self.first + self.second - 1
        return max_third_side

    def min_third(self):
        min_third_side = max(self.first, self.second) - min(self.first, self.second) + 1
        return min_third_side


def main():
    Treyg = Triangle(3,6)
    print(Treyg.max_third())
    print(Treyg.min_third())

main()



# Тема - генераторы
# Create a generator to return the fibonnaci sequence starting from the first element up to (n).
# The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# https://github.com/joaoventura/full-speed-python/blob/master/chapters/generators.md


def fibonnaci(n):
    current = 0
    next = 1
    i = 0
    while i < n:
        value = current
        yield value
        current = next
        next += value
        i += 1


for i in fibonnaci(12):
    print(i)