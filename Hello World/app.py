from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque

print('Hello World')
course = "Python Programming"
course1 = "Python \"Programming"
message = """abdc sas """  # triple string for long messages
print(len(message))  # find len of string
print(course[0])
print(course1[1:])
print(course[:4])
print(course[-1:3])

# escape sequeces are #, \, \\ , \n

first = "Karan"
last = "Aggarwal"
# full = first +" "+ last #formatted string can be written as below
full = f"{first} {last}"
print(full)
formated_string = f"{len(first)} + {2 + 2}"

# in python everything is an object and you can call functions on these objects which are referred to as methods

# String Methods:
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

# Numbers
x = 1
x = 1.1
x = 1+2j  # complex numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # int division
print(10 % 3)
print(10 ** 3)  # power

x = x+3
x += 3

# Number medthods
print(abs(2.9))
print(round(2.9))

# import math

# x = input("x: ")
x = "4"
y = int(x) + 1
print(type(x))
print(f"x: {x} , y: {y}")

# Falsy values, i.e, equivalent to bool value false
# ""
# 0
# None
# False

print(ord("b"))  # gives the ascii value

# logical operators and, or, not

# chaining comparision operators
age = 22
# if age >= 18 and age <25:
if 18 <= age < 25:
    print("Eligible")

# bag comes after apple so its true, next is false
if "bag" > "apple" and "bag" > "cat":
    print("bag")

# for-else loop, used to confirm if the for loop termination didn't occur because of the prior break statement
# [link text](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops)
# note here that the line under else doesn't get executed if the if block breaks, hence the else is needed
successful = False

for i in range(3):
    print("Attempt", i)
    if(successful):
        print("success")
        break
else:
    print("3 attempts completed")

# primitive types in python are int, str, float, boolean etc
# complex types in python are objects like range, len


print(type(5))
print(type(range(5)))

# iterables - range, str, list
# range object returned by range function is iterable
for x in range(5):
    print(x)

for x in "apple":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)


number = 100
while number > 5:
    print(number)
    # number = number // 2 # integer division
    number //= 2

command = ""
# while command.lower() != "quit":
# command = input(">")
print("Echo", command)

# or

# while True:
# command = input(">")
print("Echo", command)
# if command.lower() != "quit":
#    break

even_count = 0
for n in range(1, 10):
    if(n % 2 == 0):
        print(n)
        even_count += 1
# else:
    print(f"We have {even_count} even numbers")

# by default every function in python returns "None" value unless you explicitly make it retrun a value
print(print('hi'))


def increment(number, by):
    return number + by


# while calling functions you can make them more readable by prefixing the argument with the parameter
print(increment(2, by=1))

# to make the paramenters of a function optional
# all the optional parameters must be listed after all the required parameters while defining the function


def increment1(number, by=1):
    return number + by


# calling the above function without passing a value for by will make it use default value 1
print(increment1(2))


# defining a functions to take a variable number of arguments
# number and product variables are local variables with scope limited to the function
# message is a global varibles and remains in the memory longer and the interpreter does not
# add them into garbage collection as often as it does to local variables

message = "a"


def multiply(*numbers):
    global message  # to modify global variables in a function, but this practise should be avoided
    print(numbers)  # acts as a list
    product = 1
    for number in numbers:
        product *= number
    return product


print("start")  # debugging
print(multiply(2, 3, 4, 5))


# instead of passing a list in the previous example, we an use double * to pass a dictionary
def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)

# debugging
# add a breakpoint
# press debug icon or f9 to execute line by line
# if debugger lands on a function press f10 to go in
# inside the function keep pressng f10 to execute line by line
# to move out of a function that you know works fine press shift+f11
# shift + f5 to end debugger

# short-cuts
# 'home' for begining of line and 'end' for end
# ctr+home for beining of file and vice versa
# to move a line up instead of copy-paste press alt and up/down arrow
# for group of lines, select them and then same way
# to duplicate file shift+alt+up/down
# to comment lines of code select ctrl+ /
# to type any functions just type any of its letters in sequence and press tab to select from suggestions


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'fizbuzz'
    elif input % 3 == 0:
        return 'fizz'
    elif input % 5 == 0:
        return 'buzz'
    else:
        return input


print(fizz_buzz(7))
print(fizz_buzz(12))
print(fizz_buzz(20))
print(fizz_buzz(30))

# can be rewrittten as
# no need for elif an else we are returning in every if statement
# so only if value doesnt return in the previous if block will it move to next if block, hence no else


def fizz_buzz1(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'fizbuzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input


# lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]

zeros = [0]*5
print(zeros)

combined = zeros + letters
print(combined)

# list1 = [x:x in range(0, 21)]

# create a list using list funciton and passing any iterable

chars = list("Hello World")
numbers = list(range(20))

print(numbers)
print(chars)

print(len(chars))
print(numbers[:: 2])  # print every second number in list


# list unpacking
numbers = [0, 1, 2]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# or, can be written as below
# only requirement is no. of variables should equal number of items in the list
first, second, third = numbers
print(first, second, third)

# otherwise we can use the following syntax to store the unwanted items of the list into another list - others
# this is called unpacking and packing
numbers2 = [0, 2, 3, 4, 7, 9, 5, 3]
first1, second1, *others1 = numbers2
first2, *others2, last2 = numbers2

print(first1, second1)
print(others1)

print(first2, last2)
print(others2)

items1 = [0, "a"]
index1, letter1 = items1
print(index1, letter1)

# unpacking can also be applied to tuples
items2 = (0, "a")
index2, letter2 = items2
print(index2, letter2)

# looping over lists
# how to get a tuple of list items

letters = ["a", "b", "c"]

for letters in enumerate(letters):  # enumerate object is iterable
    print(letters)  # prints read-only typles
    print(letters[0], letters[1])  # prints index and item separatelyg


# neater way to print it is using tuple unpacking
for index, item in enumerate(letters):
    print(index, item)

# Add
letters = ["a", "b", "c"]
letters.append("d")
letters.insert(0, "_")  # to add at a specific index
print(letters)

# remove
letters.pop()
letters.pop(0)
# used when index not knowwn, removes first instance of the letter
letters.remove('b')
del letters[0:3]  # to remove range of items

letters.clear()  # to remove all the objects in a list

letters = ["a", "b", "c"]
print(letters.index("a"))

if "e" in letters:
    # will return error if no object hence we first confirm if it is there
    print(letters.index("e"))

print(letters.count("d"))

numbers = [3, 51, 2, 8, 6]
numbers.sort()
numbers.sort(reverse=True)

print(numbers)

# this returns a new list which is a sorted version of numbers
print(sorted(numbers))
print(sorted(numbers, reverse=True))


# sorting list of complex forms
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 21),
]

print(items[1])


def sort_item(item):
    return item[1]


# what above function is intended to do
print(items[1][1])

print(sort_item(items))

# passes each tuple of items list to sort_item
# which inturn returns the price of the product which is used for sorting the list
items.sort(key=sort_item)
print(items)

# lambda functions are anonymus funcitons
# to define functions that we are only going to use once as an argument to another function
# to avoid longer lines of code that goes into defining such a function only for 1 time use
# written as:    lambda parameters:expression

# above sort_item can be rewritten as a lambda funciton
# parameter for sort_item is item and return expression is item[1]
items.sort(key=lambda item: item[1])
print("check lambda")
print(items)
# transorming list of tuples to list of numbers

print("check append")
price = []
for item in items:
    price.append(item[1])

print(price)

# above can be achieved using a map function
# map funciton applies a lambda funciton on an iterable and returns an iterable object

x = map(lambda item: item[1], items)
print(x)

print("check map")

for item1 in x:
    print(item1)

print("check map list")
y = list(x)  # why didn't this take x from above?
print(y)

print("check map list2")
y = list(map(lambda item: item[1], items))
print(y)

# re-writing above as a list comprehension
# list comprehension is written as [expression for list_item in list]
print("map as list comprehension")
y = [item[1] for item in items]
print(y)


# another usecase for lamba
# filter function returns an iterable of values that satisfy the boolean expression

print("check filter")
x = list(filter(lambda item: item[1] >= 10, items))
print(x)

print("recheck map")
y = list(map(lambda item: item[1] >= 10, items))
print(y)

# re-writing above as a list comprehension
print("filter as list comprehension")
y = [item for item in items if item[1] >= 10]
print(y)

# zip funciton to combine two or more iterables, in this case a string and two lists
print("zip function to combine two lists")
list1 = [1, 2, 3]
list2 = [10, 20, 30]

x = zip('abc', list1, list2)
print(x)

y = list(x)
print(y)


# trying to implement zip using list comprehension, failed attempt
print("zip function using list comprehension1")
print((list1[0], list2[0]))
print(([lists1 for lists1 in list1], [lists2 for lists2 in list2]))

# trying to implement zip using list comprehension, successful attempt
print("zip function using list comprehension2")
print([(list1[i], list2[i]) for i in range(len(list1))])

# trying to implement zip using map, unsuccessful attempt
print("zip function using map funciton")
x, y = map(lambda lists1: lists1, list1), map(lambda lists1: lists1, list2)
print((list(x), list(y)))

# stacks in python using list
print("stacks using lists")
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print("stack")
print(browsing_session)
print("item at the end")
print(browsing_session[-1])

# before poping item check if list is not empty
# since an empty list [] is a falsey value
# we can check that a list is empty or not using the following expression
if not browsing_session:
    print("empty")
else:
    print("not empty")
    last = browsing_session.pop()
    print("poped on pressing back key in current browsing sesion")
    print(last)
# or

print(f"browsing session {browsing_session}")

if not len(browsing_session):
    print("empty")
else:
    print("not empty")
    last = browsing_session.pop()
    print("poped on pressing back key in current browsing sesion")
    print(last)

print(f"browsing session {browsing_session}")

browsing_session.pop()
print(f"browsing session {browsing_session}")

if not len(browsing_session):
    print("empty")
    print(f"items in stack: {len(browsing_session)}")


print(f"browsing session {browsing_session}")


# queue using lists FIFO
# everytime we remove the first item from the list, all the other objects need to shifted to the left
# this can become unstable for really long lists
# in such case we can use deque object

# this import line has been shifted by code runner plugin on the top section of this file
#from collections import deque

print("queues using deque")
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")


# tuples are immutable, i.e, we cannot add, modify or remove values in them
# sets are different from tuples because they can't have repeating values
# hence tuples are used when we want to store a sequence of objects and that sequence is sacrosanct
x = (1, 4, 5, 6, 7)

# print(x.pop()) #will throw error
# print(x.append(4)) #will throw error

# this is also tuple
print("/n tuples /n")
x = 1, 2
print(x)
print(type(x))

# singe tuple
x = 1,
print(x)
print(type(x))

# emplty typle
x = ()
print(x)
print(type(x))

# tuples can be combined like lists
x = (1, 2) + (2, 3) + (4,)
print(x)
print(type(x))

# tuples can also be created like lists
x = (1, 2) * 2
print(x)
print(type(x))

x = tuple([2, 3, 4])
y = tuple("hello world")
print(x, y)

print(y[0])
print(y[0:2])

# unpacking tuples
a, b, c = x
print(a, b, c)

# but unpacking needs equal no. of parameters on both sides
# i, j, k = y
# print(i, j, others)

# checking for items in tuples
if 'h' in y:
    print("exists in tuple")

#swapping in python
x = 11
y = 10

x, y = y, x

print('swap1')
print(x, y)
# this works because on the right side y,x represents a tuple (y,x),
# and on the left side we are unpacking a tuple (x,y)
#  so, it is equivalent to

print('swap2')
x, y = (y, x)
print(x, y)

# therefor we are able to define assignment of two variables like this:
a, b = 1, 2

# same tuple logic applies: (1,2) is a tuple and a,b are being unpacked from (a,b)

#arrays in python
# 90% cases we use lists but when arrays are used when we have a lists of 10K+ items
# then these become more efficient
# same behavior and methods like lists can be applied
#  but while creating arrays we need to use the right typecode parameter
# that represents the data type of items stored in the lists
# in the case below i represents signed int, can be found on google use keyword - "typecode"

# this import line has been shifted by code runner plugin on the top section of this file
#from array import array

numbers = array("i", [1, 2, 3, 7, 8, 5, 4])
numbers.pop()
print(numbers)
numbers.pop(2)
print(numbers)
numbers.append(4)
print(numbers)
numbers.remove(4)
print(numbers)
# numbers.clear()
numbers[0] = 6
print(numbers)
# numbers[3] = 7.0 will throw error because typecode is unsigned int and 7.0 is float

# emptys the array
del numbers[:]
print(numbers)
numbers.append(42)
print(numbers)

# sets in python are unordered collection, so their items cannot be accessed with an index
print("sets")
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5, 8, 9}
second.add(2)
second.remove(5)
len(second)
print(first)
print(second)

union = first | second
inter = first & second
# diff give items in first not in second
diff = first - second
# semantic difference gives items that are either in first and second but not both
seman = first ^ second

print(union, inter, diff, seman)

if 1 in first:
    print("exixts")

# dictionaries, key: value pairs
print("dictionaries")
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
print(point["x"])

point["x"] = 10
point["z"] = 20

# will throw error if key doesnt exist
# print(point["a"])

# to avoid this
if "a" in point:
    print(point["a"])

# or

# returns None if key doesn't exist
print(point.get("a"))
# use this to return 0 if key desn't exit
print(point.get("a", 0))

del point["x"]

# unpacking dictionaries
print("unpacking dictionaries")
for key in point:
    print(key, point[key])

for key in point.items():
    print(key)

for key, value in point.items():
    print(key, value)

# list comprehension
values_list = [x * 2 for x in range(5)]
print("list comp")
print(values_list)

# set comprehension
values_set = {x * 2 for x in range(5)}
print("set comp")
print(values_set)

# dict comprehension
values_dict = {x: x * 2 for x in range(5)}
print("dict comp")
print(values_dict)

# generator values
# used instead of lists when we intend to store a huge no. values in it, say a million
# in such a scenario using up memory would be ineffcient
print("generator values")
generator = (x * 2 for x in range(20))
print(generator)

for x in generator:
    print(x)


generator_values1 = (x * 2 for x in range(1000))
generator_values2 = (x * 2 for x in range(100000))
list_values = [x * 2 for x in range(1000)]

print("gen1:", getsizeof(generator_values1))
print("gen2:", getsizeof(generator_values2))
print("list:", getsizeof(list_values))


# print(len(generator_values1))
# this will throw error as generator doesn't store values in memory

# unpacking operator -> *
# returns an iterable
print("unpacking operator")
# unpack = *values_list
#print("type of unpacking operator: ", type(unpack))
print("list:", *values_list)
print("set:", *values_set)
print("dict1:", *values_dict)
# above is not the right way to deal with dictionaries
# print("dict2:", (**values_dict))


values = list(range(5))
print("values:", values)

values1 = [*range(5), *"Hello"]
values2 = [range(5)]
print("values1:", values1)
print("values2:", values2)

first = [1, 2, 3]
second = [5, 6, 7]
combine = [*first, *"abc", *second]
print("list combine:", combine)

# to unpack dict use **
first = {"x": 1}
second = {"x": 10, "y": 2}
combine1 = {*first, *second}
combine2 = {**first, **second, "z": 2}

print("dict combine1:", combine1)
print("dict combine2:", combine2)

# exercise
# find most repeated character

sentence = "This is a common interview question"
unique = set(sentence)
print(unique)

char = [*unique]
print(char)

# using list
list_count = [sentence.count(letter) for letter in char]
max_char = char[list_count.index(max(list_count))]
print("max repeated char by list method is:", max_char)

dict_count = {letter: sentence.count(letter) for letter in char}
print(dict_count)
max_char_dict = max(dict_count, key=dict_count.get)
print("max repeated charby dict method is:", max_char_dict)
print(dict_count.get)
print(type(dict_count.get))
# max = 0
# for key, value in dict_count.items:
#     if value > max:
#         max = value


# import pretty printing to get a well displayed output
# from pprint import pprint

char_frequency = {}
for char1 in sentence:
    if char1 in char_frequency:
        char_frequency[char1] += 1
    else:
        char_frequency[char1] = 1

pprint(char_frequency, width=1)

# calling items on dictionary returns a list of tuples of key value pairs
#pprint(sorted(char_frequency.items(), key=lambda char_frequency: char_frequency[1], reverse=True), width=20)
max_char_count = sorted(
    char_frequency.items(),
    key=lambda char_frequency: char_frequency[1],
    reverse=True)

print(max_char_count[0])
