from math import *

print(floor(3.7))
# name = input("Enter your name: ")
# print("Hello " + name + "!")

friends = ["ali", "veli", "sureyya", "ayse", "mehmet"]
print(friends.sort())
friends[0] = "mali"
print(friends[4])
print(friends[1:])
print(friends[1:3])
print(friends[0])

lucky_numbers = [1, 2, 3, 4, 5, 6, 7]
lucky_numbers.reverse()

friends.extend(lucky_numbers)
friends.append("leyla")
friends.append("suheyla")
friends.insert(1, "mahmut")
friends.remove("mali")
# to clear the list
# friends.clear()

# remove last element of the list
friends.pop()
print("index: ", friends.index("veli"))
print(friends.count("veli"))
print(friends)

friends2 = friends.copy()
print(friends2)

# tuples - they cant be mutated
coordinates = (4, 5)
print(coordinates[0])


# functions
def say_hi(user, age):
    print(f"hi {user}!! You are {age}")


say_hi("mikey", 3)


def cube(num):
    return num * num * num


print(cube(3))

# if statements

is_female = True
is_tall = False

if is_female or is_tall:
    print("you are a female or tall or both")
else:
    print("You are neither a female nor tall")

is_male = False
is_short = True

if is_male and is_short:
    print("You are a short male.")
elif is_male and not is_short:
    print("You are a tall male.")
elif not is_male and is_short:
    print("You are not a male but short.")
else:
    print("You are either a tall male or not both")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 50, 7))

# check two values are equals: == not equals_ !=

# check the length of a string
print("length of the string deniz: ", len("deniz"))


# calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter first operator: ")
# num2 = float(input("Enter first number: "))

def calculator(num_one, op, num_two):
    num1 = float(num_one)
    num2 = float(num_two)
    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    else:
        return "Invalid operator"


print(calculator(4, "+", 6))

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(month_conversions["Jan"])
# if the key is not valid, second argument will be shown
print(month_conversions.get("Mar", "not a valid key"))

i = 1
while i <= 10:
    print(i)
    i += 1

print("done with while loop")

for letter in "Sipidik oldurmeli":
    print(letter)

# for friend in friends:
#    print(friend)

# 5 is not included
for index in range(5):
    print(index)

for ind in range(2, 9):
    print(ind)


# for index in range(len(friends)):
#    print(index)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print("raise_to_power result: ", raise_to_power(2, 3))

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)


# vowels become the letter "g"
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiuo":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate("heyo"))

# instead of breaking the program and specify the error otherwise it will be too broad:
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err:
    print(err)
    # print("Invalid input")
'''

# "r" stands for read, "w" write with that you can change the file
# "a" append info to the file, "r+" read & write
employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print("for loop: ", employee)

print(employee_file.readable())
# read all lines
# print(employee_file.read())

#read one line
print(employee_file.readline())

# readlines puts info in an array (list)
print(employee_file.readlines())
# print(employee_file.readlines()[1])

# whenever you open the file, you want to close it as well
employee_file.close()

employee_v2_file = open("employees_v2.txt", "a")
employee_v2_file.write("Toby - Human Resources")
employee_v2_file.write("\nKelly - Customer Service")

employee_v2_file.close()

'''
write command will overwrite the whole file and add only the new line Toby - HR
employee_v2_file = open("employees_v2.txt", "w")
employee_v2_file.write("Toby - Human Resources")
'''

# create new file
employee_v3_file = open("employees_v3.txt", "w")
employee_v3_file.write("Toby - Human Resources")
employee_v3_file.close()

from StudentFile import Student

student1 = Student("Jim", "Business", "3.3", False)
print(student1)
print(student1.name)