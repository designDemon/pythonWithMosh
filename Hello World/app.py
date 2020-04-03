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
# note here that the line under else doesn't get executed if the if block breaks
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
#command = input(">")
print("Echo", command)

# or

# while True:
#command = input(">")
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
