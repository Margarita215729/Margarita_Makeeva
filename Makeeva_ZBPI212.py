def fact(x):
    if x<=1:
        return 1
    else:
        return (x*fact(x-1))


def filter_even(li):
    lst = map(int, li.split(' '))
    res = filter(lambda x: (x % 2 == 0), lst)
    return " ".join(map(str,res))


def square(li):
    sqli = [i ** 2 for i in map(int, li.split())]
    return sqli

def bin_search(li, element):
    left = 0
    right = len(li) - 1
    while right >= left:
        mid = (right + left) // 2
        if li[mid] > element:
            right = mid - 1
        elif li[mid] < element:
            left = mid + 1
        else:
            return mid
    return -1


def is_palindrome(string):
    str = string.replace(' ','').lower()
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return 'NO'
    return 'YES'

def calculate(path2file):
    with open(path2file, 'r') as file:
        a = []
        for i in file:
            ex = i.split()
            if ex[0] == '+':
                answer = int(ex[1]) + int(ex[2])
                a.append(answer)
            elif ex[0] == '-':
                answer = int(ex[1]) - int(ex[2])
                a.append(answer)
            elif ex[0] == '*':
                answer = int(ex[1]) * int(ex[2])
                a.append(answer)
            elif ex[0] == '/':
                answer = int(ex[1]) / int(ex[2])
                a.append(answer)
            elif ex[0] == '**':
                answer = int(ex[1]) ** int(ex[2])
                a.append(answer)
            elif ex[0] == '//':
                answer = int(ex[1]) // int(ex[2])
                a.append(answer)
            elif ex[0] == '%':
                answer = int(ex[1]) % int(ex[2])
                a.append(answer)
        return ','.join(map(str,a))
    file.close()


def substring_slice(path2file_1,path2file_2):
    with open(path2file_1, 'r') as file1:
        with open(path2file_2, 'r') as file2:
            a = []
            for x in file1:
                for y in file2:
                    y = y.split()
                    a.append(x[int(y[0]):int(y[1])+1])
                    break
    return ' '.join(a)
    file1.close()
    file2.close()


import json

def decoded_ch(string_of_elements):
    periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
    start_index = 0
    end_index = 1
    result = ''
    while end_index <= len(string_of_elements):
        if string_of_elements[start_index: end_index] in periodic_table and \
        (string_of_elements[end_index: end_index + 1].isupper() or end_index == len(string_of_elements)):
            result += periodic_table[string_of_elements[start_index: end_index]]
            start_index = end_index
        end_index += 1
    return result

class Student:
    def __init__(self, name, surname, grades=None):
        if grades is None:
            grades = [3, 4, 5]
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def greeting(self):
        return f'Hello, I am {self.fullname}'

    def mean_grade(self):
        return sum(self.grades)/len(self.grades)

    def is_otlichnik(self):
        return 'Yes' if self.mean_grades() >= 4.5 else 'NO'

    def __add__(self, other):
        return f'{self.name} is friends with {other.name}'

    def __str__(self):
        return self.fullname


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)
